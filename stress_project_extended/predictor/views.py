
import os, json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.db import models
from .forms import SignupForm, QuestionForm, MoodForm, TaskForm, JournalForm, PhysiologicalDataForm
from .models import Response, MoodEntry, Task, JournalEntry, PhysiologicalData
from .ml_predictor import get_predictor

# Initialize ML predictor
predictor = get_predictor()

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'predictor/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created. You can login now.')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'predictor/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'predictor/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def question_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            resp = form.save(commit=False)
            resp.user = request.user
            # Rule-based prediction for questionnaire
            features = [getattr(resp, f'q{i}') for i in range(1,11)]
            total = sum(features)
            if total <= 35:
                resp.predicted_level = 'Low Stress'
            elif total <= 65:
                resp.predicted_level = 'Medium Stress'
            else:
                resp.predicted_level = 'High Stress'
            resp.save()
            return render(request, 'predictor/result.html', {'response': resp})
    else:
        form = QuestionForm()
    return render(request, 'predictor/questions.html', {'form': form})

@login_required
def ml_predict_view(request):
    """ML-based stress prediction using physiological data"""
    if request.method == 'POST':
        form = PhysiologicalDataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            
            # Prepare features for prediction
            features_dict = {

                'Resp_mean': data.Resp_mean,
                'Resp_std': data.Resp_std,
                'TEMP_mean': data.TEMP_mean,
                'TEMP_std': data.TEMP_std,
                'TEMP_slope': data.TEMP_slope,
                'age': data.age,
                'height': data.height,
                'weight': data.weight,
            }
            
            # Make prediction
            if predictor.is_loaded():
                predicted_label, confidence = predictor.predict(features_dict)
                data.predicted_level = predicted_label
                if confidence:
                    data.confidence_amused = confidence.get('Amused', 0)
                    data.confidence_neutral = confidence.get('Neutral', 0)
                    data.confidence_stressed = confidence.get('Stressed', 0)
            else:
                data.predicted_level = 'Model not available'
                messages.warning(request, 'ML model not loaded. Please train the model first.')
            
            data.save()
            return render(request, 'predictor/ml_result.html', {'data': data})
    else:
        form = PhysiologicalDataForm()
    
    return render(request, 'predictor/ml_predict.html', {
        'form': form,
        'model_loaded': predictor.is_loaded()
    })

@login_required
def dashboard_view(request):
    # show recent responses and mood entries
    responses = Response.objects.filter(user=request.user).order_by('-created_at')[:30]
    moods = MoodEntry.objects.filter(user=request.user).order_by('-created_at')[:30]
    ml_predictions = PhysiologicalData.objects.filter(user=request.user).order_by('-created_at')[:30]
    
    # prepare simple chart data for Chart.js
    chart_labels = [r.created_at.strftime('%Y-%m-%d') for r in responses[::-1]]
    chart_data = [ (1 if r.predicted_level=='Low Stress' else 2 if r.predicted_level=='Medium Stress' else 3) for r in responses[::-1] ]
    
    return render(request, 'predictor/dashboard.html', {
        'responses': responses, 
        'moods': moods, 
        'ml_predictions': ml_predictions,
        'chart_labels': json.dumps(chart_labels), 
        'chart_data': json.dumps(chart_data),
        'model_loaded': predictor.is_loaded()
    })

@login_required
def mood_add(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.user = request.user
            m.save()
            messages.success(request, 'Mood entry saved.')
            return redirect('dashboard')
    else:
        form = MoodForm()
    return render(request, 'predictor/mood_add.html', {'form': form})

@login_required
def tasks_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('completed','due_date')
    form = TaskForm()
    return render(request, 'predictor/tasks_list.html', {'tasks': tasks, 'form': form})

@login_required
def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            t.user = request.user
            t.save()
            messages.success(request, 'Task added.')
    return redirect('tasks')

@login_required
def task_toggle(request, pk):
    t = get_object_or_404(Task, pk=pk, user=request.user)
    t.completed = not t.completed
    t.save()
    return redirect('tasks')

@login_required
def task_delete(request, pk):
    t = get_object_or_404(Task, pk=pk, user=request.user)
    t.delete()
    return redirect('tasks')

@login_required
def journal_list(request):
    # show recent anonymous and user's entries
    if request.user.is_authenticated:
        entries = JournalEntry.objects.filter(models.Q(anonymous=True) | models.Q(user=request.user)).order_by('-created_at')[:50]
    else:
        entries = JournalEntry.objects.filter(anonymous=True).order_by('-created_at')[:50]
    return render(request, 'predictor/journal_list.html', {'entries': entries})

@login_required
def journal_add(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            j = form.save(commit=False)
            if not j.anonymous:
                j.user = request.user
            j.save()
            messages.success(request, 'Journal entry saved.')
            return redirect('journal')
    else:
        form = JournalForm()
    return render(request, 'predictor/journal_add.html', {'form': form})

def resources_view(request):
    resources = [
        {'title':'5-minute breathing exercise','url':'https://youtu.be/VpHz8Mb13_Y?si=ct48n0FuL_BuuHJF'},
        {'title':'How to manage stress - article','url':'https://www.healthline.com/health/stress'},
        {'title':'Emergency helpline (example)','url':'tel:+911234567890'}
    ]
    return render(request, 'predictor/resources.html', {'resources': resources})
@login_required
def breathing_videos(request):
    videos = [
        {
            'title': '5-Minute Guided Breathing Exercise',
            'youtube_id': 'inpok4MKVLM'
        },
        {
            'title': 'Deep Breathing for Stress Relief',
            'youtube_id': 'tot2hU_Zj4Y'
        },
        {
            'title': 'Relaxing Box Breathing Technique',
            'youtube_id': 'tEmt1Znux58'
        },
        {
            'title': '10-Minute Anxiety Relief Meditation',
            'youtube_id': 'O-6f5wQXSu8'
        },
        {
            'title': 'Calming Breathwork for Beginners',
            'youtube_id': 'nmFUDkj1Aq0'
        }
    ]
    return render(request, 'predictor/breathing_videos.html', {'videos': videos})

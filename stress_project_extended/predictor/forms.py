
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Response, MoodEntry, Task, JournalEntry, PhysiologicalData

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Response
        exclude = ['user','predicted_level','created_at']
        widgets = {f'q{i}': forms.NumberInput(attrs={'min':1,'max':10,'class':'form-control'}) for i in range(1,11)}
        labels = {
            'q1': 'On a scale of 1–10, how often do you feel overwhelmed or unable to cope with daily tasks?',
            'q2': 'How frequently do you experience mood swings, irritability, or anxiety without a clear reason?',
            'q3': 'Do you find it difficult to concentrate or make decisions lately?',
            'q4': 'How many hours of sleep do you get on average per night? (Rate 1-10, where 10 = 8+ hours)',
            'q5': 'How often do you exercise or engage in physical activity each week? (Rate 1-10, where 10 = daily)',
            'q6': 'How would you rate your daily workload or academic/work pressure (1–10)?',
            'q7': 'How much time do you spend on social media daily? (Rate 1-10, where 10 = 5+ hours)',
            'q8': 'Do you experience frequent headaches, muscle tension, or fatigue? (Rate 1-10)',
            'q9': 'How often do you consume caffeine, alcohol, or nicotine-based products? (Rate 1-10)',
            'q10': 'Do you feel you have enough emotional support from family, friends, or colleagues? (Rate 1-10, where 10 = strong support)',
        }

class MoodForm(forms.ModelForm):
    class Meta:
        model = MoodEntry
        fields = ['mood_scale','note']
        widgets = {'mood_scale': forms.NumberInput(attrs={'min':1,'max':10,'class':'form-control'}),
                   'note': forms.Textarea(attrs={'rows':3,'class':'form-control'})}

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter task title'}),
            'due_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'})
        }

class JournalForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['anonymous','content']
        widgets = {'content': forms.Textarea(attrs={'rows':4,'class':'form-control'})}


class PhysiologicalDataForm(forms.ModelForm):
    class Meta:
        model = PhysiologicalData
        exclude = ['user', 'predicted_level', 'confidence_amused', 'confidence_neutral', 'confidence_stressed', 'created_at']
        widgets = {
            'BVP_mean': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': 'e.g., 0.025'}),
            'BVP_std': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': 'e.g., 0.015'}),
            'BVP_peak_freq': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': 'e.g., 1.2'}),
            'EDA_phasic_mean': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': 'e.g., 0.05'}),
            'EDA_phasic_min': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': 'e.g., 0.01'}),
            'EDA_smna_min': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': 'e.g., 0.02'}),
            'EDA_tonic_mean': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': 'e.g., 0.1'}),
            'Resp_mean': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': 'e.g., 0.3'}),
            'Resp_std': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': 'e.g., 0.05'}),
            'TEMP_mean': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'e.g., 32.5'}),
            'TEMP_std': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.001', 'placeholder': 'e.g., 0.2'}),
            'TEMP_slope': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.0001', 'placeholder': 'e.g., 0.001'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '120', 'placeholder': 'e.g., 27'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'min': '50', 'max': '250', 'placeholder': 'Height in cm, e.g., 175'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'min': '20', 'max': '300', 'placeholder': 'Weight in kg, e.g., 70'}),
        }
        labels = {
            'BVP_mean': 'Blood Volume Pulse - Mean',
            'BVP_std': 'Blood Volume Pulse - Std Dev',
            'BVP_peak_freq': 'Blood Volume Pulse - Peak Frequency',
            'EDA_phasic_mean': 'EDA Phasic - Mean',
            'EDA_phasic_min': 'EDA Phasic - Min',
            'EDA_smna_min': 'EDA SMNA - Min',
            'EDA_tonic_mean': 'EDA Tonic - Mean',
            'Resp_mean': 'Respiration - Mean',
            'Resp_std': 'Respiration - Std Dev',
            'TEMP_mean': 'Temperature - Mean (°C)',
            'TEMP_std': 'Temperature - Std Dev',
            'TEMP_slope': 'Temperature - Slope',
            'age': 'Age (years)',
            'height': 'Height (cm)',
            'weight': 'Weight (kg)',
        }

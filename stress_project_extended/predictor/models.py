
from django.db import models
from django.contrib.auth.models import User

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    predicted_level = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.predicted_level or 'Pending'}"

class PhysiologicalData(models.Model):
    """Store physiological sensor data for ML prediction"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # BVP (Blood Volume Pulse) features
    BVP_mean = models.FloatField()
    BVP_std = models.FloatField()
    BVP_peak_freq = models.FloatField()
    
    # EDA (Electrodermal Activity) features
    EDA_phasic_mean = models.FloatField()
    EDA_phasic_min = models.FloatField()
    EDA_smna_min = models.FloatField()
    EDA_tonic_mean = models.FloatField()
    
    # Respiration features
    Resp_mean = models.FloatField()
    Resp_std = models.FloatField()
    
    # Temperature features
    TEMP_mean = models.FloatField()
    TEMP_std = models.FloatField()
    TEMP_slope = models.FloatField()
    
    # User demographics
    age = models.IntegerField()
    height = models.IntegerField()  # in cm
    weight = models.IntegerField()  # in kg
    
    # Prediction results
    predicted_level = models.CharField(max_length=30, blank=True, null=True)
    confidence_amused = models.FloatField(null=True, blank=True)
    confidence_neutral = models.FloatField(null=True, blank=True)
    confidence_stressed = models.FloatField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.predicted_level or 'Pending'} at {self.created_at}"

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood_scale = models.IntegerField()  # 1-10
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.mood_scale} on {self.created_at.date()}"

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} - {'Done' if self.completed else 'Pending'}"

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    anonymous = models.BooleanField(default=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        who = 'Anonymous' if self.anonymous else (self.user.username if self.user else 'Anonymous')
        return f"{who} - {self.created_at.date()}"

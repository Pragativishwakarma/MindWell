
from django.contrib import admin
from .models import Response, MoodEntry, Task, JournalEntry, PhysiologicalData
@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('user','predicted_level','created_at')
@admin.register(MoodEntry)
class MoodAdmin(admin.ModelAdmin):
    list_display = ('user','mood_scale','created_at')
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','user','completed','due_date')
@admin.register(JournalEntry)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('anonymous','user','created_at')

@admin.register(PhysiologicalData)
class PhysiologicalDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'predicted_level', 'confidence_stressed', 'created_at')
    list_filter = ('predicted_level', 'created_at')
    search_fields = ('user__username',)
    readonly_fields = ('created_at',)

from django import forms 
from home.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'start_date' : forms.DateInput(attrs =  {'type' : 'date'})
        }


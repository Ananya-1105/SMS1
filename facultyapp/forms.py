from django import forms
from .models import Task, AddCourse
from .models import Marks

class TaskForm (forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']


class AddCourseForm(forms.ModelForm):
   class Meta:
        model = AddCourse
        fields = ['student' , 'course' , 'section']


class MarksForm (forms.ModelForm) :
    class Meta:
        model=Marks
        fields = ['student' , 'course' , 'marks']





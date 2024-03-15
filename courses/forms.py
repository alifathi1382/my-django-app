from django import forms
from .models import Courses

DEPARTMENT_CHOICES = [
    ('فنی و مهندسی', 'فنی و مهندسی'),
    ('علوم پایه', 'علوم پایه'),
    ('ادبیات و علوم انسانی', 'ادبیات و علوم انسانی'),
    ('مدیریت و اقتصاد', 'مدیریت و اقتصاد'),
    ('کشاورزی', 'کشاورزی'),
    ('منابع طبیعی', 'منابع طبیعی'),
    ('دامپزشکی', 'دامپزشکی'),
    ('شیمی', 'شیمی'),
]


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'
        labels = {
            "cid": "course id",
            "cname": "course name",
            "department": "department",
            "credit": "credit",
        }
        widgets = {
            "cid": forms.TextInput(attrs={'type': 'number', 'placeholder': 'like 10000'}),
            "cname": forms.TextInput(attrs={'placeholder': 'eg. Prosenjeet'}),
            "department": forms.Select(choices=DEPARTMENT_CHOICES),
            "credit": forms.NumberInput(attrs={'placeholder': 'eg. 3'}),  # Changed to NumberInput
        }

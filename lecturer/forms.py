from django import forms
from persiantools.jdatetime import JalaliDate
from .models import Lecturer


class SolarDateWidget(forms.DateInput):
    def format_value(self, value):
        if isinstance(value, JalaliDate):
            return value.strftime('%Y-%m-%d')
        return super().format_value(value)


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
MAJOR_CHOICES = [
    ('مهندسی کامپیوتر', 'مهندسی کامپیوتر'),
    ('مهندسی برق الکترونیک', 'مهندسی برق الکترونیک'),
    ('مهندسی برق قدرت', 'مهندسی برق قدرت'),
    ('مهندسی مکانیک و پلیمر', 'مهندسی مکانیک و پلیمر'),
    ('مهندسی معدن', 'مهندسی معدن'),
    ('مهندسی عمران', 'مهندسی عمران'),
    ('مهندسی شهرسازی', 'مهندسی شهرسازی'),
]
BORN_CITY_CHOICES = [
    ('اراک', 'اراک'),
    ('اردبیل', 'اردبیل'),
    ('تبریز', 'تبریز'),
    ('اصفهان', 'اصفهان'),
    ('اهواز', 'اهواز'),
    ('ایلام', 'ایلام'),
    ('بجنورد', 'بجنورد'),
    ('بندرعباس', 'بندرعباس'),
    ('بوشهر', 'بوشهر'),
    ('بیرجند', 'بیرجند'),
    ('ارومیه', 'ارومیه'),
    ('تهران', 'تهران'),
    ('خرم آباد', 'خرم آباد'),
    ('رشت', 'رشت'),
    ('زاهدان', 'زاهدان'),
    ('زنجان', 'زنجان'),
    ('ساری', 'ساری'),
    ('سمنان', 'سمنان'),
    ('سنندج', 'سنندج'),
    ('شهرکرد', 'شهرکرد'),
    ('شیراز', 'شیراز'),
    ('قزوین', 'قزوین'),
    ('قم', 'قم'),
    ('کرج', 'کرج'),
    ('کرمان', 'کرمان'),
    ('کرمانشاه', 'کرمانشاه'),
    ('گرگان', 'گرگان'),
    ('مشهد', 'مشهد'),
    ('همدان', 'همدان'),
    ('یاسوج', 'یاسوج'),
    ('یزد', 'یزد'),
]


class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = '__all__'
        labels = {
            'lid': 'Lecturer ID',
            'fname': 'First Name',
            'lname': 'Last Name',
            'idi': 'Identification Number',
            'department': 'Department',
            'major': 'Major',
            'birth': 'Birth Date',
            'borncity': 'Born City',
            'address': 'Address',
            'PostalCode': 'Postal Code',
            'CPhone': 'Cell Phone',
            'hphone': 'Home Phone',
            'lcourseids': 'Lecturer Courses'
        }
        widgets = {
            "lid": forms.NumberInput(attrs={'placeholder': 'Enter Lecturer ID'}),
            "fname": forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            "lname": forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            "idi": forms.NumberInput(attrs={'placeholder': 'Enter Identification Number'}),
            "department": forms.Select(choices=DEPARTMENT_CHOICES),
            "major": forms.Select(choices=MAJOR_CHOICES),
            "birth": SolarDateWidget(),  # Assuming you have a SolarDateWidget defined
            "borncity": forms.Select(choices=BORN_CITY_CHOICES),
            "address": forms.TextInput(attrs={'placeholder': 'Enter Address'}),
            "PostalCode": forms.NumberInput(attrs={'placeholder': 'Enter Postal Code'}),
            "CPhone": forms.TextInput(attrs={'placeholder': 'Enter Cell Phone'}),
            "hphone": forms.TextInput(attrs={'placeholder': 'Enter Home Phone'}),
            "lcourseids": forms.TextInput(attrs={'placeholder': 'Enter Lecturer Courses'})
        }




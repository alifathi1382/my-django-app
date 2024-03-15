from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import re


# Create your models here.
def validate_persian(value):
    if not all('\u0600' <= char <= '\u06FF' for char in value):
        raise ValidationError(_('Only Persian characters are allowed.'))

    if re.search(r'[0-9@#%`!$&*()_+=]', value):
        raise ValidationError(_('Numbers or special characters are not allowed.'))


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


class Courses(models.Model):
    cid = models.BigIntegerField(primary_key=True, validators=[MinValueValidator(10000), MaxValueValidator(99999)])
    cname = models.CharField(max_length=25, validators=[validate_persian])
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
    credit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

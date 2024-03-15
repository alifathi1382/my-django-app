from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import re

from courses.models import Courses

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


def validate_persian(value):
    if not all('\u0600' <= char <= '\u06FF' for char in value):
        raise ValidationError(_('Only Persian characters are allowed.'))

    if re.search(r'[0-9@#%`!$&*()_+=]', value):
        raise ValidationError(_('Numbers or special characters are not allowed.'))


def phonenumbercheck(value):
    if len(value) != 11:
        raise ValidationError("Phone number must be 11 digits long.")
    if value[0] != '0' or value[1] != '9':
        raise ValidationError("Phone number must start with '09'.")
    for digit in value[2:]:
        if not digit.isdigit():
            raise ValidationError("Phone number must contain only digits.")


def homephonenumbercheck(value):
    if len(value) != 11:
        raise ValidationError("Home phone number must be 11 digits long.")
    prefix = value[0] + value[1] + value[2]
    valid_prefixes = [
        "041", "044", "045", "026", "031", "084", "077", "021", "038", "056",
        "051", "058", "061", "024", "023", "054", "071", "028", "025", "087",
        "034", "083", "074", "017", "013", "066", "011", "086", "076", "081",
        "035"
    ]
    if prefix not in valid_prefixes:
        raise ValidationError("Invalid prefix for home phone number.")
    for digit in value[3:]:
        if not digit.isdigit():
            raise ValidationError("Home phone number must contain only digits.")


def validate_course_ids(value):
    # Split the provided IDs by comma
    course_ids = value.split(',')
    # Check if each ID exists in the Courses table
    for course_id in course_ids:
        try:
            course = Courses.objects.get(cid=course_id.strip())
        except Courses.DoesNotExist:
            raise ValidationError(f"Course with ID {course_id.strip()} does not exist.")


# Create your models here.
class Lecturer(models.Model):
    stid = models.BigIntegerField(primary_key=True, validators=[MinValueValidator(100000), MaxValueValidator(999999)])
    fname = models.CharField(max_length=25, validators=[validate_persian])
    lname = models.CharField(max_length=25, validators=[validate_persian])
    father =models.CharField(max_length=25,validators=[validate_persian])
    birth = models.DateField()
    ids = models.CharField()

    idi = models.BigIntegerField(unique=True)
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
    major = models.CharField(max_length=30, choices=MAJOR_CHOICES)

    borncity = models.CharField(max_length=40, choices=BORN_CITY_CHOICES)
    address = models.CharField(max_length=100)
    PostalCode = models.BigIntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    CPhone = models.CharField(max_length=11, unique=True, validators=[phonenumbercheck])
    hphone = models.CharField(max_length=11, validators=[homephonenumbercheck])
    lcourseids = models.CharField(max_length=5, validators=[validate_course_ids])

    def __str__(self):
        return f"{self.fname}{self.lname}"

    def clean(self):
        super().clean()
        if self.idi:
            if not self.validate_id_number():
                raise ValidationError("Invalid ID number")

    def validate_id_number(self):
        id_number = str(self.idi)
        if len(id_number) != 10:
            return False
        b = 0
        temp_a = self.idi
        for i in range(2, 11):
            temp_a //= 10
            b += (temp_a % 10) * i
        c = b % 11
        if c < 2 and int(id_number[-1]) == c:
            return True
        elif c >= 2 and int(id_number[-1]) == 11 - c:
            return True
        else:
            return False
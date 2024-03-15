# Generated by Django 5.0.3 on 2024-03-10 19:47

import django.core.validators
import lecturer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lecturer",
            fields=[
                (
                    "lid",
                    models.BigIntegerField(
                        primary_key=True,
                        serialize=False,
                        validators=[
                            django.core.validators.MinValueValidator(100000),
                            django.core.validators.MaxValueValidator(999999),
                        ],
                    ),
                ),
                (
                    "fname",
                    models.CharField(
                        max_length=25, validators=[lecturer.models.validate_persian]
                    ),
                ),
                (
                    "lname",
                    models.CharField(
                        max_length=25, validators=[lecturer.models.validate_persian]
                    ),
                ),
                ("idi", models.BigIntegerField(unique=True)),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("فنی و مهندسی", "فنی و مهندسی"),
                            ("علوم پایه", "علوم پایه"),
                            ("ادبیات و علوم انسانی", "ادبیات و علوم انسانی"),
                            ("مدیریت و اقتصاد", "مدیریت و اقتصاد"),
                            ("کشاورزی", "کشاورزی"),
                            ("منابع طبیعی", "منابع طبیعی"),
                            ("دامپزشکی", "دامپزشکی"),
                            ("شیمی", "شیمی"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "major",
                    models.CharField(
                        choices=[
                            ("مهندسی کامپیوتر", "مهندسی کامپیوتر"),
                            ("مهندسی برق الکترونیک", "مهندسی برق الکترونیک"),
                            ("مهندسی برق قدرت", "مهندسی برق قدرت"),
                            ("مهندسی مکانیک و پلیمر", "مهندسی مکانیک و پلیمر"),
                            ("مهندسی معدن", "مهندسی معدن"),
                            ("مهندسی عمران", "مهندسی عمران"),
                            ("مهندسی شهرسازی", "مهندسی شهرسازی"),
                        ],
                        max_length=30,
                    ),
                ),
                ("birth", models.DateField()),
                (
                    "borncity",
                    models.CharField(
                        choices=[
                            ("اراک", "اراک"),
                            ("اردبیل", "اردبیل"),
                            ("تبریز", "تبریز"),
                            ("اصفهان", "اصفهان"),
                            ("اهواز", "اهواز"),
                            ("ایلام", "ایلام"),
                            ("بجنورد", "بجنورد"),
                            ("بندرعباس", "بندرعباس"),
                            ("بوشهر", "بوشهر"),
                            ("بیرجند", "بیرجند"),
                            ("ارومیه", "ارومیه"),
                            ("تهران", "تهران"),
                            ("خرم آباد", "خرم آباد"),
                            ("رشت", "رشت"),
                            ("زاهدان", "زاهدان"),
                            ("زنجان", "زنجان"),
                            ("ساری", "ساری"),
                            ("سمنان", "سمنان"),
                            ("سنندج", "سنندج"),
                            ("شهرکرد", "شهرکرد"),
                            ("شیراز", "شیراز"),
                            ("قزوین", "قزوین"),
                            ("قم", "قم"),
                            ("کرج", "کرج"),
                            ("کرمان", "کرمان"),
                            ("کرمانشاه", "کرمانشاه"),
                            ("گرگان", "گرگان"),
                            ("مشهد", "مشهد"),
                            ("همدان", "همدان"),
                            ("یاسوج", "یاسوج"),
                            ("یزد", "یزد"),
                        ],
                        max_length=40,
                    ),
                ),
                ("address", models.CharField(max_length=100)),
                (
                    "PostalCode",
                    models.BigIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1000000000),
                            django.core.validators.MaxValueValidator(9999999999),
                        ]
                    ),
                ),
                (
                    "CPhone",
                    models.CharField(
                        max_length=11,
                        unique=True,
                        validators=[lecturer.models.phonenumbercheck],
                    ),
                ),
                (
                    "hphone",
                    models.CharField(
                        max_length=11, validators=[lecturer.models.homephonenumbercheck]
                    ),
                ),
                (
                    "lcourseids",
                    models.CharField(
                        max_length=5, validators=[lecturer.models.validate_course_ids]
                    ),
                ),
            ],
        ),
    ]
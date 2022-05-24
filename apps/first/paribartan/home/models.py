from django.db import models
from django import forms
# Create your models here.
'''
blood_choice = (
    (1, "A+"),
    (2, "A-"),
    (3, "B+"),
    (4, "B-"),  
    (5, "O+"),
    (6, "O-"),
    (7, "AB+"),
    (8, "AB-"),
)

gender_choice = (
    (1, "Male"),
    (2, "Female"),
    (3, "Other"), 
)

martial_choice = (
    (1, "Married"),
    (2, "Unmarried"),
    (3, "Divorced"),
)

education_choice = (
    (1, "Primary"),
    (2, "Upper_primary"),
    (3, "Secondary"),
    (4, "Higher Secondary"),
    (5, "Bachelor"),
    (6, "Master"),
)
'''
BLOOD_CHOICES = (
    ('AP', "A+"),
    ('AS', "A-"),
    ('BA', "B+"),
    ('BS', "B-"),  
    ('OP', "O+"),
    ('OS', "O-"),
    ('ABP', "AB+"),
    ('ABS', "AB-"),
)

GENDER_CHOICES = [
    ('ML', 'Male'),
    ('FE', 'Female'),
    ('OT', 'Other'),
    ]

MARTIAL_CHOICES =[
    ('MA', "Married"),
    ("UN", "Unmarried"),
    ('DI', "Divorced"),
]

EDUCATION_CHOICES = [
    ('PR', "Primary"),
    ('UP', "Upper_primary"),
    ('SP', "Secondary"),
    ('HS', "Higher Secondary"),
    ('BA', "Bachelor"),
    ('MA', "Master"),
]

class Register(models.Model):
    name = models.CharField(max_length=122)
    phone = models.IntegerField()
    address = models.CharField(max_length=122)
    email = models.EmailField(max_length=122)
    password1 = models.CharField(max_length=122)
    password2 = models.CharField(max_length=122)
    birth_date = models.DateField(max_length=122)

    blood_group = models.CharField(
        max_length=5,
        choices= BLOOD_CHOICES
    )
  
    gender = models.CharField(
        max_length=3,
        choices=GENDER_CHOICES
    )

    martial_status = models.CharField(
        max_length=3,
        choices=MARTIAL_CHOICES
    )

    education = models.CharField(
        max_length=3,
        choices=EDUCATION_CHOICES
    )

    def __str__(self):
        return self.name
    '''
    blood_group = models.TypedChoiceField(
                   choices = blood_choice,
                   coerce = str
                  )
    gender = models.TypedChoiceField(
                   choices = gender_choice,
                   coerce = str
                  )
    martial_status = models.TypedChoiceField(
                   choices = martial_choice,
                   coerce = str
                  )
    
    education_status = models.TypedChoiceField(
                   choices = education_choice,
                   coerce = str
                  )
    '''
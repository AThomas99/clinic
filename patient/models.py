from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    is_reception = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
    

class Department(models.Model):
    name = models.CharField(max_length=20)

class Doctor(models.Model):

    DOCTORT_SPECIALZATION = (
        ('Pediatrician', 'Pediatrician'), # Specializes in young patients, age: 18-21
        ('Gynecologist', 'Gynecologist'), # Specializes in women's health
        ('Psychiatrist', 'Psychiatrist'), # Specializes in mental health
        ('Cardiologist', 'Cardiologist'), # Specializes in treatment of heart and blood vessels
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone must be entered in the format: '+255' up to 15 digits allowed. ")
    phoneNumber = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(max_length=254)
    department = models.ForeignKey(Department, related_name='department-doctor', on_delete=models.SET_NULL)
    specialisation = models.CharField(choices=DOCTORT_SPECIALZATION, blank=False, null=False)

    def __str__(self):
        return self.email
    

class Patient(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    gender = models.CharField(max_length=1, choices=GENDER, blank=False, null=False)
    age = models.IntegerField(null=False, blank=False)
    telno = models.CharField(max_length=12)
    address = models.CharField(max_length=200, blank=True, null=True)
    registered = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey(Doctor, related_name='doctor-patient', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Vital(models.Model):
    patient = models.OneToOneField(Patient, related_name='patient',on_delete=models.CASCADE)
    body_temperature = models.CharField(max_length=10, null=False, blank=False)
    body_pressure = models.CharField(max_length=10, null=False, blank=False)
    pulse_rate = models.CharField(max_length=10, null=False, blank=False)
    respiration_rate = models.CharField(max_length=10, null=False, blank=False)
    body_height = models.CharField(max_length=10, null=False, blank=False)
    body_weight = models.CharField(max_length=10, null=False, blank=False)


    def __str__(self):
        return f"{self.patient.first_name}"
    

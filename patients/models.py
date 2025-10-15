from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    medical_history = models.TextField()


class Insurance(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="insurances"
    )
    provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)
    expiration_date = models.DateField()


class MedicalRecord(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="medical_records"
    )
    date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    follow_up_date = models.DateField()

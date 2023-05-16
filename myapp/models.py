from django.db import models

class User(models.Model):
    ssn_number = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    rank = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'

class Weapon(models.Model):
    serial_number = models.CharField(max_length=255, primary_key=True)
    user_ssn_number = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_ssn_number', related_name='weapons')
    si_type = models.CharField(max_length=255)
    weapon_status = models.BooleanField(default=True)

    class Meta:
        db_table = 'weapons'
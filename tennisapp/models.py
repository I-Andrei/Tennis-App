from django.db import models

class Coach(models.Model):
    coach_name_text = models.CharField(max_length=200)
    dob_date = models.DateTimeField('date of birth')

class Tennis_Practices(models.Model):
    practice_date = models.DateTimeField('date practice')
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
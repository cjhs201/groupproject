from django.db import connections
from django.db import models

class UserDetails(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    study_year = models.IntegerField()
    class Meta:
        db_table = "users"
from django.db import connections
from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    study_year = models.IntegerField()
    class Meta:
        db_table = "users"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
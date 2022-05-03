from django.db import models

# Create your models here.
class UsersManagement(models.Model):
    user_id = models.CharField(max_length=8,primary_key=True)
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    user_tel = models.CharField(max_length=11)
    user_ident = models.BooleanField("0:用户,1:员工")


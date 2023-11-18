from django.db import models


# Create your models here.
state_choice=((
    ('bihar','bihar'),('m.p','m.p'),('u.p','u.p')
))
class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    # phone=models.IntegerField(primary_key=True)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    state=models.CharField(choices=state_choice,max_length=50)
    loction=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    pimage=models.ImageField(upload_to='static/pimages',blank=True)
    rdoc=models.FileField(upload_to='static/rdocs',blank=True)

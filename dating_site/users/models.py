
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import allauth.socialaccount

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    name=models.CharField(max_length=100,default="")
    status=models.CharField(max_length=100,default="")
    hobbies=models.CharField(max_length=100,default="")
    age=models.IntegerField(default=18)
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
    )

    def __str__(self):
        return f'{self.user.username} Profile'
    
    #this method is used to override the save method and thus we can change the size of our image
    # def save(self):
    #     super().save()
    #     img=Image.open(self.image.path)
    #     if img.height>300 or img.width>300:
    #         output_size=(300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)



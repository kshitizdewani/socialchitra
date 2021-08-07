from django.db import models

# Create your models here.

class WhyUs(models.Model):
    content = models.CharField(max_length=200,blank=False, null=False)
    hide = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.hide:
            return '(Hidden) '+self.content
        return self.content

class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team')
    bio = models.CharField(max_length=200)
    hide = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
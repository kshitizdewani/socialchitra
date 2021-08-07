from django.db import models

# Create your models here.

class WhyUs(models.Model):
    content = models.CharField(max_length=200,blank=False, null=False)
    hidden = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.hidden:
            return '(Hidden) '+self.content
        return self.content

class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team')
    bio = models.CharField(max_length=200)
    hidden = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.hidden:
            return '(Hidden) '+self.name
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to="services")
    hidden = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.hidden:
            return '(Hidden) '+self.title
        return self.title
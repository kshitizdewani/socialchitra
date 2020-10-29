from django.db import models
from django.urls import reverse

# Create your models here.
from django.utils.text import slugify


class Blog(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    author=models.CharField(max_length=50,blank=False,null=False)
    created=models.DateField(auto_now_add=True)
    body=models.TextField(max_length=2000)
    thumbnail=models.ImageField(upload_to='blogs',help_text='size: 1920x1080')
    slug = models.SlugField(default='', editable=False, null=False, max_length=200,help_text='PLEASE KEAVE THIS FIELD EMPTY.')

    class Meta:
        ordering = ['-id']

    def __str__(self): return f'{self.id}) {self.title}'

    def snippet(self):
        return self.body[:160]+'...'

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1

        if Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if (not self.slug) or (self.slug==""):
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

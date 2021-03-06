from django.conf import settings
from django.db import models

# Create your models here.


class Work(models.Model):
    title = models.CharField('タイトル', max_length=128)
    company = models.ForeignKey(settings.AUTH_USER_MODEL,
                                verbose_name='企業',
                                on_delete=models.CASCADE)
    salary_max = models.IntegerField()
    salary_min = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

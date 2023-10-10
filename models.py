from django.db import models

# Create your models here.

class QandA():
    question = models.CharField(blank=True, null=True, max_length=255)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question
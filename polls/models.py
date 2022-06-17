import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


Q1_CHOICES = (
    ('1', 'Reincarnation'),
    ('2', 'Go to a holy place'),
    ('3', 'Nothing'),
)


class Response(models.Model):
    name = models.CharField(max_length=100)
    q1 = models.CharField(choices=Q1_CHOICES, max_length=200)
    q2 = models.CharField(max_length=10)
    q3 = models.CharField(max_length=10)
    q4 = models.CharField(max_length=10)
    q5 = models.CharField(max_length=10)
    q6 = models.CharField(max_length=10)
    q7 = models.CharField(max_length=10)
    q8 = models.CharField(max_length=10)
    q9 = models.CharField(max_length=10)
    q10 = models.CharField(max_length=10)
    q11 = models.CharField(max_length=10)

    class Meta:
        verbose_name = "User response"

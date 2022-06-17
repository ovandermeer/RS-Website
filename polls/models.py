import datetime

from django import forms
from django.db import models
from django.utils import timezone
from django.contrib import admin

from django.forms import ModelForm


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

Q2_CHOICES = (
    ('1', 'One (Monotheistic)'),
    ('2', 'More than one God'),
    ('3', 'More than one aspect of one God'),
    ('4', 'None'),
)

class Response(models.Model):
    name = models.CharField(max_length=100)
    q1 = models.CharField(choices=Q1_CHOICES, max_length=200, verbose_name="What do you believe happens after you die?")
    q2 = models.CharField(choices=Q2_CHOICES, max_length=200, verbose_name="How many deities are in your religion?")
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


class ResponseForm(ModelForm):
    q1 = forms.ChoiceField(choices=Q1_CHOICES, widget=forms.RadioSelect)
    q2 = forms.MultipleChoiceField(choices=Q2_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Response
        fields = ['name', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11']


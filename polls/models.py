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

Q3_CHOICES = (
    ('1', 'Regimented prayer schedule'),
    ('2', 'Recommended prayer'),
    ('3', 'Meditation'),
    ('4', 'Group prayer'),
)

Q4_CHOICES = (
    ('1', 'Eating And Drinking Restrictions'),
    ('2', 'Fasting'),
    ('3', 'Who you can marry'),
    ('4', 'Pre-marital sex'),
    ('5', 'Virtually None'),
    ('6', 'Cutting hair'),
    ('7', 'Gender Identity/Sexuality'),
)

Q5_CHOICES = (
    ('1', 'Yes'),
    ('2', 'No'),
)

Q6_CHOICES = (
    ('1', 'Worships in a building of religious significance of a specific week day each week'),
    ('2', 'Often happens in a building of religious significance but sometimes happens in an informal setting, on a specific day of the week'),
    ('3', 'Worship is not on a specific day, or no common gathering place'),
)

Q7_CHOICES = (
    ('1', 'Yes'),
    ('2', 'No'),
)

Q8_CHOICES = (
    ('1', 'Yes'),
    ('2', 'No'),
)

Q9_CHOICES = (
    ('1', 'Start showing up'),
    ('2', 'Specific ritual'),
    ('3', 'Through birth or a special council'),
)

Q10_CHOICES = (
    ('1', 'No specific way'),
    ('2', 'The heavens and earth were created in six days, and on the seventh day, God rested.'),
    ('3', 'The God(s) created it and it is just an extension of the God(s)')
)

Q11_CHOICES = (
    ('1', 'Through the clergy'),
    ('2', 'Personal Relationship'),
)

class Response(models.Model):
    name = models.CharField(max_length=100)
    q1 = models.CharField(choices=Q1_CHOICES, max_length=200, verbose_name="What do you believe happens after you die?")
    q2 = models.CharField(choices=Q2_CHOICES, max_length=200, verbose_name="How many deities are in your religion?")
    q3 = models.CharField(max_length=10, choices=Q3_CHOICES, verbose_name="Types And Amount Of Prayer?")
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
    q2 = forms.ChoiceField(choices=Q2_CHOICES, widget=forms.RadioSelect)
    q3 = forms.ChoiceField(choices=Q3_CHOICES, widget=forms.RadioSelect)
    q4 = forms.MultipleChoiceField(choices=Q4_CHOICES, widget=forms.CheckboxSelectMultiple)
    q5 = forms.ChoiceField(choices=Q5_CHOICES, widget=forms.RadioSelect)
    q6 = forms.ChoiceField(choices=Q6_CHOICES, widget=forms.RadioSelect)
    q7 = forms.ChoiceField(choices=Q7_CHOICES, widget=forms.RadioSelect)
    q8 = forms.ChoiceField(choices=Q8_CHOICES, widget=forms.RadioSelect)
    q9 = forms.ChoiceField(choices=Q9_CHOICES, widget=forms.RadioSelect)
    q10 = forms.ChoiceField(choices=Q10_CHOICES, widget=forms.RadioSelect)
    q11 = forms.ChoiceField(choices=Q11_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Response
        fields = ['name', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11']


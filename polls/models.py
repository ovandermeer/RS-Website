from django import forms
from django.db import models

from django.forms import ModelForm

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
    ('2', 'Mandatory fasting'),
    ('3', 'Restrictions on who you can marry'),
    ('4', 'No pre-marital sex'),
    ('5', 'Restrictions on Gender Identity/Sexuality'),
    ('6', 'Restrictions on Cutting hair'),
    ('7', 'None of the above'),
)

Q5_CHOICES = (
    ('1', 'Yes'),
    ('2', 'No'),
)

Q6_CHOICES = (
    ('1', 'Worships in a building of religious significance of a specific week day each week'),
    ('2',
     'Often happens in a building of religious significance but sometimes happens in an informal setting, '
     'on a specific day of the week'),
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
    # name = models.CharField(max_length=100)
    q1 = models.CharField(max_length=10, choices=Q1_CHOICES, verbose_name="What do you believe happens after you die?")
    q2 = models.CharField(max_length=10, choices=Q2_CHOICES, verbose_name="How many deities are in your religion?")
    q3 = models.CharField(max_length=10, choices=Q3_CHOICES, verbose_name="Types And Amount Of Prayer?")
    q4 = models.CharField(max_length=10, choices=Q4_CHOICES, verbose_name="What kind of rules and restrictions do you find acceptable?")
    q5 = models.CharField(max_length=10, choices=Q5_CHOICES, verbose_name="Do you want to travel/go on a pilgrimage?")
    q6 = models.CharField(max_length=10, choices=Q6_CHOICES,
                          verbose_name="Preferred type of meeting place for your religious gatherings")
    q7 = models.CharField(max_length=10, choices=Q7_CHOICES,
                          verbose_name="Does sitting with people of the opposite sex distract you from the service?")
    q8 = models.CharField(max_length=10, choices=Q8_CHOICES,
                          verbose_name="Do you want your place of worship to open during non-service times for "
                                       "personal prayer?")
    q9 = models.CharField(max_length=10, choices=Q9_CHOICES, verbose_name="Preferred method of joining a religion")
    q10 = models.CharField(max_length=10, choices=Q10_CHOICES,
                           verbose_name="How do you think the world/universe was created?")
    q11 = models.CharField(max_length=10, choices=Q11_CHOICES,
                           verbose_name="Do you wish to attain spiritual enlightenment through you or religious "
                                        "authorities?")

    class Meta:
        verbose_name = "User response"


class ResponseForm(ModelForm):
    q1 = forms.ChoiceField(label="What do you believe happens after you die?", choices=Q1_CHOICES,
                           widget=forms.RadioSelect)
    q2 = forms.ChoiceField(label="How many deities are in your religion?", choices=Q2_CHOICES, widget=forms.RadioSelect)
    q3 = forms.ChoiceField(label="Types And Amount Of Prayer?", choices=Q3_CHOICES, widget=forms.RadioSelect)
    q4 = forms.MultipleChoiceField(label="What kind of rules and restrictions do you find acceptable?", choices=Q4_CHOICES,
                                   widget=forms.CheckboxSelectMultiple)
    q5 = forms.ChoiceField(label="Do you want to travel/go on a pilgrimage?", choices=Q5_CHOICES,
                           widget=forms.RadioSelect)
    q6 = forms.ChoiceField(label="Preferred type of meeting place for your religious gatherings", choices=Q6_CHOICES,
                           widget=forms.RadioSelect)
    q7 = forms.ChoiceField(label="Does sitting with people of the opposite sex distract you from the service?",
                           choices=Q7_CHOICES, widget=forms.RadioSelect)
    q8 = forms.ChoiceField(
        label="Do you want your place of worship to open during non-service times for personal prayer?",
        choices=Q8_CHOICES, widget=forms.RadioSelect)
    q9 = forms.ChoiceField(label="Preferred method of joining a religion", choices=Q9_CHOICES, widget=forms.RadioSelect)
    q10 = forms.ChoiceField(label="How do you think the world/universe was created?", choices=Q10_CHOICES,
                            widget=forms.RadioSelect)
    q11 = forms.ChoiceField(label="Do you wish to attain spiritual enlightenment through you or religious authorities?",
                            choices=Q11_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Response
        # fields = ['name', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11']
        fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11']

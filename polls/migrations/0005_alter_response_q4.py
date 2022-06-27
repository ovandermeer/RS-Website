# Generated by Django 4.0.5 on 2022-06-22 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_response_q1_alter_response_q10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='q4',
            field=models.CharField(choices=[('1', 'Eating And Drinking Restrictions'), ('2', 'Fasting'), ('3', 'Who you can marry'), ('4', 'No Pre-marital sex'), ('5', 'Virtually No restrictions'), ('6', 'No Cutting hair'), ('7', 'Gender Identity/Sexuality')], max_length=10, verbose_name='What kind of rules and restrictions do you find acceptable?'),
        ),
    ]
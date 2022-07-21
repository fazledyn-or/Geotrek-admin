# Generated by Django 3.1.14 on 2022-07-20 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0034_workflowdistrict'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportstatus',
            name='display_in_legend',
            field=models.BooleanField(default=True, help_text='Whether or not this status should be displayed in legend', verbose_name='Display in legend'),
        ),
    ]

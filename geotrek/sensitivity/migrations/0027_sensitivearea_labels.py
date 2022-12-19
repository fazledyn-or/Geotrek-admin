# Generated by Django 3.2.16 on 2022-12-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0028_alter_recordsource_name'),
        ('sensitivity', '0026_alter_sensitivearea_geom_buffered'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensitivearea',
            name='labels',
            field=models.ManyToManyField(to='common.Label', verbose_name='Labels'),
        ),
    ]

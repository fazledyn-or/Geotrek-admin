# Generated by Django 3.2.18 on 2023-04-07 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zoning', '0102_auto_20220919_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restrictedarea',
            name='area_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='zoning.restrictedareatype', verbose_name='Restricted area'),
        ),
    ]

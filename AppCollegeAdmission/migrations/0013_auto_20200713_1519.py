# Generated by Django 3.0.3 on 2020-07-13 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCollegeAdmission', '0012_auto_20200713_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedstudent',
            name='Percentage',
            field=models.FloatField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='selectedstudent',
            name='Percentage',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
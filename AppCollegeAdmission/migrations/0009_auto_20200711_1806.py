# Generated by Django 3.0.3 on 2020-07-11 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCollegeAdmission', '0008_auto_20200711_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='CollegeOpt',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='CourseOpt',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]

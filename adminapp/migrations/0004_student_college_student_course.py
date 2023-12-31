# Generated by Django 4.2.2 on 2023-06-21 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_college_course_remove_student_college_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.college'),
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.course'),
        ),
    ]

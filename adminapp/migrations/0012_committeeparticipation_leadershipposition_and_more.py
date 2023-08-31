# Generated by Django 4.2.2 on 2023-07-03 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0011_letstalk'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteeParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=300, null=True)),
                ('last_name', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=300, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('relevant_experience', models.TextField(blank=True, null=True)),
                ('skills_and_expertise', models.TextField(blank=True, null=True)),
                ('status_of_committee', models.CharField(default='waiting', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeadershipPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=300, null=True)),
                ('last_name', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=300, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('relevant_experience', models.TextField(blank=True, null=True)),
                ('leadership_philosipy', models.TextField(blank=True, null=True)),
                ('status_of_leadership', models.CharField(default='waiting', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Volunteering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=300, null=True)),
                ('last_name', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=300, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('relevant_experience', models.TextField(blank=True, null=True)),
                ('status_of_volunteering', models.CharField(default='waiting', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='LetsTalk',
        ),
    ]

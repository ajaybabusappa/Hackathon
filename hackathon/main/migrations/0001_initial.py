# Generated by Django 3.0.7 on 2020-10-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=100)),
                ('department_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('mailid', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('mailid', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
            ],
        ),
    ]

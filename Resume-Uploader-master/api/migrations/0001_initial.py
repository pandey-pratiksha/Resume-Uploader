# Generated by Django 4.0.5 on 2022-12-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('state', models.CharField(choices=[('bihar', 'bihar'), ('m.p', 'm.p'), ('u.p', 'u.p')], max_length=50)),
                ('loction', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('pimage', models.ImageField(blank=True, upload_to='static/pimages')),
                ('rdoc', models.FileField(blank=True, upload_to='static/rdocs')),
            ],
        ),
    ]

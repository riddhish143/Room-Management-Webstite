# Generated by Django 4.0.4 on 2022-06-07 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Block', models.CharField(choices=[('A-BLOCK', 'A-BLOCK'), ('B-BLOCK', 'B-BLOCK'), ('C-BLOCK', 'C-BLOCK'), ('D-BLOCK', 'D-BLOCK')], max_length=10)),
                ('Type', models.CharField(choices=[('class', 'classroom'), ('meet', 'meetingroom'), ('audit', 'auditorium')], max_length=20)),
                ('Roomno', models.IntegerField()),
                ('capacity', models.IntegerField(default='40')),
                ('Availability', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=20)),
            ],
        ),
    ]

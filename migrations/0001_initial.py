# Generated by Django 4.0.4 on 2022-06-07 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('block', models.CharField(choices=[('A-BLOCK', 'A-BLOCK'), ('B-BLOCK', 'B-BLOCK'), ('C-BLOCK', 'C-BLOCK'), ('D-BLOCK', 'D-BLOCK')], default='A-BLOCK', max_length=10)),
                ('number', models.IntegerField(default=40)),
                ('purpose', models.TextField()),
                ('Desgination', models.CharField(choices=[('Teacher', 'Teacher'), ('student', 'student'), ('other', 'other')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

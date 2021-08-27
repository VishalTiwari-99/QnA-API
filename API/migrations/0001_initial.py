# Generated by Django 3.2.5 on 2021-08-27 10:46

import datetime
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
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2021, 8, 27), null=True)),
                ('question_english', models.TextField(null=True)),
                ('question_hindi', models.TextField(null=True)),
                ('option_one', models.TextField(null=True)),
                ('option_two', models.TextField(null=True)),
                ('option_three', models.TextField(null=True)),
                ('option_four', models.TextField(null=True)),
                ('correct_answer', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=10, null=True)),
                ('fresh', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2021, 8, 27), null=True)),
                ('time_slot', models.CharField(choices=[('Morning', 'M'), ('Evening', 'E')], max_length=10, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('question_list', models.ManyToManyField(to='API.Question')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTestAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(null=True)),
                ('assigned_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.testslot')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=10, null=True)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.question')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.usertestattempt')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-02 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('firstName', models.CharField(max_length=20)),
                ('bio', models.TextField(default='Write a bio!', max_length=1000)),
                ('hashPass', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('numQuestions', models.PositiveIntegerField(default=0)),
                ('numCorrect', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]

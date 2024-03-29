# Generated by Django 2.2.3 on 2019-07-30 22:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_program_speaker'),
    ]

    operations = [
        migrations.CreateModel(
            name='pastspeakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('talk', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=500)),
                ('Linkedin', models.TextField()),
                ('kaggle', models.TextField()),
                ('github', models.TextField()),
                ('slide', models.TextField()),
                ('Notebook', models.TextField()),
                ('code', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='sponsors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsorname', models.CharField(max_length=10)),
                ('sponsorlink', models.TextField()),
            ],
        ),
    ]

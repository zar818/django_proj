# Generated by Django 3.2.6 on 2021-12-07 10:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yougo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('abtract', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('researcher', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

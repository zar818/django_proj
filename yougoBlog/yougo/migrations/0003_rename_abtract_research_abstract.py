# Generated by Django 3.2.6 on 2021-12-07 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yougo', '0002_research'),
    ]

    operations = [
        migrations.RenameField(
            model_name='research',
            old_name='abtract',
            new_name='abstract',
        ),
    ]

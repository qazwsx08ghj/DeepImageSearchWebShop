# Generated by Django 3.2.9 on 2021-11-23 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Users', 'verbose_name_plural': 'Users'},
        ),
    ]

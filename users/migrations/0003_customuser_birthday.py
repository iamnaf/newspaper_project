# Generated by Django 3.2.6 on 2021-10-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(default='1995-09-19'),
            preserve_default=False,
        ),
    ]
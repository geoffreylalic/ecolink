# Generated by Django 3.2.15 on 2022-10-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_auto_20221010_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
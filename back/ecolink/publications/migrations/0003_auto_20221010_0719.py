# Generated by Django 3.2.15 on 2022-10-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_auto_20221001_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='photos',
        ),
        migrations.AddField(
            model_name='publication',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='ImagePublication',
        ),
    ]

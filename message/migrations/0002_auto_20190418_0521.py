# Generated by Django 2.1.7 on 2019-04-18 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(default='Hello from the other side', max_length=140),
        ),
    ]

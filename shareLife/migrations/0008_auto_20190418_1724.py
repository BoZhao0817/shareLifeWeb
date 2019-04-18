# Generated by Django 2.1.7 on 2019-04-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareLife', '0007_postdetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postdetail',
            name='address',
        ),
        migrations.RemoveField(
            model_name='postdetail',
            name='bathrooms',
        ),
        migrations.RemoveField(
            model_name='postdetail',
            name='bedrooms',
        ),
        migrations.RemoveField(
            model_name='postdetail',
            name='garage_size',
        ),
        migrations.RemoveField(
            model_name='postdetail',
            name='price',
        ),
        migrations.RemoveField(
            model_name='postdetail',
            name='property_size',
        ),
        migrations.RemoveField(
            model_name='postdetail',
            name='year_built',
        ),
        migrations.AddField(
            model_name='post',
            name='bathrooms',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='bedrooms',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='garage_size',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='property_size',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='post',
            name='year_built',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(max_length=500),
        ),
    ]
# Generated by Django 2.1.7 on 2019-03-28 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shareLife', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Chicago', max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shareLife.Location'),
        ),
    ]

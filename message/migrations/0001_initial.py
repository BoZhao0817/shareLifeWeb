# Generated by Django 2.1.7 on 2019-04-18 03:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('postId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Message_post', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='recv_chats', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='send_chats', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
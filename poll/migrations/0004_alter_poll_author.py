# Generated by Django 3.2.13 on 2022-08-17 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poll', '0003_alter_poll_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll_user', to='auth.user'),
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-29 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_priority'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0003_booking_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='treatment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_treatment', to='blog.post'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.2.13 on 2022-08-11 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.TextField(blank=True),
        ),
    ]
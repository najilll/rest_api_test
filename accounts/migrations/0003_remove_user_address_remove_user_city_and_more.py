# Generated by Django 5.0.4 on 2024-04-18 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_user_usertype"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="address",
        ),
        migrations.RemoveField(
            model_name="user",
            name="city",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone",
        ),
        migrations.RemoveField(
            model_name="user",
            name="postal_code",
        ),
    ]
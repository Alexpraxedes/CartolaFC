# Generated by Django 4.1.6 on 2023-02-05 18:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="player",
            old_name="action_type",
            new_name="position",
        ),
    ]

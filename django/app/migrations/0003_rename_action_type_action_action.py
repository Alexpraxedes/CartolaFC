# Generated by Django 4.1.6 on 2023-02-05 18:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_rename_action_type_player_position"),
    ]

    operations = [
        migrations.RenameField(
            model_name="action",
            old_name="action_type",
            new_name="action",
        ),
    ]

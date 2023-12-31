# Generated by Django 4.1.7 on 2023-05-18 08:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "authentication",
            "0002_users_created_at_users_created_by_users_deleted_at_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="access_token",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="users",
            name="flag",
            field=models.BooleanField(default=False),
        ),
    ]

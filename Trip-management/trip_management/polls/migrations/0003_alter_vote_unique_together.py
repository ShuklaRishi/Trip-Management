# Generated by Django 4.1.7 on 2023-04-27 11:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("polls", "0002_vote"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="vote",
            unique_together={("user", "choice")},
        ),
    ]

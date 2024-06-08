# Generated by Django 4.2.13 on 2024-06-04 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("outreach", "0019_alter_message_subject"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="message",
            name="type",
        ),
        migrations.AddField(
            model_name="message",
            name="campaign",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="outreach.campaign",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="message",
            name="sender",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

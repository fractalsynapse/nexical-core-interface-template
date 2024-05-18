# Generated by Django 4.2.5 on 2024-05-18 08:00

import app.utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="State",
            fields=[
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                ("name", models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name="Name")),
                ("value", app.utils.fields.DictionaryField(default=dict, verbose_name="Value")),
            ],
            options={
                "ordering": ["-created"],
                "abstract": False,
            },
        ),
    ]

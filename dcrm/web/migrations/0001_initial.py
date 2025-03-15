# Generated by Django 5.1.7 on 2025-03-15 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=40)),
                ("phone", models.CharField(max_length=15)),
                ("address", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=30)),
                ("province", models.CharField(max_length=30)),
                ("zipcode", models.CharField(max_length=10)),
            ],
        ),
    ]

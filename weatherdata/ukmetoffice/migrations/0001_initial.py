# Generated by Django 4.2.1 on 2023-05-28 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Month",
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
                ("name", models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name="Region",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Weather",
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
                ("tmax", models.FloatField()),
                ("tmin", models.FloatField()),
                ("tmean", models.FloatField()),
                ("sunshine", models.FloatField()),
                ("rainfall", models.FloatField()),
                ("raindays1mm", models.FloatField()),
                ("airfrost", models.FloatField()),
                (
                    "month",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ukmetoffice.month",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ukmetoffice.region",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 2.2.12 on 2020-05-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_auto_20200513_1021"),
    ]

    operations = [
        migrations.RemoveField(model_name="landingpage", name="f2",),
        migrations.RemoveField(model_name="landingpage", name="f3",),
        migrations.RemoveField(model_name="landingpage", name="f4",),
        migrations.RemoveField(model_name="landingpage", name="f5",),
        migrations.CreateModel(
            name="Mname",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("f1", models.BigIntegerField()),
                ("f2", models.BooleanField()),
                ("f3", models.DateTimeField(auto_now=True)),
                ("f4", models.URLField()),
                (
                    "f5",
                    models.ManyToManyField(
                        related_name="mname_f5", to="home.Landingpage"
                    ),
                ),
            ],
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-19 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="title",
            field=models.CharField(max_length=250),
        ),
    ]

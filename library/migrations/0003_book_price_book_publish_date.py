# Generated by Django 4.0.3 on 2022-03-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0002_book_colour"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="price",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="publish_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

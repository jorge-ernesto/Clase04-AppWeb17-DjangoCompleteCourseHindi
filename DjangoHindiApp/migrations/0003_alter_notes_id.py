# Generated by Django 4.2 on 2023-04-18 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoHindiApp', '0002_notes_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

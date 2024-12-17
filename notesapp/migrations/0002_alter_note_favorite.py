# Generated by Django 5.1.4 on 2024-12-16 19:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='favorite',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='notesapp.favorites'),
        ),
    ]
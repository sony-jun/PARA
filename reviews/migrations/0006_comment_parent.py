# Generated by Django 4.1.3 on 2022-11-17 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_delete_tagmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reviews.comment'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-31 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_post_title_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.post'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.4 on 2020-04-06 09:39

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=None, storage=django.core.files.storage.FileSystemStorage(location='assets/images/uploads'), upload_to=''),
            preserve_default=False,
        ),
    ]

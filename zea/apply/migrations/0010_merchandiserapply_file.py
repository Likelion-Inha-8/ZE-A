# Generated by Django 3.1.1 on 2020-09-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0009_merchandiserapply_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandiserapply',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]

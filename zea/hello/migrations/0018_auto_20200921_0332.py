# Generated by Django 3.1.1 on 2020-09-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0017_auto_20200921_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuapply',
            name='account',
            field=models.CharField(max_length=200),
        ),
    ]
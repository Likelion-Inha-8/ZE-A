# Generated by Django 3.1.1 on 2020-09-22 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0019_stuapply_namestore'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuapply',
            name='phonenum',
            field=models.CharField(default='example', max_length=200),
            preserve_default=False,
        ),
    ]
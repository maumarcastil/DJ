# Generated by Django 3.1.2 on 2020-10-23 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20201021_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='valid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='valid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]

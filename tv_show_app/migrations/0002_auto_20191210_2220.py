# Generated by Django 2.2 on 2019-12-10 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(),
        ),
    ]
# Generated by Django 3.2 on 2021-07-20 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_alter_category_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
# Generated by Django 3.2 on 2021-07-19 21:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0003_alter_category_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='admin',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
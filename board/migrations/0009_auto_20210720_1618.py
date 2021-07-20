# Generated by Django 3.2 on 2021-07-20 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_alter_comment_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_created']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='body',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.AddField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='board.comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
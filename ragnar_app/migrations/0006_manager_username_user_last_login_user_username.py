# Generated by Django 5.1.1 on 2024-10-19 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ragnar_app', '0005_manager_deleted_at_manager_restored_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='username',
            field=models.CharField(default='username', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='username', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]

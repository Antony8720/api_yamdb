# Generated by Django 2.2.16 on 2022-08-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.TextField(blank=True, null=True, verbose_name='Код подтверждения'),
        ),
    ]
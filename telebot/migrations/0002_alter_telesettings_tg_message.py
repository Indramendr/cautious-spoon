# Generated by Django 3.2 on 2021-06-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telebot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telesettings',
            name='tg_message',
            field=models.TextField(max_length=200, verbose_name='Текст сообщение'),
        ),
    ]
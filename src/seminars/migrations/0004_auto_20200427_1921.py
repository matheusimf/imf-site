# Generated by Django 2.2 on 2020-04-27 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminars', '0003_auto_20200427_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seminar',
            old_name='inscription_link',
            new_name='payment_link',
        ),
    ]

# Generated by Django 3.2.12 on 2022-04-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20211104_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_format',
            field=models.CharField(blank=True, default='MMM-DD-YYYY - HH:mm', max_length=30),
        ),
    ]

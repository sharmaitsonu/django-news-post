# Generated by Django 3.0.8 on 2020-08-31 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0004_auto_20200831_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_title',
            field=models.CharField(max_length=300),
        ),
    ]
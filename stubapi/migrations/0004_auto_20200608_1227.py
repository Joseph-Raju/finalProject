# Generated by Django 2.2.10 on 2020-06-08 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stubapi', '0003_auto_20200608_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebook',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

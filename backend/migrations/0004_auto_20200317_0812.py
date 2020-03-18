# Generated by Django 2.2.10 on 2020-03-17 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0003_data_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='fields',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='data',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.CreateModel(
            name='CustomTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('structure', jsonfield.fields.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 3.0.7 on 2020-09-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 3.1.7 on 2021-09-23 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karte', '0015_auto_20210922_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='autorin',
            name='schools',
            field=models.ManyToManyField(blank=True, to='karte.Schule'),
        ),
    ]
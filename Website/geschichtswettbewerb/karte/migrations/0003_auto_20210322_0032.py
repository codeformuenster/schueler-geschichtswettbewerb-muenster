# Generated by Django 3.1.7 on 2021-03-22 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karte', '0002_auto_20210322_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokument',
            name='dokument',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
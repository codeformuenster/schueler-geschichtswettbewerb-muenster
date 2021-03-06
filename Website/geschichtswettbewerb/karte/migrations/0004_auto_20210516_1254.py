# Generated by Django 3.1.7 on 2021-05-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karte', '0003_auto_20210322_0032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auszeichnung',
            options={'verbose_name_plural': 'Auszeichnungen'},
        ),
        migrations.AlterModelOptions(
            name='auszeichnungeinreichung',
            options={'verbose_name_plural': 'Auszeichnungen Einreichungen'},
        ),
        migrations.AlterModelOptions(
            name='autorin',
            options={'verbose_name_plural': 'Autorinnen'},
        ),
        migrations.AlterModelOptions(
            name='autorinschule',
            options={'verbose_name_plural': 'Autorinnen Schulen'},
        ),
        migrations.AlterModelOptions(
            name='beitrag',
            options={'ordering': ('signatur',), 'verbose_name_plural': 'Beiträge'},
        ),
        migrations.AlterModelOptions(
            name='beitragsart',
            options={'verbose_name_plural': 'Beitragsarten'},
        ),
        migrations.AlterModelOptions(
            name='beitragwettbewerb',
            options={'verbose_name_plural': 'Beiträge Wettbewerbe'},
        ),
        migrations.AlterModelOptions(
            name='dokument',
            options={'verbose_name_plural': 'Dokumente'},
        ),
        migrations.AlterModelOptions(
            name='dokumenttyp',
            options={'verbose_name': 'Dokument Type', 'verbose_name_plural': 'Dokument Typen'},
        ),
        migrations.AlterModelOptions(
            name='historischeregion',
            options={'verbose_name': 'Historische Region', 'verbose_name_plural': 'Historische Regionen'},
        ),
        migrations.AlterModelOptions(
            name='historischerort',
            options={'verbose_name': 'Historischer Ort', 'verbose_name_plural': 'Historische Orte'},
        ),
        migrations.AlterModelOptions(
            name='institution',
            options={'verbose_name_plural': 'institutionen'},
        ),
        migrations.AlterModelOptions(
            name='materialgrundlage',
            options={'verbose_name_plural': 'Materialgrundlagen'},
        ),
        migrations.AlterModelOptions(
            name='ort',
            options={'verbose_name_plural': 'Orte'},
        ),
        migrations.AlterModelOptions(
            name='persoenlichkeit',
            options={'verbose_name': 'Persönlichkeit', 'verbose_name_plural': 'Persönlichkeiten'},
        ),
        migrations.AlterModelOptions(
            name='schulart',
            options={'verbose_name_plural': 'Schularten'},
        ),
        migrations.AlterModelOptions(
            name='schule',
            options={'verbose_name_plural': 'Schulen'},
        ),
        migrations.AlterModelOptions(
            name='schuleschulart',
            options={'verbose_name_plural': 'Schulen Schularten'},
        ),
        migrations.AlterModelOptions(
            name='tutor',
            options={'verbose_name': 'Tutorin', 'verbose_name_plural': 'Tutorinnen'},
        ),
        migrations.AlterModelOptions(
            name='wettbewerb',
            options={'verbose_name_plural': 'Wettbewerbe'},
        ),
        migrations.AlterField(
            model_name='beitrag',
            name='zeitraumBis',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='beitrag',
            name='zeitraumVon',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-28 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_dateandlocation_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dateandlocation',
            name='latitude',
            field=models.DecimalField(decimal_places=15, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='dateandlocation',
            name='longitude',
            field=models.DecimalField(decimal_places=15, max_digits=20, null=True),
        ),
    ]
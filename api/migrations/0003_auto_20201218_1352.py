# Generated by Django 3.1.3 on 2020-12-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201218_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='reviewScore',
            field=models.FloatField(null=True, verbose_name='Nota'),
        ),
    ]

# Generated by Django 4.2.5 on 2024-01-29 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_energyinsight_intensity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energyinsight',
            name='likelihood',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='energyinsight',
            name='relevance',
            field=models.IntegerField(null=True),
        ),
    ]
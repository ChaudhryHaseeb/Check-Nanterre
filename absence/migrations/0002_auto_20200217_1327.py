# Generated by Django 3.0.3 on 2020-02-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absence', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absence',
            name='justification',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='absence',
            name='retard',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
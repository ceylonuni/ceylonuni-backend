# Generated by Django 4.0.3 on 2022-04-03 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CeylonuniApp', '0003_delete_accounts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='address',
        ),
        migrations.AddField(
            model_name='students',
            name='address1',
            field=models.CharField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='address2',
            field=models.CharField(max_length=350, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='city',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='state',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='zip',
            field=models.IntegerField(null=True),
        ),
    ]

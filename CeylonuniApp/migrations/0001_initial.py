# Generated by Django 4.0.3 on 2022-04-03 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=350)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=350)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=350)),
                ('lastName', models.CharField(max_length=350)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('mobile', models.IntegerField()),
                ('isVerified', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=True)),
                ('address1', models.CharField(max_length=350)),
                ('address2', models.CharField(max_length=350, null=True)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('zip', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('deletedAt', models.DateTimeField(default=None, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CeylonuniApp.courses')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CeylonuniApp.universities'),
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-18 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('introduction', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('employee', models.ManyToManyField(to='intermgmt.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='sponsor',
            field=models.ManyToManyField(to='intermgmt.Sponsor'),
        ),
        migrations.AddField(
            model_name='event',
            name='vendor',
            field=models.ManyToManyField(to='intermgmt.Vendor'),
        ),
        migrations.AddField(
            model_name='event',
            name='volunteer',
            field=models.ManyToManyField(to='intermgmt.Volunteer'),
        ),
    ]

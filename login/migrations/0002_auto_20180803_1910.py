# Generated by Django 2.0.2 on 2018-08-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Job_number',
            field=models.CharField(default='工号', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(default='部门', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(default='电话', max_length=22),
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(default='职位', max_length=30),
        ),
    ]

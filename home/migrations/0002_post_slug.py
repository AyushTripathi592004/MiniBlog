# Generated by Django 3.1.3 on 2020-11-15 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=800),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-09 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orpodanieissues',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='orpodanieissues',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='orpodanieissues',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='statusName',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], max_length=20),
        ),
    ]
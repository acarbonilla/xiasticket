# Generated by Django 4.2.2 on 2023-06-26 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_alter_advisory_created_alter_advisory_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incticket',
            name='created',
            field=models.DateField(),
        ),
    ]

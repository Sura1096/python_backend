# Generated by Django 5.1 on 2024-09-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breed_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='exercise_needs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='breed',
            name='friendliness',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='breed',
            name='shedding_amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='breed',
            name='trainability',
            field=models.IntegerField(),
        ),
    ]

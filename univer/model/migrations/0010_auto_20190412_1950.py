# Generated by Django 2.0.13 on 2019-04-12 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0009_auto_20190412_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.IntegerField(choices=[(1, 'Beginner'), (2, 'Mixed'), (3, 'Hard')], default=None, null=True),
        ),
    ]
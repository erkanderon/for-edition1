# Generated by Django 2.0.13 on 2019-03-19 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_auto_20190318_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=30)),
                ('teacher_surname', models.CharField(max_length=30)),
                ('teacher_description', models.TextField(blank=True, null=True)),
                ('teacher_image', models.CharField(max_length=150)),
                ('teacher_popularity', models.IntegerField(choices=[(1, 'Half Star'), (2, 'One Star'), (3, 'One and Half Star'), (4, 'Two Star'), (5, 'Two and Half Star'), (6, 'Three Star'), (7, 'Three and Half Star'), (8, 'Four Star'), (9, 'Four and Half Star'), (10, 'Five Star')])),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=50)),
                ('university_description', models.CharField(max_length=50)),
                ('university_logo', models.CharField(max_length=150)),
                ('university_popularity', models.IntegerField(choices=[(1, 'Half Star'), (2, 'One Star'), (3, 'One and Half Star'), (4, 'Two Star'), (5, 'Two and Half Star'), (6, 'Three Star'), (7, 'Three and Half Star'), (8, 'Four Star'), (9, 'Four and Half Star'), (10, 'Five Star')])),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_logo',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_status',
            field=models.IntegerField(choices=[(1, 'Show'), (2, 'Hide')]),
        ),
        migrations.AlterField(
            model_name='course',
            name='price_currency',
            field=models.CharField(choices=[('$', 'Dolar'), ('€', 'Euro'), ('TL', 'Türk Lirası')], max_length=5),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_university',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='model.University'),
        ),
        migrations.AddField(
            model_name='course',
            name='course_teacher',
            field=models.ManyToManyField(blank=True, to='model.Teacher'),
        ),
    ]
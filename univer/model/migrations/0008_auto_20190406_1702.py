# Generated by Django 2.0.13 on 2019-04-06 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0007_course_belongs_to'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_logo',
            new_name='logo',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_owner',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_teacher',
            new_name='teacher',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher_popularity',
            new_name='popularity',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher_surname',
            new_name='surname',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='teacher_university',
            new_name='university',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='university_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='university_logo',
            new_name='logo',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='university_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='university',
            old_name='university_popularity',
            new_name='popularity',
        ),
    ]

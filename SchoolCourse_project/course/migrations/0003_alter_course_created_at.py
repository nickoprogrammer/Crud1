# Generated by Django 5.0.6 on 2024-06-10 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_delete_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
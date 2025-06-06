# Generated by Django 5.2.1 on 2025-06-04 15:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_techfault_assigned_to_alter_techfault_student_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ec',
            name='student',
            field=models.ForeignKey(limit_choices_to={'user_type': 'student'}, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_tickets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='techfault',
            name='student',
            field=models.ForeignKey(limit_choices_to={'user_type': 'student'}, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.2.19 on 2023-05-30 12:15

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_follow_no_self_follow'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('user', django.db.models.expressions.F('author')), _negated=True), name='no_self_follow'),
        ),
    ]

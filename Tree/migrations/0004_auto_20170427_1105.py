# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tree', '0003_remove_textquestion_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='Tree.Node'),
        ),
    ]
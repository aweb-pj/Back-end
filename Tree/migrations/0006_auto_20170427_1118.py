# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tree', '0005_auto_20170427_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicequestion',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_questions', to='Tree.Quiz'),
        ),
        migrations.AlterField(
            model_name='textquestion',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_questions', to='Tree.Quiz'),
        ),
    ]

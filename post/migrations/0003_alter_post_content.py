# Generated by Django 3.2.14 on 2022-07-19 06:02

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20220718_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_quill.fields.QuillField(),
        ),
    ]

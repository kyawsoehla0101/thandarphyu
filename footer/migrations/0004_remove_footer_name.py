# Generated by Django 3.2.14 on 2022-07-18 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0003_footer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='name',
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-03 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200603_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='level',
            new_name='mptt_level',
        ),
    ]
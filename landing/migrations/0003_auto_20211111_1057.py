# Generated by Django 3.2.8 on 2021-11-11 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_rename_users_customers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customers',
            new_name='Customer',
        ),
        migrations.RenameModel(
            old_name='Payments',
            new_name='Payment',
        ),
    ]

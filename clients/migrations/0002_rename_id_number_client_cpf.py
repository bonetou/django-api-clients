# Generated by Django 3.2.3 on 2021-05-30 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='id_number',
            new_name='cpf',
        ),
    ]
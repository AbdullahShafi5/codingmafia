# Generated by Django 3.2.7 on 2021-09-07 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_sbscrb_email_subscribeemail_sbscrb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribeemail',
            old_name='sbscrb',
            new_name='sbscrb_email',
        ),
    ]

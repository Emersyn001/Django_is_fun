# Generated by Django 5.1.3 on 2024-11-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phones'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]

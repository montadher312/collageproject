# Generated by Django 4.2.7 on 2023-11-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_cyber_security_11request_delete_lecture1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='computerengineering_1request',
            name='chair',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default='Pending', max_length=10, null=True),
        ),
    ]

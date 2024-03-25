# Generated by Django 4.2.7 on 2023-11-25 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_computerengineering_1request_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computerengineering_2request',
            name='status',
        ),
        migrations.CreateModel(
            name='ComputerEngineering_22Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10, null=True)),
                ('name', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.computerengineering_2request')),
            ],
        ),
    ]

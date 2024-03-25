# Generated by Django 4.2.7 on 2023-11-25 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_delete_cyber_security_11request'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cyber_security_11Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Lecture1',
        ),
        migrations.RemoveField(
            model_name='computerengineering_1request',
            name='lecture_name',
        ),
        migrations.RemoveField(
            model_name='computerengineering_2request',
            name='lecture_name',
        ),
        migrations.RemoveField(
            model_name='computerengineering_3request',
            name='lecture_name',
        ),
        migrations.RemoveField(
            model_name='computerengineering_4request',
            name='lecture_name',
        ),
        migrations.RemoveField(
            model_name='cyber_security_1request',
            name='lecture_name',
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
        migrations.AddField(
            model_name='cyber_security_11request',
            name='name',
            field=models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.cyber_security_1request'),
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateField()),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]

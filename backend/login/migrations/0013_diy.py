# Generated by Django 3.2.7 on 2025-03-28 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20250328_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='DIY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video', models.FileField(upload_to='video/')),
            ],
            options={
                'db_table': 'diy',
            },
        ),
    ]

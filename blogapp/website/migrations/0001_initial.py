# Generated by Django 5.1 on 2024-09-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelMenuLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=2048)),
                ('new_tab', models.BooleanField(default=False)),
            ],
        ),
    ]

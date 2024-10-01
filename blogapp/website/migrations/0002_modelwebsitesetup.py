# Generated by Django 5.1 on 2024-10-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelWebsiteSetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('description', models.CharField(max_length=255)),
                ('show_header', models.BooleanField(default=False)),
                ('show_search', models.BooleanField(default=False)),
                ('show_menu', models.BooleanField(default=False)),
                ('show_description', models.BooleanField(default=False)),
                ('show_pagination', models.BooleanField(default=False)),
                ('show_footer', models.BooleanField(default=False)),
            ],
        ),
    ]

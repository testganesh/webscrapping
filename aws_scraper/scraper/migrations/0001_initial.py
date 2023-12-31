# Generated by Django 4.2.2 on 2023-06-20 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=255)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourceType', models.CharField(max_length=255)),
                ('arn', models.CharField(max_length=255)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='scraper.service')),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditionKey', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('typ', models.CharField(max_length=255)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conditions', to='scraper.service')),
            ],
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
                ('access', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='scraper.service')),
            ],
        ),
    ]

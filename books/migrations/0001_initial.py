# Generated by Django 3.2.9 on 2021-11-22 23:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id_book', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('realease_year', models.IntegerField()),
                ('state', models.CharField(max_length=50)),
                ('pages', models.IntegerField()),
                ('publishing_company', models.CharField(max_length=255)),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

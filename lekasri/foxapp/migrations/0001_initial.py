# Generated by Django 5.0.2 on 2024-02-28 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='librarybooks_DB',
            fields=[
                ('bookno', models.IntegerField(primary_key='bookno', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=20)),
                ('edition', models.CharField(max_length=5)),
            ],
        ),
    ]

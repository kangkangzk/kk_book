# Generated by Django 4.2.14 on 2024-11-24 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sql',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('brief_title', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# Generated by Django 2.2.4 on 2021-05-15 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notas',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

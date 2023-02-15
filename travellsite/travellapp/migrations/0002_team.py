# Generated by Django 4.1.5 on 2023-01-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=250)),
                ('des', models.TextField()),
            ],
        ),
    ]
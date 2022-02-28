# Generated by Django 3.2.6 on 2021-08-27 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0003_auto_20210827_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Table',
            },
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='dishes/%Y/%m/%d')),
                ('ingredients', models.TextField()),
                ('details', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('discounted_price', models.FloatField(blank=True)),
                ('is_available', models.BooleanField(default=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Dish Table',
            },
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Contact Table'},
        ),
    ]

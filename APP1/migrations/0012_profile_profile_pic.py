# Generated by Django 3.2.6 on 2021-09-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0011_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/%Y/%m/%d'),
        ),
    ]

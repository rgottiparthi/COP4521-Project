# Generated by Django 4.1.7 on 2023-04-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_item_image_restaurant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='NumRatings',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='NumRatings',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 2.2.1 on 2019-05-20 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopeeSite', '0002_auto_20190518_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopinfo',
            old_name='product1id',
            new_name='product_id',
        ),
        migrations.RemoveField(
            model_name='shopinfo',
            name='product2id',
        ),
        migrations.RemoveField(
            model_name='shopinfo',
            name='product3id',
        ),
    ]

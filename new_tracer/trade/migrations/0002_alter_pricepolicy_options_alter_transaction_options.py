# Generated by Django 4.2.7 on 2023-12-23 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricepolicy',
            options={'verbose_name': '价格策略', 'verbose_name_plural': '价格策略'},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'verbose_name': '交易记录', 'verbose_name_plural': '交易记录'},
        ),
    ]

# Generated by Django 2.1.2 on 2018-12-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20181218_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='sample_6',
            new_name='do_check',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_7',
        ),
        migrations.AddField(
            model_name='item',
            name='do_date',
            field=models.DateField(blank=True, null=True, verbose_name='する日'),
        ),
    ]
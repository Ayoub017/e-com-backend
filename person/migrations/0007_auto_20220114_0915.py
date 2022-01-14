# Generated by Django 3.2.8 on 2022-01-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0006_auto_20220114_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='id_cmd',
        ),
        migrations.AddField(
            model_name='commande',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(max_length=60, null=True),
        ),
    ]
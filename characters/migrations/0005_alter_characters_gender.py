# Generated by Django 3.2.3 on 2021-05-26 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_alter_characters_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='gender',
            field=models.CharField(choices=[('', '性別を選んでください'), ('unknown', 'unknown'), ('man', 'man'), ('woman', 'woman')], max_length=7, verbose_name='性別'),
        ),
    ]

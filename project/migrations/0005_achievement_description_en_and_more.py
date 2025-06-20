# Generated by Django 5.2.1 on 2025-05-24 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_achievement_image_alter_achievement_image_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='description_ha',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='title_ha',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]

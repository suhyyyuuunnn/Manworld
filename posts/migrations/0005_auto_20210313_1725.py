# Generated by Django 3.1.7 on 2021-03-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210313_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../Manworld/static/img/header/1', upload_to='posts/img', verbose_name='썸네일 이미지'),
        ),
    ]

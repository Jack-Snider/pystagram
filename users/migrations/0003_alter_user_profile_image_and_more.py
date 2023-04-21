# Generated by Django 4.2 on 2023-04-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_profile_image_user_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='users/profile', verbose_name='프로필 이미지'),
        ),
        migrations.AlterField(
            model_name='user',
            name='short_description',
            field=models.TextField(blank='True', verbose_name='소개글'),
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(default='default_profile_pic.png', upload_to='media-files/'),
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_category_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='img/Lion_waiting_in_Nambia.jpg', upload_to='img/'),
        ),
    ]

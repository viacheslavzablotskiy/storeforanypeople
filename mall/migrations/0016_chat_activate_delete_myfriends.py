# Generated by Django 4.1.7 on 2023-03-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0015_myfriends_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='activate',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='MyFriends',
        ),
    ]

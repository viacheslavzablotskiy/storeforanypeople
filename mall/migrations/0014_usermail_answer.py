# Generated by Django 4.1.7 on 2023-03-08 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0013_alter_balance_balance_alter_basket_total_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.TextField(max_length=120)),
                ('text', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(max_length=120)),
                ('activate', models.BooleanField(default=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mall.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

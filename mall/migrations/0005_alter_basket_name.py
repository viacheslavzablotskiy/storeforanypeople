# Generated by Django 4.1.7 on 2023-03-02 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0004_basket_listproduct_name_review_product_basket_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='name',
            field=models.ManyToManyField(related_name='pizza', related_query_name='pizza', to='mall.product'),
        ),
    ]

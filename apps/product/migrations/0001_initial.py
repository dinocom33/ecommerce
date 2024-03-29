# Generated by Django 5.0 on 2024-01-04 14:53

import apps.product.fields
import autoslug.fields
import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='product_name', unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('is_digital', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='product_name', unique=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('sku', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('order', apps.product.fields.OrderField(blank=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_line', to='product.product')),
            ],
        ),
    ]

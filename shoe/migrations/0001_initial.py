# Generated by Django 4.1.5 on 2023-04-13 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BRAND_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BRAND_NAME', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CATEGORY_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATEGORY_NAME', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='CONTACT_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MESSAGE', models.CharField(max_length=300)),
                ('FULL_NAME', models.CharField(default='', max_length=300)),
                ('EMAIL_ID', models.EmailField(max_length=254)),
                ('PHONE_NO', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LOGIN_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EMAIL_ID', models.EmailField(max_length=254)),
                ('PHONE_NO', models.IntegerField()),
                ('PASSWORD', models.CharField(max_length=300)),
                ('DP', models.ImageField(upload_to='photos')),
                ('ROLE', models.IntegerField(choices=[(0, 'ADMIN'), (1, 'USER')])),
                ('STATUS', models.IntegerField(choices=[(0, 'Active'), (1, 'Inactive')])),
                ('NAME', models.CharField(max_length=300)),
                ('DOB', models.DateTimeField()),
                ('ADDRESS', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SHOES_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SIZE', models.IntegerField()),
                ('PRICE', models.IntegerField(default=100)),
                ('COLOR', models.CharField(max_length=300)),
                ('TYPE', models.CharField(max_length=300)),
                ('NAME', models.CharField(max_length=300)),
                ('SHOE_PHOTO', models.ImageField(upload_to='photos')),
                ('BRAND_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.brand_table')),
                ('CATEGORY_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.category_table')),
            ],
        ),
        migrations.CreateModel(
            name='STOCK_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COMMENT', models.CharField(max_length=300)),
                ('BRAND_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.brand_table')),
                ('CATEGORY_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.category_table')),
                ('SHOES_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.shoes_table')),
            ],
        ),
        migrations.CreateModel(
            name='ORDER_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TOTAL_AMOUNT', models.IntegerField(default=0)),
                ('ADDRESS', models.CharField(max_length=500)),
                ('DATETIME', models.DateTimeField(auto_now=True)),
                ('PAYMENT_STATUS', models.CharField(default='', max_length=300)),
                ('ORDER_STATUS', models.CharField(default='', max_length=300)),
                ('L_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='FEEDBACK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RATINGS', models.CharField(max_length=300)),
                ('COMMENT', models.CharField(default='', max_length=300)),
                ('L_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.login_table')),
            ],
        ),
        migrations.CreateModel(
            name='CART_TABLE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SHOES_NAME', models.CharField(max_length=300)),
                ('DATE', models.DateTimeField(auto_now=True)),
                ('PRICE', models.IntegerField(default=100)),
                ('QUANTITY', models.IntegerField()),
                ('FINAL_PRICE', models.IntegerField(default=160)),
                ('ORDER_ID', models.IntegerField(default=0)),
                ('ORDER_STATUS', models.IntegerField(default=0)),
                ('BRAND_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.brand_table')),
                ('CATEGORY_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.category_table')),
                ('L_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.login_table')),
                ('SHOES_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shoe.shoes_table')),
            ],
        ),
    ]

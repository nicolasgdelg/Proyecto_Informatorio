# Generated by Django 3.2.9 on 2021-12-20 03:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'categorias',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image_header', models.ImageField(upload_to='posts/photos')),
                ('post', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('url', models.SlugField(max_length=255, unique=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('categories', models.ManyToManyField(to='blogs.Category')),
            ],
            options={
                'db_table': 'posteos',
                'ordering': ('title',),
            },
        ),
    ]

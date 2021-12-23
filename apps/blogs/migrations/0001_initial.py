# Generated by Django 3.2.9 on 2021-12-23 05:20

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image_header', models.ImageField(upload_to='posts/photos')),
                ('post', django_quill.fields.QuillField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_draft', models.BooleanField(default=True)),
                ('url', models.SlugField(max_length=255, unique=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('categories', models.ManyToManyField(to='categories.Category')),
            ],
            options={
                'db_table': 'posteos',
                'ordering': ('title',),
            },
        ),
    ]

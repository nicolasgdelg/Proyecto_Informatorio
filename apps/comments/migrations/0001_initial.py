# Generated by Django 3.2.9 on 2021-12-19 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=5000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blogs.post')),
            ],
        ),
    ]

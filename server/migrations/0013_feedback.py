# Generated by Django 5.1.4 on 2024-12-27 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0012_shopping'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=1000)),
                ('message', models.TextField()),
            ],
        ),
    ]

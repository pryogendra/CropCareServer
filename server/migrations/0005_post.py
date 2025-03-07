# Generated by Django 5.1.4 on 2024-12-09 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_alter_userprofile_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='posts/')),
                ('caption', models.CharField(max_length=255)),
                ('likes', models.IntegerField()),
                ('comments', models.IntegerField()),
                ('posted_ago', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='server.userprofile')),
            ],
        ),
    ]

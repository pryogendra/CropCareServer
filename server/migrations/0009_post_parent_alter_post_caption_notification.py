# Generated by Django 5.1.4 on 2024-12-24 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_alter_post_image_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='parent',
            field=models.CharField(blank=True, max_length=5555, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(max_length=9255),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=700, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='server.userprofile')),
            ],
        ),
    ]

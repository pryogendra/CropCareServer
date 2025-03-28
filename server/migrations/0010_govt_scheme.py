# Generated by Django 5.1.4 on 2024-12-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0009_post_parent_alter_post_caption_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Govt_Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=5000, null=True)),
                ('discription', models.TextField()),
                ('benefit', models.TextField()),
                ('eligibility', models.TextField()),
                ('document', models.TextField()),
                ('apply_process', models.TextField()),
                ('contact', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]

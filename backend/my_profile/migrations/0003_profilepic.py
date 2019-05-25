# Generated by Django 2.2.1 on 2019-05-23 22:38

import backend.common_helpers.update_filename
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_profile', '0002_auto_20190524_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=backend.common_helpers.update_filename.update_filename_with_username)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_profile.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
# Generated by Django 2.2.14 on 2020-07-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200720_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='test',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]

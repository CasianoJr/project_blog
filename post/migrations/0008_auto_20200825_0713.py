# Generated by Django 3.0.8 on 2020-08-24 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20200726_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='post.Category'),
        ),
    ]
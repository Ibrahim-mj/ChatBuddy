# Generated by Django 4.2.2 on 2023-07-27 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_comment_options_alter_tweet_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tag'),
        ),
    ]
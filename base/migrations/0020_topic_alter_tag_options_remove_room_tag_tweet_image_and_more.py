# Generated by Django 4.2.2 on 2023-07-28 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_remove_user_display_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': []},
        ),
        migrations.RemoveField(
            model_name='room',
            name='tag',
        ),
        migrations.AddField(
            model_name='tweet',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(),
        ),
        migrations.AddField(
            model_name='room',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.topic'),
        ),
    ]

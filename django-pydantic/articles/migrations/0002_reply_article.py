# Generated by Django 4.0.2 on 2022-02-24 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='articles.article'),
            preserve_default=False,
        ),
    ]
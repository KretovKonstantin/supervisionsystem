# Generated by Django 4.2.5 on 2024-07-01 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='ai_status',
            field=models.CharField(blank=True, choices=[('good', 'Хорошая'), ('needs_review', 'Требует проверки'), ('bad', 'Плохая')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='status',
            field=models.CharField(choices=[('good', 'Хорошая'), ('needs_review', 'Требует проверки'), ('bad', 'Плохая')], default='needs_review', max_length=15),
        ),
    ]

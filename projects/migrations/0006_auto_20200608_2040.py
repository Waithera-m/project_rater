# Generated by Django 3.0.7 on 2020-06-08 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200608_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]

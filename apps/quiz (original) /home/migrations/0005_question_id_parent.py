# Generated by Django 4.0.3 on 2022-04-22 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_subcategory_questiontype'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='id_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.questiontype'),
        ),
    ]

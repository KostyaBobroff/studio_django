# Generated by Django 2.0.4 on 2018-04-11 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0004_auto_20180412_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_color', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='material',
            old_name='title_material',
            new_name='name_material',
        ),
        migrations.RenameField(
            model_name='model',
            old_name='title_model',
            new_name='name_model',
        ),
    ]
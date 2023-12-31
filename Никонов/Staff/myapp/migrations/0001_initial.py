# Generated by Django 4.2.6 on 2023-12-13 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название услуги')),
                ('material', models.CharField(max_length=100, verbose_name='Имя сотрудника')),
                ('price', models.IntegerField(default=100, verbose_name='Цена')),
                ('kolvo', models.IntegerField(default=0, verbose_name='Время работы')),
            ],
            options={
                'verbose_name': 'Фотограф',
                'verbose_name_plural': 'Фотографы',
            },
        ),
    ]

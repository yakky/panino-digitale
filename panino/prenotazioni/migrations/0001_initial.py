# Generated by Django 2.0.3 on 2018-03-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Panino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='nome')),
                ('descrizione', models.TextField(verbose_name='descrizione')),
                ('prezzo', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='prezzo')),
            ],
            options={
                'verbose_name': 'panino',
                'verbose_name_plural': 'panini',
            },
        ),
    ]
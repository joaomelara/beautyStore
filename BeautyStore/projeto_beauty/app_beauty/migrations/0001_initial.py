# Generated by Django 5.0.6 on 2024-05-22 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id_produtobeleza', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.TextField(max_length=255)),
                ('marca', models.TextField(max_length=255)),
                ('valor', models.FloatField()),
                ('estoque', models.IntegerField()),
            ],
        ),
    ]
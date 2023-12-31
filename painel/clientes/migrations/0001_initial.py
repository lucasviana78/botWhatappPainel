# Generated by Django 4.2.5 on 2023-10-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=80)),
                ('email_painel', models.CharField(max_length=100)),
                ('situacao', models.CharField(choices=[(0, 'Ativo'), (1, 'Inativo')], max_length=1)),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_rename_valor_proposta_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposta',
            name='status',
            field=models.CharField(choices=[('0', 'Em Análise'), ('1', 'Aprovada'), ('2', 'Negada')], default='0', max_length=2),
        ),
    ]

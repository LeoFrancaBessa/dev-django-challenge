# Generated by Django 4.2.2 on 2023-06-17 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_propostacustomfield_remove_proposta_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposta',
            old_name='valor',
            new_name='value',
        ),
        migrations.AlterField(
            model_name='propostacustomfieldanswer',
            name='proposta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='crud.proposta'),
        ),
    ]
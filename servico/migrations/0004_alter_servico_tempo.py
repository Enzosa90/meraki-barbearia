# Generated by Django 5.0.4 on 2024-04-17 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("servico", "0003_alter_servico_imagem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servico",
            name="tempo",
            field=models.TimeField(verbose_name="Tempo de atendimento (em minutos)"),
        ),
    ]

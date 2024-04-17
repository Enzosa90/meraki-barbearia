# Generated by Django 5.0.4 on 2024-04-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("servico", "0004_alter_servico_tempo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servico",
            name="tempo",
            field=models.PositiveIntegerField(
                verbose_name="Tempo de atendimento (em minutos)"
            ),
        ),
    ]

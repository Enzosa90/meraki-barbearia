# Generated by Django 5.0.4 on 2024-04-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("servico", "0008_servico_imagem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Servicoo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "imagem",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="servicos/",
                        verbose_name="Imagem",
                    ),
                ),
                ("nome", models.CharField(max_length=255, verbose_name="Serviço")),
                ("descricao", models.TextField(verbose_name="Descrição")),
                (
                    "preco",
                    models.DecimalField(
                        decimal_places=2, max_digits=8, verbose_name="Preço"
                    ),
                ),
                (
                    "tempo",
                    models.IntegerField(
                        verbose_name="Tempo de atendimento (em minutos)"
                    ),
                ),
            ],
            options={
                "verbose_name": "Serviço",
                "verbose_name_plural": "Serviços",
            },
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0002_despesas'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesas',
            name='categoria',
            field=models.CharField(choices=[('Outras', 'Outras'), ('Alimentação', 'Alimentação'), ('Saúde', 'Saúde'), ('Moradia', 'Moradia'), ('Transporte', 'Transporte'), ('Educação', 'Educação'), ('Lazer', 'Lazer'), ('Imprevistos', 'Imprevistos')], default='Outras', max_length=20),
        ),
    ]

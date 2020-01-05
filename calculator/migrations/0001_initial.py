# Generated by Django 2.2.6 on 2019-12-16 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Equation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equation_text', models.CharField(max_length=200)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Answer')),
            ],
        ),
    ]
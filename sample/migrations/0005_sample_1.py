# Generated by Django 3.0.4 on 2020-04-24 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0004_sample_num_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.PositiveIntegerField()),
            ],
        ),
    ]

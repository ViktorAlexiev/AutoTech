# Generated by Django 4.2.13 on 2024-06-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='b_data',
            name='id',
            field=models.BigAutoField(default='0', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='c_data',
            name='id',
            field=models.BigAutoField(default='0', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='p_data',
            name='id',
            field=models.BigAutoField(default='0', primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='w_data',
            name='id',
            field=models.BigAutoField(default='0', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='b_data',
            name='RK',
            field=models.IntegerField(blank=True, db_column='RK'),
        ),
        migrations.AlterField(
            model_name='c_data',
            name='RK',
            field=models.IntegerField(blank=True, db_column='RK'),
        ),
        migrations.AlterField(
            model_name='p_data',
            name='RK',
            field=models.IntegerField(blank=True, db_column='RK'),
        ),
        migrations.AlterField(
            model_name='w_data',
            name='RK',
            field=models.IntegerField(blank=True, db_column='RK'),
        ),
    ]
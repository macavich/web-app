# Generated by Django 2.1.1 on 2018-10-10 00:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=100, unique=True)),
                ('cusip', models.CharField(max_length=9)),
                ('mktArea', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=3)),
                ('active_date', models.DateTimeField(default=datetime.date.today)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_date', models.DateField(default=datetime.date.today)),
                ('quantity', models.IntegerField(default=0)),
                ('strategy', models.CharField(max_length=200)),
                ('substrategy', models.CharField(max_length=200)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Manager', to_field='username')),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Instrument', to_field='symbol')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('trade_date', models.DateField(default=datetime.date.today)),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Instrument', to_field='symbol')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Question'),
        ),
    ]
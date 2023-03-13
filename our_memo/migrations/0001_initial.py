# Generated by Django 4.1.7 on 2023-03-07 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(verbose_name='creation date')),
            ],
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo_title', models.CharField(max_length=255)),
                ('memo_text', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(verbose_name='creation date')),
                ('accomplish', models.BooleanField(default=False)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='our_memo.block')),
            ],
        ),
    ]

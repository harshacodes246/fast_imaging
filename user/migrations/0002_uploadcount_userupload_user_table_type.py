# Generated by Django 4.0.3 on 2022-05-14 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadcount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usid', models.CharField(max_length=100)),
                ('count', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usid', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('upload', models.FileField(upload_to='userupload')),
                ('dt', models.DateField(auto_now=True)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user_table',
            name='type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_uploadcount_userupload_user_table_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='usermax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('userid', models.CharField(max_length=100)),
                ('usernameMax', models.CharField(max_length=100)),
            ],
        ),
    ]

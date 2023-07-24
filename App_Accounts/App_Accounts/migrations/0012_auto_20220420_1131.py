# Generated by Django 3.1.2 on 2022-04-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Accounts', '0011_profile_totaldonationcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='HLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(blank=True, choices=[('blood doner', 'Blood Doner')], max_length=20),
        ),
    ]

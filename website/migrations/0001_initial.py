# Generated by Django 3.0.5 on 2024-06-16 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('passwd', models.CharField(max_length=16)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]

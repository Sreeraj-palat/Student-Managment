# Generated by Django 4.1 on 2022-08-09 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_account_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('dob', models.DateTimeField()),
                ('parent_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student'),
        ),
    ]

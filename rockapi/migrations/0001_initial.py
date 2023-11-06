# Generated by Django 4.2.7 on 2023-11-06 17:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Rock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rocks', to='rockapi.type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

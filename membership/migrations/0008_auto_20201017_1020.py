# Generated by Django 3.1 on 2020-10-17 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0007_auto_20201017_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='subscription_id',
        ),
        migrations.AddField(
            model_name='payment',
            name='subscription',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='membership.subscription'),
        ),
    ]

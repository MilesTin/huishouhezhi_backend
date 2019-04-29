# Generated by Django 2.2 on 2019-04-27 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_user'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='openid',
        ),
        migrations.AddField(
            model_name='order',
            name='timedelta',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
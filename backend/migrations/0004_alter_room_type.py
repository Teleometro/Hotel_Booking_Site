# Generated by Django 4.1 on 2022-10-25 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_booking_check_out_alter_room_type_cardpayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='type',
            field=models.CharField(choices=[('single', 'single'), ('president', 'president'), ('family', 'family'), ('double', 'double')], max_length=50),
        ),
    ]
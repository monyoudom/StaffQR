# Generated by Django 2.0.6 on 2018-07-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=255)),
                ('staff_id', models.CharField(max_length=255)),
                ('staff_position', models.CharField(max_length=255)),
                ('staff_department', models.CharField(max_length=255)),
                ('qrcode', models.ImageField(blank=True, null=True, upload_to='qrcode')),
            ],
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0011_rename_meeting_id_meeting_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingfile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-15 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lps', '0002_alter_freeconsultationmodel_mobilenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='freeconsultationmodel',
            name='email',
            field=models.EmailField(default='abc@somemail.com', max_length=254),
        ),
    ]

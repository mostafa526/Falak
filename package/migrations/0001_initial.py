# Generated by Django 4.0.5 on 2022-07-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='packages',
            fields=[
                ('name_pack', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='نوع الباقة')),
                ('package_duration', models.PositiveIntegerField(verbose_name='مدة الباقة')),
                ('price', models.FloatField(verbose_name='سعر الباقة')),
                ('describtion', models.TextField(blank=True, null=True, verbose_name='وصف الباقة')),
            ],
            options={
                'verbose_name': 'الباقات',
                'verbose_name_plural': 'الباقات',
            },
        ),
    ]
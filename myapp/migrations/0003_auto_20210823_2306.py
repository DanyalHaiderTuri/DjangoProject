# Generated by Django 3.2.6 on 2021-08-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.IntegerField(db_column='Emp_ID', primary_key=True, serialize=False)),
                ('emp_name', models.CharField(db_column='Emp_Name', max_length=20)),
                ('social_media', models.CharField(blank=True, db_column='Social_Media', max_length=30, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=220, null=True)),
                ('deignation', models.CharField(blank=True, db_column='Deignation', max_length=40, null=True)),
                ('seniority', models.CharField(blank=True, db_column='Seniority', max_length=20, null=True)),
                ('joining_date', models.DateField(blank=True, db_column='Joining_Date', null=True)),
                ('pay_scale', models.IntegerField(blank=True, db_column='Pay_Scale', null=True)),
                ('salary', models.IntegerField(blank=True, db_column='Salary', null=True)),
                ('allowed_holidays', models.IntegerField(blank=True, db_column='Allowed_holidays', null=True)),
                ('availed_holidays', models.IntegerField(blank=True, db_column='Availed_holidays', null=True)),
            ],
            options={
                'db_table': 'EMPLOYEE',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Feature',
        ),
    ]
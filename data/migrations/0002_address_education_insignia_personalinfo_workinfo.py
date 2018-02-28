# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_regis', models.CharField(max_length=10)),
                ('village_no_regis', models.IntegerField(default=0)),
                ('village_name_regis', models.CharField(max_length=40)),
                ('lane_regis', models.CharField(max_length=40)),
                ('road_regis', models.CharField(max_length=70)),
                ('sub_district_regis', models.CharField(max_length=70)),
                ('district_regis', models.CharField(max_length=70)),
                ('province_regis', models.CharField(max_length=70)),
                ('postal_code_regis', models.IntegerField(default=0)),
                ('smartphone_number_regis', models.CharField(max_length=20)),
                ('phone_number_regis', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=10)),
                ('village_no', models.IntegerField(default=0)),
                ('village_name', models.CharField(max_length=40)),
                ('lane', models.CharField(max_length=40)),
                ('road', models.CharField(max_length=70)),
                ('sub_district', models.CharField(max_length=70)),
                ('district', models.CharField(max_length=70)),
                ('province', models.CharField(max_length=70)),
                ('postal_code', models.IntegerField(default=0)),
                ('smartphone_number', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym_bachelor', models.CharField(max_length=10)),
                ('major_field_bachelor', models.CharField(max_length=40)),
                ('minor_field_bachelor', models.CharField(max_length=40)),
                ('start_year_bachelor', models.DateField(verbose_name='date published')),
                ('end_year_bachelor', models.DateField(verbose_name='date published')),
                ('acronym_master', models.CharField(max_length=10)),
                ('major_field_master', models.CharField(max_length=40)),
                ('minor_field_master', models.CharField(max_length=40)),
                ('start_year_master', models.DateField(verbose_name='date published')),
                ('end_year_master', models.DateField(verbose_name='date published')),
                ('acronym_phD', models.CharField(max_length=10)),
                ('major_field_phD', models.CharField(max_length=40)),
                ('minor_field_phD', models.CharField(max_length=40)),
                ('start_year_phD', models.DateField(verbose_name='date published')),
                ('end_year_phD', models.DateField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Insignia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class1', models.CharField(max_length=60)),
                ('date1', models.DateField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('MR', 'Mr.'), ('MRS', 'Mrs.'), ('MISS', 'Miss.')], max_length=6)),
                ('firstname_thai', models.CharField(max_length=30)),
                ('lastname_thai', models.CharField(max_length=30)),
                ('firstname_eng', models.CharField(max_length=30)),
                ('lastname_eng', models.CharField(max_length=30)),
                ('card_number', models.CharField(max_length=20)),
                ('religion', models.CharField(max_length=20)),
                ('blood_type', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')], max_length=6)),
                ('birth_date', models.DateField(verbose_name='date published')),
                ('email', models.EmailField(max_length=60)),
                ('status', models.CharField(choices=[('MR', 'Married'), ('SN', 'Single'), ('DV', 'Divorce'), ('WD', 'Widow')], max_length=10)),
                ('domicile_province', models.CharField(max_length=30)),
                ('firstname_spouse_thai', models.CharField(max_length=30)),
                ('lastname_spouse_thai', models.CharField(max_length=30)),
                ('firstname_spouse_eng', models.CharField(max_length=30)),
                ('lastname_spouse_eng', models.CharField(max_length=30)),
                ('firstname_father_thai', models.CharField(max_length=30)),
                ('lastname_father_thai', models.CharField(max_length=30)),
                ('firstnamename_father_eng', models.CharField(max_length=30)),
                ('lastname_father_eng', models.CharField(max_length=30)),
                ('firstname_mother_thai', models.CharField(max_length=30)),
                ('lastname_mother_thai', models.CharField(max_length=30)),
                ('firstname_mother_eng', models.CharField(max_length=30)),
                ('lastname_mother_eng', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WorkInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_service_date', models.DateField(verbose_name='date published')),
                ('position', models.CharField(max_length=30)),
                ('group', models.CharField(max_length=30)),
                ('end_service_date', models.DateField(verbose_name='date published')),
                ('current_position', models.CharField(max_length=60)),
                ('position_number', models.CharField(max_length=20)),
                ('rank_number', models.CharField(max_length=20)),
                ('rank_money', models.IntegerField(default=0)),
                ('academic_standing', models.CharField(max_length=20)),
                ('academic_standing_money', models.IntegerField(default=0)),
                ('start_PW_date', models.DateField(verbose_name='date published')),
                ('isGPF_member', models.BooleanField()),
                ('department', models.CharField(max_length=60)),
                ('subject', models.CharField(max_length=60)),
            ],
        ),
    ]

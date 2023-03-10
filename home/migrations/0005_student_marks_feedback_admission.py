# Generated by Django 4.1.3 on 2022-11-17 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_demo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.CharField(max_length=122)),
                ('Reg_No', models.CharField(max_length=122)),
                ('Address', models.CharField(max_length=122)),
                ('Taluka', models.CharField(max_length=122)),
                ('District', models.CharField(max_length=122)),
                ('State', models.CharField(max_length=122)),
                ('Photo', models.ImageField(upload_to='')),
                ('Pincode', models.IntegerField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reg_no', models.CharField(max_length=12)),
                ('Subject', models.CharField(max_length=122)),
                ('Marks', models.IntegerField(max_length=122)),
                ('Semester', models.CharField(max_length=122)),
                ('Year', models.IntegerField(max_length=122)),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reg_no', models.CharField(max_length=12)),
                ('Date', models.DateField()),
                ('Subject', models.CharField(max_length=122)),
                ('Feedback', models.TextField()),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.marks')),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reg_no', models.CharField(max_length=120)),
                ('Student_name', models.CharField(max_length=120)),
                ('Branch', models.CharField(max_length=50)),
                ('Class', models.CharField(max_length=50)),
                ('Year', models.IntegerField(max_length=10)),
                ('Date_of_admission', models.IntegerField(max_length=20)),
                ('Semester', models.CharField(max_length=20)),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
    ]

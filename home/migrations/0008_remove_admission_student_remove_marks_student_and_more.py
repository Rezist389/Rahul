# Generated by Django 4.1.1 on 2022-11-25 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_student_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admission',
            name='Student',
        ),
        migrations.RemoveField(
            model_name='marks',
            name='Student',
        ),
        migrations.AddField(
            model_name='marks',
            name='Student_name',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='admission',
            name='Reg_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.student'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='Reg_no',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.student'),
        ),
    ]
# Generated by Django 2.2 on 2019-05-02 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_settingsmodel_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addleavemodel',
            name='leave_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.LeaveTypeModel'),
        ),
        migrations.AlterField(
            model_name='employeebankmodel',
            name='emplyee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.EmployeePersonalModel'),
        ),
        migrations.AlterField(
            model_name='employeecontactmodel',
            name='emplyee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.EmployeePersonalModel'),
        ),
        migrations.AlterField(
            model_name='employeejoiningmodel',
            name='emplyee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.EmployeePersonalModel'),
        ),
        migrations.AlterField(
            model_name='employeepersonalbiomodel',
            name='emplyee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.EmployeePersonalModel'),
        ),
        migrations.AlterField(
            model_name='employeepersonalmodel',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.BranchModel'),
        ),
        migrations.AlterField(
            model_name='employeepersonalmodel',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.DepartmentModel'),
        ),
        migrations.AlterField(
            model_name='employeepersonalmodel',
            name='designation',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.DesignationModel'),
        ),
        migrations.AlterField(
            model_name='employeepreviousworkmodel',
            name='emplyee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.EmployeePersonalModel'),
        ),
        migrations.AlterField(
            model_name='employeequalificationmodel',
            name='emplyee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.EmployeePersonalModel'),
        ),
        migrations.AlterField(
            model_name='transfermodel',
            name='present_branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.BranchModel'),
        ),
        migrations.AlterField(
            model_name='transfermodel',
            name='present_department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.DepartmentModel'),
        ),
    ]

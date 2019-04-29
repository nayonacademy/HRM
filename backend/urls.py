from django.urls import path
from . import views
urlpatterns = [
    path('',views.homeView,name="home"),

    path('branch',views.branchView,name="branch"),
    path('branch_delete/<int:pk>',views.branch_delete,name="branch_delete"),
    path('branch_update/<int:pk>',views.branch_update,name="branch_update"),

    path('department',views.departmentView,name="department"),
    path('department_delete/<int:pk>',views.department_delete,name="department_delete"),
    path('department_update/<int:pk>',views.department_update,name="department_update"),

    path('designation',views.designationView,name="designation"),
    path('designation_delete/<int:pk>',views.designation_delete,name="designation_delete"),
    path('designation_update/<int:pk>',views.designation_update,name="designation_update"),

    path('employee',views.employeeReportView,name="employee"),
    path('addemployee',views.employeeAddView,name="addemployee"),

    
    path('transfer',views.transfer,name="transfer"),
    path('transfer_delete/<int:pk>',views.transfer_delete,name="transfer_delete"),
    path('transfer_update/<int:pk>',views.transfer_update,name="transfer_update"),
    
    path('get_employee',views.getEmployee,name='get_employee'),

    path('get_designation',views.employeeDesination,name='get_designation'),
    path('atttendance_report',views.atttendanceReportView,name="atttendance_report"),

    path('add_attendance',views.addAttendanceView,name="add_attendance"),

    path('leave_type',views.leaveTypeView,name="leave_type"),
    path('leave_type_delete/<int:pk>',views.leave_type_delete,name="leave_type_delete"),
    path('leave_type_update/<int:pk>',views.leave_type_update,name="leave_type_update"),
    
    path('add_leave',views.addLeaveView,name="add_leave"),
    path('add_leave_delete/<int:pk>',views.add_leave_delete,name="add_leave_delete"),
    path('add_leave_update/<int:pk>',views.add_leave_update,name="add_leave_update"),
    
    path('general_settings',views.generalsettingsView,name="general_settings"),

    path('get_attendance',views.getAttendance,name="get_attendance") 



]           
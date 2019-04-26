from django.urls import path
from . import views
urlpatterns = [
    path('',views.homeView,name="home"),
    path('branch',views.branchView,name="branch"),
    path('branch_delete/<int:pk>',views.branch_delete,name="branch_delete"),
    path('branch_update/<int:pk>',views.branch_update,name="branch_update"),
    path('department',views.departmentView,name="department"),
    path('department_delete/<int:pk>',views.department_delete,name="department_delete"),
    path('designation',views.designationView,name="designation"),
    path('employee',views.employeeReportView,name="employee"),
    path('addemployee',views.employeeAddView,name="addemployee"),
    path('atttendance_report',views.atttendanceReportView,name="atttendance_report"),
    path('add_attendance',views.atttendanceReportView,name="add_attendance"),
    path('leave_type',views.leaveTypeView,name="leave_type"),
    path('add_leave',views.addLeaveView,name="add_leave"),
    path('general_settings',views.generalsettingsView,name="general_settings")


]           
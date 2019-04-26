from django.urls import path
from . import views
urlpatterns = [
    path('',views.homeView,name="home"),
    path('branch',views.branchView,name="branch"),
    path('department',views.departmentView,name="department"),
    path('designation',views.designationView,name="designation"),
    path('employee',views.employeeReportView,name="employee"),
    path('addemployee',views.employeeAddView,name="addemployee")

]
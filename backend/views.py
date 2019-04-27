from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from .forms.branch_form import BranchForm
from .forms.department_form import DepartmentForm
from .forms.employee_form import *

# Create your views here.
# Start home method
def homeView(request):
    return render(request,'backend/index.html')
# End home method  

#Start Branch method    
def branchView(request):
        branch_all_data=BranchModel.objects.all()
        if request.method =='POST':
                branch=BranchForm(request.POST)
                if branch.is_valid():
                        branch.save()
                        messages.success(request,'Branch Form submission successful')
                        return HttpResponseRedirect(reverse('branch'))
                
        else:
                branch=BranchForm()
        context={
                'form':branch,
                'branch':branch_all_data
        }        
        return render(request,'backend/branch/branch.html',context) 

def branch_delete(request,pk):
        branch_delete_data=get_object_or_404(BranchModel,pk=pk)
        branch_delete_data.delete()
        messages.info(request,'Branch Deleted')
        return HttpResponseRedirect(reverse('branch')) 

def branch_update(request,pk):
        branch_edit_data=get_object_or_404(BranchModel,pk=pk)
        if request.method == 'POST':
                form=BranchForm(request.POST or None,instance=branch_edit_data)
                if form.is_valid():
                        form.save()
                        messages.success(request,"Branch data updated successfully")
                        return HttpResponseRedirect(reverse('branch'))
        else:
                form=BranchForm(instance=branch_edit_data)
        context={
                'form':form,
                
        }        
        return render(request,'backend/branch/branch_edit.html',context)
#End Branch method 

#Start Department method    
def departmentView(request):
        department_all_data=DepartmentModel.objects.all()
        if request.method =='POST':
                department=DepartmentForm(request.POST)
                if department.is_valid():
                        department.save()
                        messages.success(request,'Departmentform submission successful')
                        return HttpResponseRedirect(reverse('department'))
                
        else:
                department=DepartmentForm()
        context={
                'form':department,
                'department':department_all_data
        }        
        return render(request,'backend/department/department.html',context) 

def department_delete(request,pk):
        department_delete_data=get_object_or_404(DepartmentModel,pk=pk)
        department_delete_data.delete()
        messages.info(request,'Department Deleted')
        return HttpResponseRedirect(reverse('department')) 

#End Department method 


#Start Designation method    
def designationView(request):
        return render(request,'backend/designation/designation.html')
#End Designation method

#Start Designation method    
def employeeReportView(request):
        return render(request,'backend/employee/employee.html')
#End Designation method 
#Start Designation method    
def employeeAddView(request):
        basic_info=EmployeePersonalForm()
        context={
                'basic_info':basic_info
        }
        return render(request,'backend/employee/createemployee.html',context)
#End Designation method 
# start attendance report method
def atttendanceReportView(request):
        return render(request,'backend/attendance/attendance_report.html')
def addAttendanceView(request):
        # return HttpResponse('ok')
        return render(request,'backend/attendance/add_attendance.html')
def leaveTypeView(request):
        return render(request,'backend/leave/leave_type.html') 
def addLeaveView(request):
        return render(request,'backend/leave/add_leave.html')               
def generalsettingsView(request):
        return render(request,'backend/settings/general_settings.html')        
                     

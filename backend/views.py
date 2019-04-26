from django.shortcuts import render

# Create your views here.
# Start home method
def homeView(request):
    return render(request,'backend/index.html')
# End home method  

#Start Branch method    
def branchView(request):
    return render(request,'backend/branch/branch.html')
#End Branch method 

#Start Department method    
def departmentView(request):
    return render(request,'backend/department/department.html')
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
    return render(request,'backend/employee/createemployee.html')
#End Designation method 
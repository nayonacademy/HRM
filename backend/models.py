from django.db import models
# Create your models here.


# Branch Model
class BranchModel(models.Model):
    branch_name=models.CharField(max_length=40,unique=True)
    branch_status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):

        return self.branch_name
# Department Model
class DepartmentModel(models.Model):
    department_name=models.CharField(max_length=40,unique=True)
    department_status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):

        return self.department_name
# Designation Model
class DesignationModel(models.Model):
    department_name=models.ForeignKey(DepartmentModel,on_delete=models.DO_NOTHING, default=1)
    designation_name=models.CharField(max_length=40)
    designation_status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):

        return self.designation_name
# Employee Personal  Model
class EmployeePersonalModel(models.Model):
    employee_code=models.CharField(max_length=40)
    employee_name=models.CharField(max_length=40)
    branch=models.ForeignKey(BranchModel,on_delete=models.DO_NOTHING, default=1)
    department=models.ForeignKey(DepartmentModel,on_delete=models.DO_NOTHING, default=1)
    designation=models.ForeignKey(DesignationModel,on_delete=models.DO_NOTHING, default=1)
    father_name=models.CharField(max_length=40)
    mother_name=models.CharField(max_length=40)
    date_of_birth=models.DateTimeField(auto_now=False, auto_now_add=False)
    gender=models.CharField(max_length=20)
    national_id=models.CharField(max_length=50)
    nationality=models.CharField(max_length=30)
    blood_group=models.CharField(max_length=10)
    religion=models.CharField(max_length=20)
    marital_status=models.CharField(max_length=20)
    photo=models.ImageField(upload_to = 'emplyee_image/', default = 'emplyee_image/no-image.png')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.employee_name
# Employee Contact Model
class EmployeeContactModel(models.Model):
    emplyee_id=models.ForeignKey(EmployeePersonalModel,on_delete=models.DO_NOTHING)
    contact_number=models.CharField(max_length=30)
    contact_email=models.CharField(max_length=50)
    present_address=models.TextField()
    permanent_address=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.contact_email
 # Employee Bank Model      
class EmployeeBankModel(models.Model):
    emplyee_id=models.ForeignKey(EmployeePersonalModel,on_delete=models.DO_NOTHING)
    account_no=models.CharField(max_length=50)
    bank_name=models.CharField(max_length=40)
    branch_name=models.CharField(max_length=40)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.bank_name
 # Employee Joining Model        
class EmployeeJoiningModel(models.Model):
    emplyee_id=models.ForeignKey(EmployeePersonalModel,on_delete=models.DO_NOTHING)
    date_of_joining=models.DateTimeField(auto_now=False, auto_now_add=False)
    offer_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    confirmation_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.date_of_joining
 # Employee Qualification Model         
class EmployeeQualificationModel(models.Model):
    emplyee_id=models.ForeignKey(EmployeePersonalModel,on_delete=models.DO_NOTHING)
    name_of_exam=models.CharField(max_length=40)
    year_of_passing=models.CharField(max_length=30)
    board=models.CharField(max_length=30)
    grade=models.CharField(max_length=30)
    document_file=models.ImageField(upload_to='emplyee_document/', default='emplyee_document/no-image.png')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name_of_exam
 # Employee Previouswork Model        
class EmployeePreviousworkModel(models.Model):  
    emplyee_id=models.ForeignKey(EmployeePersonalModel,on_delete=models.DO_NOTHING)
    company_name=models.CharField(max_length=40)
    company_address=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    duration=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.company_name
 # Employee Personalbio Model        
class EmployeePersonalbioModel(models.Model):  
    emplyee_id=models.ForeignKey(EmployeePersonalModel,on_delete=models.DO_NOTHING)
    cv_file=models.ImageField(upload_to='emplyee_document/', default='emplyee_document/no-image.png')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
# Attendance Model    
class AttendanceModel(models.Model):
    date=models.DateTimeField(auto_now=False, auto_now_add=False)
    department=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.department 
# Attendance Child Model 
class AttendanceChildModel(models.Model):
    attendance=models.ForeignKey(AttendanceModel,on_delete=models.DO_NOTHING)
    employee_code=models.CharField(max_length=40)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.employee_code
# Leave Type Model         
class LeaveTypeModel(models.Model):
    name=models.CharField(max_length=30) 
    description=models.TextField()
    status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 
 # Add Leave Model        
class AddLeaveModel(models.Model):
    employee_code=models.CharField(max_length=40) 
    leave_type=models.ForeignKey(LeaveTypeModel,on_delete=models.DO_NOTHING, default=1)
    from_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    to_date=models.DateTimeField(auto_now=False, auto_now_add=False)
    reason=models.TextField()
    status=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.employee_code 
# Add Transfer Model    
# class TransferModel(models.Model):
#     employee_code=models.CharField(max_length=40)
#     issue_date=models.DateTimeField(auto_now=False, auto_now_add=False)
#     previous_branch=models.ForeignKey(BranchModel,on_delete=models.DO_NOTHING, default=1)
#     previous_department=models.ForeignKey(DepartmentModel,on_delete=models.DO_NOTHING, default=1)
#     present_branch=models.ForeignKey(BranchModel,on_delete=models.DO_NOTHING, default=1)
#     present_department=models.ForeignKey(DepartmentModel,on_delete=models.DO_NOTHING, default=1) 
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True) 
#      def __str__(self):
#         return self.employee_code 


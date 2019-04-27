from django import forms
from backend.models import *

class EmployeePersonalForm(forms.ModelForm):
    class Meta:
        model=EmployeePersonalModel
        fields = '__all__'
        choices=(('','--Select--'),('Active','Active'),('Inactive','Inactive'))
        gender=(('','--Select--'),('Female','Female'),('Male','Male'))
        religion=(('','--Select--'),('Islam','Islam'),('Hindu','Hindu'))
        marital_status=(('','--Select--'),('Unmarried','Unmarried'),('Married','Married'))
        blood_group=(('','--Select--'),('O+','O+'),('O-','O-'),('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'))
        widgets={
            
            'employee_code':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Employee Code'}),
            'employee_name':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Employee Name'}),
            'branch':forms.Select(attrs={'class':'form-control input-circle','id':'branch'}),
            'department':forms.Select(attrs={'class':'form-control input-circle','id':'department'}),
            'designation':forms.Select(attrs={'class':'form-control input-circle','id':'designation'}),
            'father_name':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Father Name'}),
            'mother_name':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Mother Name'}),
            'date_of_birth':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control input-circle', 'placeholder':'Select a date', 'type':'date'}),
            'gender':forms.Select(attrs={'class':'form-control input-circle'},choices=gender),
            'national_id':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'National Id'}),
            'nationality':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Nationality'}),
            'blood_group':forms.Select(attrs={'class':'form-control input-circle','id':'designation'},choices=blood_group),
            'religion':forms.Select(attrs={'class':'form-control input-circle','id':'designation'},choices=religion),
            'marital_status':forms.Select(attrs={'class':'form-control input-circle','id':'designation'},choices=marital_status)
           
        }  
class EmployeeContactForm(forms.ModelForm):
    class Meta:
        model=EmployeeContactModel
        fields='__all__'
        widgets={
            'contact_number':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Contact Number'}),
            'contact_email':forms.EmailInput(attrs={'class':'form-control input-circle','placeholder':'eg.: email@email.com'}),
            'present_address':forms.Textarea(attrs={'class':'form-control input-circle','rows':'2','cols':'3','placeholder':'Present Address'}),
            'permanent_address':forms.Textarea(attrs={'class':'form-control input-circle','rows':'2','cols':'3','placeholder':'Parmanent Address'})

        }   
class EmployeeBankForm(forms.ModelForm):
       class Meta:
           model=EmployeeBankModel
           fields='__all__'
           widgets={
             'account_no':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Account No'}),
             'bank_name':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Bank No'}),
             'branch_name':forms.TextInput(attrs={'class':'form-control input-circle','placeholder':'Branch Name'})
        
           }   
class EmployeeJoiningForm(forms.ModelForm):
    class Meta:
        model=EmployeeBankModel
        fields='__all__'
        widgets={
           'date_of_joining':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
           'offer_date':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
           'confirmation_date':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'})
           }
class EmployeeQualificationForm(forms.ModelForm):
    class Meta:
        model=EmployeeQualificationModel
        fields='__all__'
        widgets={
            'name_of_exam':forms.TextInput(attrs={'class':'form-control','placeholder':'Name Of Exam'}),
            'year_of_passing':forms.TextInput(attrs={'class':'form-control','placeholder':'Passing Year'}),
            'board':forms.TextInput(attrs={'class':'form-control','placeholder':'Board'}),
            'grade':forms.TextInput(attrs={'class':'form-control','placeholder':'Grade'})

         }

class EmployeePreviousworkForm(forms.ModelForm):
    class Meta:
        model=EmployeePreviousworkModel
        fields='__all__'
        widgets={
            'company_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Company Name'}),
            'company_address':forms.Textarea(attrs={'class':'form-control','rows':'2','cols':'3','placeholder':'Company Address'}),
            'designation':forms.TextInput(attrs={'class':'form-control','placeholder':'Designation'}),
            'duration':forms.TextInput(attrs={'class':'form-control','placeholder':'Duration'})

        }
  


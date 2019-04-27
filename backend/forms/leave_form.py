from django import forms
from backend.models import LeaveTypeModel

class LeaveTypeForm(forms.ModelForm):
    class Meta:
        model=LeaveTypeModel
        fields = '__all__'
        choices=(('','--Select--'),('Active','Active'),('Inactive','Inactive'))
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'},choices=choices)

        }
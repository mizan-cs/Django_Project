from django import forms

class Reg_Form(forms.Form):
    First_Name = forms.CharField(max_length=100)
    Last_Name = forms.CharField(max_length=100)
    Email = forms.CharField(max_length=150)
    Phone_Numebr = forms.CharField(max_length=100)
    Institute = forms.CharField(max_length=100)
    Address = forms.CharField(max_length=200)
    City = forms.CharField(max_length=50)
    Gender = forms.CharField(max_length=20)
    Password = forms.CharField(max_length=100,)
    Confirm_Password = forms.CharField(max_length=100)
    '''
        first_name = rf.cleaned_data['first_name']
        last_name = rf.cleaned_data['last_name']
        email = rf.cleaned_data['email']
        phone = rf.cleaned_data['mobile_number']
        institute = rf.cleaned_data['institute']
        address = rf.cleaned_data['address']
        city = rf.cleaned_data['city']
        gender = rf.cleaned_data['value']
        password = rf.cleaned_data['password']
        confirm_password = rf.cleaned_data['confirm_password']

        ct = {'fn': first_name, 'ln': last_name, 'email': email, 'phone': phone, 'institute': institute,
             'addr': address, 'city': city, 'sex': gender, 'password': password, 'cf': confirm_password}
    '''

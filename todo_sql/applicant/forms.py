from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from .models import Applicant

class ApplicantCreationForm(UserCreationForm):
    def __init__(self,*args,**kargs):
        super(ApplicantCreationForm,self).__init__(*args,**kargs)
        del self.filds['username']

    class Meta:
        model = Applicant
        filds = ('email',)

class ApplicantChangeForm(UserChangeForm):

    def __init__(self,*args,**kargs):
        super(ApplicantChangeForm,self).__init__(*args,**kargs)
        del self.files['username']
        class Meta:
            model = Applicant
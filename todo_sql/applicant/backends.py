from .models import Applicant

class ApplicantAuth(object):
    def authenticate(self,username=None,password=None):
        try:
            applicant = Applicant.objects.get(email=username)
            if applicant.check_password(password):
                return applicant
        except Applicant.DoesNotExist:
            return None
    def get_applicant(self,applicant_id):
        try:
            applicant = Applicant.objects.get(pk=applicant_id)
            if applicant.is_active:
                return applicant
            return None
        except Applicant.DoesNotExist:
            return None
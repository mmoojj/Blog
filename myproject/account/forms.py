from django.forms import ModelForm
from .models import User

class UserModelForm(ModelForm):
    def __init__(self,*args,**kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text=None
        if not user.is_superuser:
            self.fields['username'].disabled=True 
            self.fields['email'].disabled=True 
            self.fields['spetial_user'].disabled=True 
            self.fields['is_author'].disabled=True 
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','spetial_user','is_author'] 
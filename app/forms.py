from django import forms

g = [('male','MALE'),('female','FEMALE')]
c = [('python','python'),('django','django')]
class RegistationForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(max_value=100)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=g)
    # gender = forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course = forms.MultipleChoiceField(choices=c)
    # course = forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)

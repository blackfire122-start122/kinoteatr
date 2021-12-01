from .models import Country
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm 
from django.forms import(ModelForm, 
						TextInput,
						PasswordInput, 
						FileInput,
						ModelMultipleChoiceField, 
						Select,
						FileField,
						IntegerField)
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1','password2']
		widgets = {
			'username':TextInput(attrs={
				'class':'form_name','placeholder':'username',}),
			'password1':PasswordInput(attrs={
				'class':'form_pass','placeholder':'pass1',}),
			'password2':PasswordInput(attrs={
				'class':'form_pass','placeholder':'pass2',}),
			}
class ChangeForm(UserChangeForm):
	img = FileField(widget=FileInput(attrs={
				'class':'input_file_change','id':"input_file_change"})
	)
	age = IntegerField(widget=TextInput(attrs={
				'class':'form_age_change','placeholder':'Age','id':'age'})
	)
	class Meta:
		model = User
		fields = ['username',
			'first_name','last_name',
			'email',
			'country','img','age'
			]
		widgets = {
			'username':TextInput(attrs={
				'class':'form_name_change','placeholder':"name",'id':'username'}),
			'first_name':TextInput(attrs={
				'class':'form_name_change','placeholder':'first_name','id':'first_name'}),
			'last_name':TextInput(attrs={
				'class':'form_name_change','placeholder':'last_name','id':'last_name'}),
			'email':TextInput(attrs={
				'class':'form_email_change','placeholder':'Email','id':'email'}),
			}


class Users_login_Form(AuthenticationForm):
	class Meta:
		model = User
		fields = ['username','password']

		widgets = {
			'username':TextInput(attrs={
				'class':'form_name',
				'placeholder':'Name',
				}),
			'password':PasswordInput(attrs={
				'class':'form_pass',
				'placeholder':'pass',
				}),
		}
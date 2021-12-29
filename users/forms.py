from .models import Country
from django.contrib.auth.forms import (UserCreationForm,
								AuthenticationForm,
								UserChangeForm,
								PasswordResetForm)
from django.forms import(ModelForm, 
						TextInput,
						PasswordInput, 
						FileInput,
						ModelMultipleChoiceField, 
						Select,
						FileField,
						IntegerField,
						ModelChoiceField)
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterForm(UserCreationForm):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].widget = TextInput(attrs={
				'class':'form_name','placeholder':'username'})
		self.fields['password1'].widget = PasswordInput(attrs={
				'class':'form_pass','placeholder':'pass1'})
		self.fields['password2'].widget = PasswordInput(attrs={
				'class':'form_pass','placeholder':'pass2'})

	class Meta:
		model = User
		fields = ['username','password1','password2']
	
class ChangeForm(UserChangeForm):
	img = FileField(required=False,widget=FileInput(attrs={
				'class':'input_file_change','id':"input_file_change"})
	)
	age = IntegerField(required=False,widget=TextInput(attrs={
				'class':'form_age_change','placeholder':'Age','id':'age'})
	)
	country = ModelChoiceField(Country.objects.all(),required=False)
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
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget = TextInput(attrs={
				'class':'form_name',
				'placeholder':'Name',
			})
		self.fields['password'].widget = PasswordInput(attrs={
				'class':'form_pass',
				'placeholder':'pass',
			})
	class Meta:
		model = User
		fields = ['username','password']
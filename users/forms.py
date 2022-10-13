from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .models import Profile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields=('username','email')
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Please use another Email, that one already taken")
        return email
            
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("image","bio")
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "username")



# kullancii passwordunu resetlemek istediginde, gelen sayfada email istiyorum. Bu email db de kayitli olan bir email degil ise raise ValidationError ile kullaniciya bu email kayitli degil diyerek hata return ediyorum.
# Ayrica bunu burda override ettigim icin url.py da password_reset kisminda form_class diyerek bu class i veriyorum(template_name vererek, hazir template i override ettigim gibi), bu yaptigim degsikligin django taradindan algilanabilmesi icin.

# (Peki form_class i degsitirmem/override etmem gerektigini nasil anladim ? Cünkü email i unuttum kismini tikladigimda login olurken, gelen sayfa password_reset sayfasi ve gelen hazir bir form.. Bunu hazir kullandim projede. Bunun icin django views olarak, url e yazdigim auth_views.PasswordResetView tiklayarak neyi override etmem gerektigini anladim.)           
class PasswordResetEmailCheck(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not User.object.filter(email=email).exists():
            raise forms.ValidationError("This email is not registered")
        return email
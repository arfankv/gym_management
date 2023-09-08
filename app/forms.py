from django.contrib.auth.forms import UserCreationForm
from app.models import Login


class TrainerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username','password1','password2', 'name', 'age', 'email', 'address', 'contact_no','photo')

class CustomerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username','password1','password2', 'name', 'age', 'email', 'address', 'contact_no', 'photo')


from django import from .forms import
from .models import Todo

class TodoForm(forms.class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ("__all__",)
        #exclude=[]
)
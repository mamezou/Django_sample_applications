from django import forms
from .models import Photo


class PhotoCreateForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('title', 'comment', 'image')
        widgets = {
            'title': forms.TextInput(attrs={  # <input type="text" class="form-control"
                'class': 'form-control',
            }),
            'comment': forms.Textarea(attrs={  # <textarea class="form-cotrol"
                'class': 'form-control',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': "form-control-file",
            }),
        }

from django import forms
from .models import Status
class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('user', 'content', 'image')


    def clean_content(self,*args,**kwargs):
        con = self.cleaned_data.get('content')
        if len(con)>240:
            raise forms.ValidationError('Content should not be greater than 240 characters')
        return con
    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        image = data.get('image', None)
        content = data.get('content', None)
        if content == "":
            content = None
        if image is None and content is None:
            raise forms.ValidationError('Content or image is required')
        return data



    """we can also return super().clean(*args, **kwargs)"""
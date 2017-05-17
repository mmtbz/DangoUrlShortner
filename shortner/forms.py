__author__ = 'Dave'

from django import forms
from .validators import validate_url, validate_dot_com


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='',
                          validators=[validate_url, validate_dot_com],
                          widget=forms.TextInput(
                              attrs={"placeholder": "Long URL",
                                     "class": "form-control"
                                     }
                          )
                          )

    def clean_url(self):
        url = self.cleaned_data['url']  # we are using 'url' because it is the declared one
        # url_validator = URLValidator()
        if 'http' in url:
            return url
        return 'http://' + url


"""
    def clean(self):
        cleaned_data = super(SubmitUrlForm, self).clean()
        # print(cleaned_data)
"""

from django import forms
from firestore.utils.constants import Constants
from firestore.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": Constants.FORM_CLASS.value}),
            "description": forms.Textarea(attrs={"class": Constants.TEXT_AREA.value}),
        }


class Themes(forms.Form):
    theme = forms.ChoiceField(
        choices=Constants.THEME_CHOICES.value,
        widget=forms.Select(
            attrs={
                "class": Constants.SELECT_CLASS.value,
                "id": "themeSelect",
                "required": False,
            }
        ),
    )


class NewsLetter(forms.Form):
    subscribe = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "grow", "type": "email"})
    )

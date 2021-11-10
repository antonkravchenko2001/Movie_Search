from django import forms
from .models import MoviesInfo

from django import forms

class MoviesForm(forms.ModelForm):
    class Meta:
        model = MoviesInfo
        fields = [
            'movie_id',
            'title',
            'release_date',
            'duration',
            'box_office',
            'plot',
        ]

        widgets={
            'movie_id': forms.NumberInput(attrs={'class': 'movie-submit'}),
            'title': forms.TextInput(attrs={'class': 'movie-submit'}),
            'plot': forms.Textarea(attrs={'class': 'movie-submit'}),
            'duration': forms.TextInput(attrs={'class': 'movie-submit'}),
            'box_office': forms.NumberInput(attrs={'class': 'movie-submit'}),
            'release_date': forms.TextInput(attrs={'class': 'movie-submit'}),
        }


    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title == "":
            raise forms.ValidationError("title field is be empty")
        for instance in MoviesInfo.objects.all():
            if instance.title == title:
                raise forms.ValidationError(f'There exists a movie titled "{title}"')
        return title
    
    def clean_plot(self):
        plot = self.cleaned_data.get('plot')
        if plot == "":
            raise forms.ValidationError("plot field is empty")
        return plot
    

    
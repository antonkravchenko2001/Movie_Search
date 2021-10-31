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
            'countries',
            'genre',
            'plot',
        ]
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title == "":
            raise forms.ValidationError("title can't be empy")
        for instance in MoviesInfo.objects.all():
            if instance.title == title:
                raise forms.ValidationError(f'There is a movie with title {title}')
        return title
    
    def clean_plot(self):
        plot = self.cleaned_data.get('plot')
        if plot == "":
            raise forms.ValidationError("plot can't be empy")
        return plot
    

    
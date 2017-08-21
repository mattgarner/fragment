from django.forms import ModelForm

from HD.models import Genemarker_data

class Genemarker_dataForm(ModelForm):
    class Meta:
        model = Genemarker_data
        fields = ('gm_file',)
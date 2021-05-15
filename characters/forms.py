from django import forms

class CharactersForm(forms.Form):
    name = forms.CharField(label='名前', max_length=20)
    gender = forms.ChoiceField(label='性別',
        choices = (
            ('unknown', '不明'),
            ('man', '男'),
            ('woman', '女'),
        )
    )  
    discription = forms.CharField(label="説明", max_length=1000)

    def post(self, name, gender, discription):
        name = self.cleaned_data[name]
        gender = self.cleaned_data[gender]
        discription = self.cleaned_data[discription]
        



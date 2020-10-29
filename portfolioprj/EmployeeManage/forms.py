from django import forms

labels = ['チェック','複数チェック','ラジオボタン','動的選択肢１','動的選択肢２']
CHOICE = [
    ('1','Higher'),
    ('2','Lower')]

class EmployeeFrom(forms.Form):
    id_num = forms.IntegerField(
        label='ID',
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'ID', 'class':'google_font'})
    )
    name = forms.CharField(
        label='Name',
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'Name', 'class':'google_font'})
    )
    dept = forms.CharField(
        label='Dept',
        max_length=10,
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'Dept', 'class':'google_font'})
    )
    salary = forms.IntegerField(
        label='Salary',
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'Salary', 'class':'google_font'})
    )
    radio = forms.MultipleChoiceField(
         label=labels[2],
         disabled=False,
         required=True,
         initial=['1'],
         choices=CHOICE,
         widget=forms.RadioSelect(attrs={'id': 'radio','class': 'form-check-input'}))
  
class CreateEmployeeFrom(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Name', 'class':'google_font'})
    )
    dept = forms.CharField(
        label='Dept',
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Dept', 'class':'google_font'})
    )
    salary = forms.IntegerField(
        label='Salary',
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Salary', 'class':'google_font'})
    )

    # カスタム　バリデーション
    # ※特にカスタムする必要がない為、今回は使用しない

    # def clean_salary(self):
    #     try:
    #         salary = self.cleaned_data['id_num']
    #         print('validation::::')
    #         print(len(salary))
    #         if salary:
    #             int(salary)
    #         else:
    #             return salary
    #     except Exception:
    #         raise forms.ValidationError('10桁以内の整数を入力して下さい。')
    #         print('form error salary:::::::')

    # def clean_radio(self):
    #     radio = self.cleaned_data['radio']
    #     if not radio:
    #         raise forms.ValidationError('radio のバリデーションに引っかかりました。')
    #     else:
    #         return radio
    #         print('form error radio:::::::')



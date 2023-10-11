from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Column, Row


class ResumeForms(forms.Form):

    name = forms.CharField(max_length=200)
    # email = forms.EmailField()
    # telephone = forms.CharField()
    # address = forms.CharField()
    # skill_1 = forms.CharField()
    # skill_2 = forms.CharField()
    # skill_3 = forms.CharField()
    # skill_4 = forms.CharField()

    # experience_1_Title=forms.CharField()
    # experience_1_Duration = forms.CharField(widget=forms.DateInput(attrs={'type':'date', 'max':datetime.month}))
    # experience_1_description = forms.CharField()

    # experience_2_Title=forms.CharField()
    # experience_2_Duration = forms.CharField(widget=forms.DateInput(attrs={'type':'date','max':datetime.month}))
    # experience_2_description = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = reverse_lazy('home')
        self.helper.add_input(Submit('submit', 'Submit'))
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('name', css_class='form-group col-md-5  mb-10'),
    #             Column('email', css_class='form-group col-md-7 mb-10'),
    #             css_class='form-row  center'
    #         ),
    #         Row(
    #             Column('telephone', csss_class='form-group col-md-5 mb-10'),
    #             Column('address', csss_class='form-group col-md-5 mb-10'),
    #             css_class = 'form-row center'
    #         ),
    #         Row(
    #             Column('skill_1', csss_class='form-group col-md-6 mb-10'),
    #             Column('skill_2', csss_class='form-group col-md-6 mb-10'),
    #             css_class = 'form-row center'
    #         ),
    #         Row(
    #             Column('skill_3', csss_class='form-group col-md-6 mb-10'),
    #             Column('skill_4', csss_class='form-group col-md-6 mb-10'),
    #             css_class = 'form-row center'
    #         ),
    #         Row(
    #             Column('experience_1_Title', csss_class='form-group col-md-7 mb-10'),
    #             Column('experience_1_Duration', csss_class='form-group col-md-5 mb-10'),
    #             css_class = 'form-row center'
    #         ),
    #         'experience_1_description',
    #         Row(
    #             Column('experience_2_Title', css_class='form-group col-md-7 mb-10'),
    #             Column('experience_2_Duration', css_class='form-group col-md-5 mb-10'),
    #             css_class='form-row center'
    #         ),
    #         'experience_2_description'
    #     )
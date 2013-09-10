from django import forms
from base_maternal_model_form import BaseMaternalModelForm
from mpepu_maternal.models import (MaternalEnroll, MaternalEnrollDem, MaternalEnrollOb, MaternalEnrollMed, MaternalEnrollDx,
                                   MaternalEnrollClin, MaternalEnrollArv)


class MaternalEnrollForm (BaseMaternalModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data

        # if recruit_source == OTHER, recruit_source_other may not be blank"""
        if cleaned_data.get('recruit_source', None) == 'OTHER' and cleaned_data.get('recruit_source_other', None) == '':
            raise forms.ValidationError("If recruitment source is 'OTHER', please specify. You wrote '%s'" % cleaned_data.get('recruit_source_other', None))
        # if prev_pregnancy super(MyModelForm, self).clean()es == 0, prev_pregnancy_arv must be N/A"""
        if cleaned_data.get('prev_pregnancies', None) == 0 and cleaned_data.get('prev_pregnancy_arv', None) != 'N/A':
            raise forms.ValidationError("If no previous pregnancies, question (4) refering to ARVs during previous pregnancies should be 'Not Applicable'. You wrote '%s'" % cleaned_data.get('prev_pregnancy_arv', None))
        # if previous pregnancy <>0, then prev_pregnancy_arv <>N/A"""
        if cleaned_data.get('prev_pregnancies', None) != 0 and cleaned_data.get('prev_pregnancy_arv', None) == 'N/A':
            raise forms.ValidationError("If there are previous pregnancies, question (4) refering to ARVs during previous pregnancies should be 'Yes' or 'No'. You wrote '%s'" % cleaned_data.get('prev_pregnancy_arv', None))
        # if prev_pregnancies == 0, forms MaternalEnrollOb and  MaternalEnrollClin are not required"""

        return super(MaternalEnrollForm, self).clean()

    class Meta:
        model = MaternalEnroll


class MaternalEnrollDemForm (BaseMaternalModelForm):

    def clean(self):

        cleaned_data = self.cleaned_data

        # if unemployed then they have no personal earn and they are not providing most money"""
        if cleaned_data.get('current_occupation', None) == 'Unemployed' and cleaned_data.get('provides_money', None) == 'You':
            raise forms.ValidationError("If partcipant is unemployed they will not be providing most money. You wrote '%s'" % cleaned_data.get('provides_money', None))
        if cleaned_data.get('current_occupation', None) == 'Unemployed' and cleaned_data.get('money_earned', None) != 'None':
            raise forms.ValidationError("If partcipant is unemployed they will not be earning any money. You wrote '%s'" % cleaned_data.get('money_earned', None))

        # if they are not married or widowed they cannot be a housewife"""
        if cleaned_data.get('current_occupation', None) == 'Housewife' and cleaned_data.get('marital_status', None) == 'Single':
            raise forms.ValidationError("The participant is not married or widowed or divorced, they cannot be a housewife. You wrote '%s'" % cleaned_data.get('marital_status', None))
        if cleaned_data.get('current_occupation', None) == 'Housewife' and cleaned_data.get('marital_status', None) == 'Cohabiting':
            raise forms.ValidationError("The participant is not married or widowed or divorced, they cannot be a housewife. You wrote '%s'" % cleaned_data.get('marital_status', None))

        #if employed then personal earn cannot be none"""
        #if cleaned_data.get('current_occupation', None) <> 'Unemployed' and cleaned_data.get('money_earned', None) == 'None':
            #raise forms.ValidationError("The participant is employed, indicate her personal earn. You wrote '%s'" %  cleaned_data.get('money_earned', None))
        #if 'non of the above is selected, then no other option should be selected """
        #if 'non of the above is selected, then no other option should be selected """
        if cleaned_data.get('hh_goods', None) == 'None of the above' and len(cleaned_data.get('hh_goods', None)) != 1:
            raise forms.ValidationError("if they have none of these goods, they cannot have any of other listed items. Please correct")

        return super(MaternalEnrollDemForm, self).clean()

    class Meta:
        model = MaternalEnrollDem


class MaternalEnrollObForm (BaseMaternalModelForm):

    class Meta:
        model = MaternalEnrollOb


class MaternalEnrollMedForm (BaseMaternalModelForm):

    def clean(self):

        cleaned_data = self.cleaned_data

        if 'chronic_cond' in cleaned_data:
            self.validate_m2m(
                    label='chronic condition',
                    leading=cleaned_data.get('has_chronic_cond', None),
                    m2m=cleaned_data.get('chronic_cond', None),
                    other=cleaned_data.get('chronic_cond_other', None),
            )
        return super(MaternalEnrollMedForm, self).clean()

    class Meta:
        model = MaternalEnrollMed


class MaternalEnrollDxForm (BaseMaternalModelForm):

    class Meta:
        model = MaternalEnrollDx


class MaternalEnrollArvForm (BaseMaternalModelForm):

    class Meta:
        model = MaternalEnrollArv


class MaternalEnrollClinForm (BaseMaternalModelForm):

    class Meta:
        model = MaternalEnrollClin
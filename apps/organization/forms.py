# _*_ coding: utf-8 _*_
__author__ = 'seal'
__data__ = '7/1/17'

import re
from django import forms
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']


    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGX_MOBILE = "/^1[34578]\d{9}$"
        p = re.compile(REGX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法",code="mobile_invalid")
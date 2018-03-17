# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django import forms

from .models import Panino


class PaninoForm(forms.ModelForm):
    class Meta:
        model = Panino
        fields = '__all__'

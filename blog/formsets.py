from django.forms import BaseInlineFormSet, BaseModelFormSet, ValidationError, modelformset_factory
from blog.models import Post


class BasePostFormSet(BaseInlineFormSet):

    def clean(self):
        super().clean()
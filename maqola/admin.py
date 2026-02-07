from django.contrib import admin
from .models import Maqola, Comment, Like, Category
from ckeditor.widgets import CKEditorWidget
from django import forms

class MaqolaForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Maqola
        fields = '__all__'

class MaqolaAdmin(admin.ModelAdmin):
    form = MaqolaForm

admin.site.register(Maqola, MaqolaAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Category)
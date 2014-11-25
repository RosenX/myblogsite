from django import forms
from blog.models import Classification

class BlogAddForm(forms.Form):
	# ch = [(obj.id,obj.name) for obj in Classification.objects.all()]
	caption = forms.CharField()
	content = forms.CharField(widget=forms.Textarea)
	tag = forms.CharField(required=False)
	# classification = forms.ChoiceField(required=True,widget=forms.Select(),choices=ch)
	classification = forms.CharField()

class searchForm(forms.Form):
	keyWords =forms.CharField()

class cmtAddForm(forms.Form):
	"""docstring for cmtAddForm"""
	name = forms.CharField()
	email = forms.EmailField()
	content = forms.CharField(widget = forms.Textarea)
	thread = forms.CharField(required=False)
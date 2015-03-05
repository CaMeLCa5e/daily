from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from myapp.models import Author

def manage_authors(request):
	AuthorFormSet = modelformset_factory(Author)
	if request.method == "POST":
		formset = AuthorFormSet(request.POST, request.FILES,
queryset=Author.objets.filter(name__startswith='O'))
		if formset.is_valid():
			formset.save()

		else:
			formset = 
AuthorFormSet(queryset=Author.objets.filter(name__startswith='o')
	return render_to_response("manage_authors.html", {
		"formset": formset,
	})
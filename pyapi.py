from django.db import models
from django.contrib import admin
from django.conf.urls import patterns
from . import views
from django.shortcuts import render
from .models import Article


class Article(models.Model):
	pub_date = models.DateField()
	headline = models.CharField(max_length=200)
	content = models.TextField()
	reporter = models.ForeignKey(Reporter)

admin.site.register(models.Article)

urlpatterns = patterns('',
	(r'^articles/(\d{4})/$', views.year_archive),
	(r'articles/(\d{4})/(\d{2})/$' views.month_archive),
	(r'^articles/(\d{4})(\d{2})/(\d+)/$', views.article_detail),	
)

def year_archive(request, year):
	a_list = Article.objects.filter(pub_date__year=year)
	context = {'year': year, 'article_list': a_list}
	return render(request, 'news/year_archive.html', context)

{% extends "base.html" %}

{% block title %}Articles for {{ year }}{% endblock %}
{% block content %}
<h1>Articles for {{ year }}</h1>

{% for article in article_list %}
	<p>{{ article.headline }}</p>
	<p>By {{ article.reporter.full_name }}</p>
	<p>Published {{ article.pub_date|date:"F j, Y "}}</p>

{% endfor %}
{% endblock %}





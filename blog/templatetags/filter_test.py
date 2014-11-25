from django import template

register=template.Library()

@register.filter
def getfirstPara(content):
	a = content.split("</p>")
	return a[0]

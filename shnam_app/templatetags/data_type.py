from django import template
register = template.Library()
@register.filter
def data_type(data):
	data_type = None
	if str(data) == "Follow object":
		data_type = "fol"
	elif str(data) == "MusicMsg object":
		data_type = "msg"
	return data_type
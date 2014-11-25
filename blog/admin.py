from django.contrib import admin

# Register your models here.

from blog.models import *

class BlogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('caption', 'id', 'publish_time')
    list_filter = ('publish_time',)
    #date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)

class TagAdmin(admin.ModelAdmin):
	"""docstring for TagAdmin"""
	list_display = ('tag_name','count')
	ordering = ('-count',)

class ClassificationAdmin(admin.ModelAdmin):
	"""docstring for ClassificationAdmin"""
	list_display = ('name','count')
	ordering = ('-count',)

class AuthorAdmin(admin.ModelAdmin):
	"""docstring for AuthorAdmin"""
	list_display=('user','count')
	ordering = ('-count',)

class CommentAdmin(admin.ModelAdmin):
	"""docstring for CommentAdmin"""
	list_display=('username','email','blog')										

admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Classification,ClassificationAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Comment,CommentAdmin)

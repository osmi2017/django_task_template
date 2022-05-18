from django.contrib import admin

# Register your models here.
from task.models import Blog_article, Contact_request

class Blog_articleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog_article, Blog_articleAdmin)

class Contact_requestAdmin(admin.ModelAdmin):


    def has_change_permission(self, request, obj=None):
        if obj is not None :
            return False
        return super().has_change_permission(request, obj=obj)

admin.site.register(Contact_request, Contact_requestAdmin)

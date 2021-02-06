from django.contrib import admin

from Construct.models import ConstructionCategory, ConstructionProjects, ConstructionArchitects, Images

class adminConstructionCategory(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    
class adminConstructionProjects(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(ConstructionCategory, adminConstructionCategory)
admin.site.register(ConstructionProjects, adminConstructionProjects)
admin.site.register(ConstructionArchitects)
admin.site.register(Images)
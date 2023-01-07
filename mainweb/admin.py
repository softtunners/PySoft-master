from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Scrapbook)
admin.site.register(ScrapBookImg)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_title',)
    icon_name = 'apps'

# class CommentAdmin(admin.ModelAdmin):
#     list_display =('post','username')
class ContactAdmin(admin.ModelAdmin):
    list_display=("fname","email","number")
    icon_name='contact_phone'

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','post_date',)
    search_fields = ('tags',)
    list_filter= ('category','title',)
    list_per_page = 8
    icon_name='add_to_photos'




admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(IpModel)
admin.site.register(BlogComment)
admin.site.register(SubcribeUsers)


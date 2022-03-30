from django.contrib import admin
from .models import Support, Answer

class SupportAdmin(admin.ModelAdmin):
    list_display = ('id','autor','title','description','date','done')
    list_display_links = ('id','autor','title')
    search_fields = ('id','autor','title','description')
    list_editable = ('done',)
    list_filter = ('done',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'support', 'text_answer', 'date')
    list_display_links = ('id', 'support')
    search_fields = ('id', 'support', 'text_answer')

admin.site.register(Support,SupportAdmin)
admin.site.register(Answer,AnswerAdmin)
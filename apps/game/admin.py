from django.contrib import admin
from apps.game.models.category import Category
from apps.game.models.question import Question

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    search_fields = ('category__name',)
    list_filter = ('category__name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)



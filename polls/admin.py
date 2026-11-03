from django.contrib import admin

from .models import Choice, Question

# TabularInline and StackedInline are two different ways to display related objects in the Django admin interface. 
# TabularInline displays related objects in a table format, while StackedInline displays them in a stacked format. 
# The choice between the two depends on the amount of information you want to display and your personal preference.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]


admin.site.register(Question, QuestionAdmin)

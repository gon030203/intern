from django.contrib import admin
from .models import Question,Choice

admin.site.site_header = "Quản trị ứng dụng Polls"

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"],"classes":["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
class ChoiceInline(admin.TabularInline): ...

admin.site.register(Question, QuestionAdmin)
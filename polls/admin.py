from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets 元组中的第一个元素是字段集的标题
    fieldsets = [
        (None, {"fields":["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]

# 向管理页面中加入投票应用
admin.site.register(Question, QuestionAdmin)

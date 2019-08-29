from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]  # 作用域，以及前台显示顺序


# 向管理页面中加入投票应用
admin.site.register(Question, QuestionAdmin)

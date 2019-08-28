from django.contrib import admin
from .models import Question

# 向管理页面中加入投票应用
admin.site.register(Question)

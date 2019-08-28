from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    # 一个快捷函数： render()
    return render(request, "polls/index.html", context)

    # 载入模板，填充上下文，再返回由它生成的 HttpResponse 对象
    template = loader.get_template("polls/index.html")
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at quesiont %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at result of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on quesion %s." % question_id)

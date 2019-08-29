from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
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
    # 一个快捷函数： get_object_or_404()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    # 如果指定问题 ID 所对应的问题不存在，这个视图就会抛出一个 Http404 异常。
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("You're looking at result of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on quesion %s." % question_id)

from django.template.response import TemplateResponse
from django.http import HttpResponseNotFound
from django.views.generic import WeekArchiveView

from diary.models import Entry

def index(request):
    entries = Entry.objects.filter(user__id=request.user.id)
    context = {
        'entries': entries
    }
    return TemplateResponse(request, 'index.html', context=context)

def user_view(request, user_name):
    entries = Entry.objects.filter(user__username=user_name)
    if entries:
        context = {
            'entries': entries
        }
    else:
        return HttpResponseNotFound()
    return TemplateResponse(request, 'index.html', context=context)


class WeeklyView(WeekArchiveView):
    queryset = Entry.objects.all()
    date_field = "created"
    week_format = '%W'

weekly_view = WeeklyView.as_view()

def home(request):
    return TemplateResponse(request, 'home.html')

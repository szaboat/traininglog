from django.template.response import TemplateResponse
from diary.models import Entry

def index(request):
    entries = Entry.objects.filter(user__id=request.user.id)
    context = {
        'entries': entries
    }
    return TemplateResponse(request, 'index.html', context=context)

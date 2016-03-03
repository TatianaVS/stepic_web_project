from django.http import HttpResponse 

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def qid(request, q_id, *args, **kwargs):
    return HttpResponse("You're looking at question %s." % q_id)

import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    print(request.GET)
    body = request.body # byte string of Json data
    data = {}
    try:
        data = json.loads(body) # converts byte string Json data to python dictionary
    except:
        pass
    print(data)
    # data['headers'] = dict(request.headers)
    # data['method'] = request.method
    # data['user'] = dict(request.user)
    # data['auth'] = str(request.auth)
    # data['content_type'] = str(request.content_type)
    data['params'] = dict(request.GET)
    return JsonResponse(data)

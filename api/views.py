from django.shortcuts import render, Http404, HttpResponse
from django.shortcuts import render
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def update_information(request):
    if request.method == "POST":
        post = json.loads(request.body.decode("utf-8"))
        print(post)
        response_data = {}
        if post.get("key") == "70b66a89929e93416d2ef535893ea14da331da8991cc7c74010b4f3d7fabfd62":
            latitude = post['latitude']
            longitude = post['longitude']
            no = post['no']
            try:
                a = Information()
                a.latitude= latitude
                a.longitude= longitude
                a.no= no
                a.save()
                response_data['status'] = 'true'
            except Exception as e:
                    response_data['status'] = str(e)
                    print(e)

        else:
            response_data['status'] = 'Request Invalid'

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
    else:
        raise Http404("NOT ALLOWED")

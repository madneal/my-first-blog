import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def weixin_main(request):
    if request.method == "GET":
        signature = request.Get().get('signature', None)
        timestamp = request.Get().get('timestamp', None)
        nonce = request.Get().get('nonce', None)
        echostr = request.Get().get('echostr', None)

        token = "neal"
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist])
        hashstr = hashlib.sha1(hashstr).hexdigest()
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("field")




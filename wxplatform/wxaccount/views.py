from django.shortcuts import render


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import hashlib

from wechat.official import WxRequest, WxTextResponse

def checkSignature(request):
    signature=request.GET.get('signature',None)
    timestamp=request.GET.get('timestamp',None)
    nonce=request.GET.get('nonce',None)
    echostr=request.GET.get('echostr',None)
    #这里的token我放在setting，可以根据自己需求修改
    token='NHL28IPA'

    tmplist=[token,timestamp,nonce]
    tmplist.sort()
    tmpstr="%s%s%s"%tuple(tmplist)
    tmpstr=hashlib.sha1(tmpstr).hexdigest()
    if tmpstr==signature:
        return echostr
    else:
        return None


@csrf_exempt
def index(request):
    if request.method == 'GET':
        response = HttpResponse(checkSignature(request))
        return response
    else:
        resp = WxTextResponse("hello world", wxreq).as_xml()
        return resp

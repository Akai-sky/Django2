from django.http import HttpResponse
from captcha.views import CaptchaStore, captcha_image
from captcha.helpers import captcha_image_url
import base64
from rest_framework.views import APIView
import json
from captcha.fields import CaptchaField

class ImageView(APIView):
    def get(self, request):
        hashkey = CaptchaStore.generate_key()
        try:
            # 获取图片id
            id_ = CaptchaStore.objects.filter(hashkey=hashkey).first().id
            # image = captcha_image(request, hashkey)
            images_url = captcha_image_url(hashkey)
            print("images_url",images_url)
            # 将图片转换为base64
            # image_base = base64.b64encode(image.content)
            # json_data = json.dumps({"id": id_, "image_base": image_base.decode("utf-8")})
            json_data = json.dumps({"id": id_, "images_url": images_url})
        except:
            json_data = None
        return HttpResponse(json_data, content_type="application/json")

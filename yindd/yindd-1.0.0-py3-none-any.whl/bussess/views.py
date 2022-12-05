from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.sms_code import send_message
import string
import random
from captcha.image import ImageCaptcha
import redis
import jwt
from myapp.models import *
import time
from django.conf import settings
from utils.LoginTools import check_login
# Create your views here.
# 商家视图


# 图片验证码的视图
class ImageCodeAPIView(APIView):
    def get(self, request, uuid):
        # 生成一个4位数随机码
        # string.ascii_letters：a-zA-Z所有字母
        # string.digits：数字0-9
        # random.sample：随机采样(返回列表类型)
        code = "".join(random.sample(string.ascii_letters + string.digits, 4))
        # 实例化一个图片验证码对象
        # 用captcha.image下的 ImageCaptcha 生成字符验证码图片
        img = ImageCaptcha()
        # 把这个验证码转换成图片形式的
        image_code = img.generate(code)  # 字节io对象
        # 验证码存入redis
        redis_conn = redis.Redis(host="localhost", port=6379)
        redis_conn.set(uuid, code, ex=5 * 60)

        # 返回响应
        return HttpResponse(image_code, content_type="image/png")


# 获取验证码
class SmsView(APIView):
    def get(self,request,mobile):
        uuid = request.query_params.get('uuid')
        code = request.query_params.get('code')
        if not all([uuid,code]):
            return Response({
                'code':400,
                'msg':'获取数据为空'
            })
        print('>>>>>>>>>>',uuid,code)
        # 取出redis中uuid的值
        redis_conn = redis.Redis(host="localhost", port=6379)
        code_r = redis_conn.get(uuid)
        if not code_r:
            return Response({
                'code':400,
                'msg':'校验码已过期'
            })
        # 验证码还未过期，解码与前端对比
        if code_r.decode().lower() != code.lower():
            return Response({
                "code": 400,
                "msg": "校验码错误"
            })

        send_message(mobile)
        return Response({
            'code':200,
            'msg':'发送成功'
        })


# 手机验证码登入或注册
class UserView(APIView):
    def post(self,request):
        mobile = request.data.get('mobile')
        sms = request.data.get('sms')
        if not all([mobile,sms]):
            return Response({
                'code':400,
                'msg':'获取数据为空'
            })

        # 取出redis中uuid的值
        redis_conn = redis.Redis(host="localhost", port=6379)
        key = 'sms_%s' % mobile
        code_r = redis_conn.get(key)
        if not code_r:
            return Response({
                'code': 400,
                'msg': '验证码已过期'
            })
        # 验证码还未过期，解码与前端对比
        if code_r.decode().lower() != sms.lower():
            return Response({
                "code": 400,
                "msg": "验证码错误"
            })

        # 判断此手机号是否注册
        user = BussessModel.objects.filter(mobile=mobile)
        if not user:
            # 没有注册，进行注册
            BussessModel.objects.create(
                mobile=mobile,
            )
        try:
            user = BussessModel.objects.get(mobile=mobile)
        except Exception as e:
            return Response({
                'code':400,
                'msg':'没有此信息'
            })

        token = jwt.encode({
            'uid':user.id,
            'username':user.b_name,
            'exp':time.time() + 720000
        },key=settings.SECRET_KEY,algorithm='HS256')

        return Response({
            'code':200,
            'msg':'登入成功',
            'token':token
        })


# 对商品类别的增删改查  在平台操作
class ClassifyView(APIView):
    def get(self,request):
        # 获取所有分类
        food = FoodModel.objects.filter(delete=False)
        food_list = []
        for i in food:
            food_list.append({
                'cid':i.id,
                'name':i.name,
                'food_img':i.food_img,
            })

        return Response({
            'code':200,
            'msg':'获取分类商品成功',
            'data':food_list,
        })

    def post(self,request):
        name = request.data.get('name')
        img = request.data.get('img')
        pay_count = request.data.get('pay_count')
        cun_count = request.data.get('cun_count')
        price = request.data.get('price')
        verbose_name = request.data.get('verbose_name')
        if not all([img, name,pay_count,cun_count,price,verbose_name]):
            return Response({
                'code':400,
                'msg':'获取的数据为空'
            })

        # 唯一性判断
        food = FoodModel.objects.filter(name=name)
        if food:
            return Response({
                'code':400,
                'msg':'已有此分类'
            })

        FoodModel.objects.create(
            name=name,
            img=img,
            price=price,
            verbose_name=verbose_name,
            pay_count=pay_count,
            cun_count = cun_count
        )

        return Response({
            'code':200,
            'msg':"添加成功"
        })

# 商品的编辑获取删除
class ClassifyInfoView(APIView):
    def get(self,request,id):
        try:
            food = FoodModel.objects.get(id=id)
            return Response({
                'code':200,
                'msg':'获取成功',
                'data':{
                    "id":food.id,
                    'name':food.c_name,
                    'img':food.c_img,
                    "pay_count":food.pay_count,
                    'cun_count':food.cun_count,
                    "price":food.price,
                    'verbose_name':food.verbose_name
                }
            })
        except Exception as e:
            print(">?>>>>>",e)
            return Response({
                'code':400,
                'msg':'获取商品分类失败'
            })

    def put(self,request,id):
        # 获取前端数据
        name = request.data.get('name')
        img = request.data.get('img')
        pay_count = request.data.get('pay_count')
        cun_count = request.data.get('cun_count')
        price = request.data.get('price')
        verbose_name = request.data.get('verbose_name')

        if not all([img, name,pay_count,cun_count,price,verbose_name]):
            return Response({
                'code': 400,
                'msg': '获取的数据为空'
            })

        try:
            food = FoodModel.objects.get(id=id)
            food.name = name
            food.img = img
            food.pay_count = pay_count
            food.cun_count = cun_count
            food.price = price
            food.save()

            return Response({
                'code':200,
                'msg':'商品分类修改成功'
            })

        except Exception as e:
            print(">?>>>>>",e)
            return Response({
                'code':400,
                'msg':'获取商品分类失败'
            })

    def delete(self,request,id):
        try:
            food = FoodModel.objects.filter(id=id).delete()

            return Response({
                'code':200,
                'msg':'删除成功'
            })

        except Exception as e:
            print(">>>>>>>",e)
            return Response({
                'code':400,
                'msg':'没有此分类'
            })


class StatusView(APIView):
    @check_login
    def put(self,requst):
        id = requst.uid
        state = requst.data.get('state')
        data = BussessModel.objects.filter(id=id).update(state=state)
        return Response({
            'code':200,
            'msg':'修改成功'
        })







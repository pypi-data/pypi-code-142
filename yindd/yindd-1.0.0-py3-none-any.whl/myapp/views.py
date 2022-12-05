from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
import random
import json,time
import jwt
import redis
from utils.pay import AlipayTool
from utils.sms_code import send_message
from myapp.models import OrderModel
# Create your views here.
from django.conf import settings
class Sms_CodeView(APIView):
    def get(self, request):
        """生成短信验证码"""
        mobile = request.query_params.get('mobile')
        resp = send_message(mobile)
        print(resp)
        return Response({
            "code":200,
            "msg":"发送短信验证码成功"
        })

from  myapp.models import UserModel
from utils import myjwt

class LoginView(APIView):
    def post(self,request):
        mobile=request.data.get("mobile")
        code=request.data.get("code")

        print(mobile,"前端手机号")

        cls = redis.Redis()
        redis_data = cls.get("sms_%s"%mobile)
        print("数据库验证码",redis_data)


        if not redis_data  or redis_data.decode() !=code:
            return Response({
                "code":300,
                "msg":"验证码过期，或者不对"
            })
        user_info = UserModel.objects.filter(mobile=mobile).first()
        print('xxxxxxxxxxxxx',user_info)
        if not user_info:
            username1="用户"+mobile[-4:]

            UserModel.objects.create(username=username1,mobile=mobile,img="")

            user_info=UserModel.objects.get(username=username1,mobile=mobile)
            payload={
                    "id":user_info.id,
                    "name":user_info.username,
                    "mobile":user_info.mobile,
                }
            token=jwt.encode(payload=payload,key=settings.SECRET_KEY,algorithm='HS256')
            return Response({
                "code": 200,
                "msg": "登录成功",
                "data": token,
            })
        user_info = UserModel.objects.filter(mobile=mobile).first()
        payload = {
            "id": user_info.id,
            "name": user_info.username,
            "mobile": user_info.mobile,
        }
        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256')
        return Response({
            "code":200,
            "msg":"登录成功",
            "data":token,
        })

class LogoutView(APIView):
    def post(self,request):
        return Response({
            "code":200,
            "msg":"退出登录成功，请重新登录"
        })

from  utils.LoginTools import check_login
from myapp.models import AddressModel

class  ShowUser_address(APIView):
    @check_login
    def get(self,request):
        user=request.user
        user_addres=user.addressmodel_set()
        temp=[]
        for i in user_addres:
            temp_dict={
                "uid":i.id,
                "name":i.name,
                "phone":i.phone,
                "address":i.address,
                "is_mo":i.is_mo,
            }
            temp.append(temp_dict)
        return Response({
            "code":200,
            "msg":"获取登录用户收货地址成功",
            "data":temp,
        })

    @check_login
    def post(self,request):
        user_id = request.id
        name= request.data.get("name")
        phone= request.data.get("phone")
        address=request.data.get("address")
        is_mo=request.data.get("is_mo")

        try:
            AddressModel.objects.create(uid=user_id,name=name,phone=phone,address=address,is_mo=is_mo)
        except Exception as e:
            print(e,"用户添加收货地址报错")
        return Response({
            "code": 200,
            "msg": "添加登录用户收货地址成功",
        })
    @check_login
    def put(self,request):
        user_id=request.user

        id=request.data.get("id")
        name= request.data.get("name")
        phone= request.data.get("phone")
        address=request.data.get("address")
        is_mo=request.data.get("is_mo")

        try:
            AddressModel.objects.filter(id=id).update(name=name,phone=phone,address=address,is_mo=is_mo)
        except Exception as e:
            print(e,"用户修改收货地址报错")
        return Response({
                "code":200,
                "msg":"修改用户收货地址成功",
            })


from myapp.models import CouponModel
class  Showuser_Coupon(APIView):
    @check_login
    def get(self,request):
        id=request.id
        user_coup=CouponModel.objects.filter(uid=id).first()
        temp=[]

        for i in user_coup:
            temp_dict={
                "id":i.uid,
                "name":i.name,
                "price":i.price,
                "type":i.type,
                "start_time":i.start_time,
                "end_time": i.end_time,
                "time": i.time,
            }
            temp.append(temp_dict)
        return Response({
            "code":200,
            "msg":"获取用户优惠卷成功",
            "data":temp,
        })


from utils.qiniu_token import qiniu_token

class QNYtoken(APIView):
    def get(self,request):
        token=qiniu_token()
        return Response({
            "code":200,
            "token":token
        })

class Show_userInfo(APIView):
    @check_login
    def get(self,request):
        users_id = request.id
        users = UserModel.objects.filter(id=request.id)
        temp=[]
        for i in users:
            temp_dict={
                "id":i.id,
                "username":i.username,
                "mobile":i.mobile,
                "img" :i.img,
                "login_time":i.login_time,
                "intro":i.intro,
                "status":i.status,
                "time":time.strftime('%Y-%m-%d',time.localtime(int(i.vip_end_time)))
            }
            temp.append(temp_dict)
        return Response({
            "code":200,
            "msg":"获取登录用户信息成功",
            "data":temp,
        })
    @check_login
    def put(self,request):
        username=request.data.get("username")
        img=request.data.get("img")
        id=request.id

        try:
            UserModel.objects.filter(id=id).update(username=username,img=img)
        except Exception as e:
            print(e)
        return Response({
            "code":200,
            "msg":"修改登录用户信息成功"
        })

from myapp.models import VipListModel
class VipListView(APIView):
    def get(self,request):
        vip_list = VipListModel.objects.all()

        vip_all = []
        for item in vip_list:
            vip_all.append({
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "time_text": item.time_text,
                "time": item.time,
                "day_price": "%.2f" % (int(item.price) / (int(item.time) / 86400))
            })

        return Response({
            "code":200,
            "msg":"获取所有vip类型成功",
            "data":vip_all
        })


from datetime import datetime
from myapp.models import CategoryModel,FoodModel,BussessModel,PayOrderModel


class CateView(APIView):
    def get(self,request):
        data = CategoryModel.objects.all().order_by('-num')
        lst = []
        for i in data:
            lst.append({
                "id":i.id,
                'name':i.name,
                "num":i.num
            })
        return Response({
            "code":200,
            'msg':'获取成功',
            'data':lst
        })



class Add_OrderView(APIView):
    @check_login
    def get(self,request):
        user_id = request.id
        orders=PayOrderModel.objects.filter(uid=user_id).all()

        temp=[]
        all_price=[]
        for i in orders:

            all_price+=i.fid.price
            order_temp={
                "id":i.id,
                "order_num":i.order_num,
                "uid": i.uid,
                "bid=": i.bid,
                "fid": i.fid,
                "amount": i.amount,
                "status":i.status,
            }
            temp.append(order_temp)
        return Response({
            "code":200,
            "msg":"获取用户所有订单成功",
            "all_price": all_price,
        })

    @check_login
    def post(self,request):
        user_id = request.id
        bid = request.data.get("bid")
        fid = request.data.get("fid")

        # 生成订单号
        order_num = "T" + datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") + str(
            random.randint(100000, 999999)) + str(
            random.randint(100000, 999999))

        price=FoodModel.objects.filter(id=fid).first().price
        try:
            PayOrderModel.objects.create(uid=user_id,order_num =order_num,bid=bid,fid=fid,amount=price)
        except Exception as e:
            print(e,"生成未支付用户订单保存")
            return Response({
                "code": 305,
                "msg": "用户添加订单失败"
            })

        return Response({
            "code":200,
            "msg":"用户添加订单成功"
        })
    @check_login
    def delete(self,request):
        user_id = request.id
        id = request.data.get("id")
        try:
            ss=PayOrderModel.objects.filter(uid=user_id).filter(id=id).first()
            ss.delete()
        except Exception as e:
            print(e, "删除用户订单报错")
            return Response({
                "code": 305,
                "msg": "用户删除订单失败"
            })

        return Response({
            "code": 200,
            "msg": "用户删除订单成功"
        })
import time
from myapp.models import PayVipModel
class VipCreateView(APIView):
    @check_login
    def post(self,request):
        user_id = request.id
        u = UserModel.objects.get(id = user_id)
        vip_order_num = "T" + datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") + str(
            random.randint(100000, 999999)) + str(
            random.randint(100000, 999999))

        vid = request.data.get('id')
        amount = request.data.get('price')
        times = request.data.get('time')

        PayVipModel.objects.create(
            vip_order_num=vip_order_num,
            uid_id= user_id,
            vid_id=vid,
            amount=amount,
        )
        user_info = UserModel.objects.get(id=user_id)
        if user_info.vip_start_time== '':
            user_info.vip_start_time = int(time.time())
        if user_info.vip_end_time == '':
            user_info.vip_end_time = int(time.time()) + int(times)
        else:
            user_info.vip_end_time += int(times)
        user_info.status = 1
        user_info.save()
        with open("./keys/alipay_public_key.txt", "r", encoding="utf-8") as f:
            alipay_public_key = f.read()
            f.close()

        with open("./keys/private_key.txt", "r", encoding="utf-8") as f:
            private_key = f.read()
            f.close()
        from alipay import AliPay
        # 2. 实例化阿里的SDK
        alipay = AliPay(
            appid="2021000121639230",  # APPID 从 open.alipay.com 获取
            app_private_key_string=private_key,  # 使用密钥生成工具生成的
            alipay_public_key_string=alipay_public_key,  # 用我们自己生成的公钥，与支付宝官方换来的支付宝的公钥
            debug=True,  # 调试模式打开
        )
        urls = alipay.api_alipay_trade_page_pay(  # 此方法是用来网页支付的
            subject="支付订单 - %s" % u.username,  # 订单标题
            out_trade_no=vip_order_num,  # 我们自己平台的订单号
            total_amount=amount,  # 支付金额，字符串形式。精确到两位小数
            return_url="http://127.0.0.1:8000/api.wm/v1/user/pay_notify",  # 同步回调地址
            notify_url="https://www.baidu.com/",  # 异步回调地址,没有上线做不了，等上线后再说
        )
        url = "https://openapi.alipaydev.com/gateway.do?" + urls
        return Response({
            "code":200,
            "url": url,
        })


class Goods_PayView(APIView):
    @check_login
    def post(self,request):
        user_id = request.id
        data = request.data.get('vip')
        u = UserModel.objects.get(id=user_id)
        # 获取一下商品信息
        for i in data:
            OrderModel.objects.create(
                uid_id=i.uid,
                fid_id=i.fid,
                bid_id=i.bid,
                num = i.num
            )
        user_id = request.id
        money = request.data.get('money')
        # 生成订单号
        order_num = "T" + datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") + str(
            random.randint(100000, 999999)) + str(
            random.randint(100000, 999999))


        user_info = UserModel.objects.filter(id =user_id).first()
        if not user_info:
            return Response({
                "code":303,
                "msg":"用户未登录"
            })
        PayOrderModel.objects.create(
            order_num=order_num,
            amount=money,
            status="0"
        )

        with open("./keys/alipay_public_key.txt", "r", encoding="utf-8") as f:
            alipay_public_key = f.read()
            f.close()

        with open("./keys/private_key.txt", "r", encoding="utf-8") as f:
            private_key = f.read()
            f.close()
        from alipay import AliPay
        # 2. 实例化阿里的SDK
        alipay = AliPay(
            appid="2021000121639230",  # APPID 从 open.alipay.com 获取
            app_private_key_string=private_key,  # 使用密钥生成工具生成的
            alipay_public_key_string=alipay_public_key,  # 用我们自己生成的公钥，与支付宝官方换来的支付宝的公钥
            debug=True,  # 调试模式打开
        )
        urls = alipay.api_alipay_trade_page_pay(  # 此方法是用来网页支付的
            subject="支付订单 - %s" % u.username,  # 订单标题
            out_trade_no=order_num,  # 我们自己平台的订单号
            total_amount=money,  # 支付金额，字符串形式。精确到两位小数
            return_url="http://127.0.0.1:8000/api.wm/v1/user/pay_notify",  # 同步回调地址
            notify_url="https://www.baidu.com/",  # 异步回调地址,没有上线做不了，等上线后再说
        )
        url = "https://openapi.alipaydev.com/gateway.do?" + urls
        return Response({
            "code":200,
            "url": url,
        })


class PayNotifyView(APIView):
    def get(self,request):
        """接收同步地址回调"""
        args = request.query_params
        num = args.get('out_trade_no')
        print(type(num))

        # 因为是get请求，且地址啥的都是公开的。为了保证安全性，需要对回调数据进行校验
        # 把订单的状态改为已支
        order = PayOrderModel.objects.filter(order_num = str(num)).first()
        vip = PayVipModel.objects.filter(vip_order_num= str(num)).first()
        if order:
            print('xxxxxxx',order)
            if order.status == '0':
                order.status = '1'
                order.save()
        elif vip:
            if vip.status == '0':
                vip.status = '1'
                vip.save()
        else:
            return Response({
                'code':400,
                'msg':'订单状态不允许'
            })
        return redirect("http://localhost:8080/home")


class OrderRecordView(APIView):
    @check_login
    def get(self,request):
        user_id =request.id
        order_list = PayVipModel.objects.filter(uid_id=user_id).all()
        order_all = []
        lst = []
        for item in order_list:
            data = OrderModel.objects.filter(oid_id=item.id).all()
            for i in data:
                lst.append({
                    "bid":i.bid_id,
                    'fid':i.fid.name,
                    'food_img':i.fid.food_img,
                    'num':i.num,
                    'price':i.fid.price
                })
            order_all.append({
                "order_num": item.oid.order_num,
                "amount": item.oid.amount,
                "status": item.oid.status,
                'data':lst
            })

        return Response({
            "code":200,
            "msg":"获取支付记录成功",
            "data":order_all
        })

class VipAllView(APIView):
    @check_login
    def get(self,request):
        user_id = request.id
        data = PayVipModel.objects.filter(uid_id=user_id).all()
        lst = []
        for i in data:
            lst.append({
                'id':i.id,
                "vip_order_num":i.vip_order_num,
                "vid_text":i.vid.time_text,
                "amount":i.amount,
                "status":i.status,
                'name':i.vid.name
            })
        return Response({
            'code':200,
            'msg':'获取成功',
            'data':lst
        })
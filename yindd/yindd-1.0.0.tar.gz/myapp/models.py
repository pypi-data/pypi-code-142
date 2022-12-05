# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
# 用户表
class UserModel(models.Model):
    username=models.CharField(max_length=32,verbose_name="用户名",unique=True)
    mobile = models.CharField(max_length=16,verbose_name="手机号",unique=True)
    img = models.CharField(max_length=256, verbose_name="头像")
    login_time = models.DateTimeField(default=datetime.now,verbose_name="登录时间")
    reg_time= models.DateTimeField(default=datetime.now,verbose_name="注册时间")
    intro = models.CharField(max_length=256,default="这个人懒，什么也没写",verbose_name="用户简介")
    vip_start_time = models.CharField(max_length=56,default='', verbose_name="vip开始时间")
    vip_end_time = models.CharField(max_length=56,default='', verbose_name="vip结束时间")
    status=models.CharField(max_length=32,default=0,verbose_name="是否冻结 0 不冻结 1 冻结")
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'user_model'

# vip类型表
class VipListModel(models.Model):
    name=models.CharField(max_length=56,verbose_name="VIP名字")
    price=models.CharField(max_length=16,default=0,verbose_name="价格")
    time_text=models.CharField(max_length=124,default="",verbose_name="有效期")
    time=models.CharField(max_length=56,default=0,verbose_name="有效期（s）")
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'vip_list_model'
# 购买vip表
class PayVipModel(models.Model):
    vip_order_num = models.CharField(max_length=555,default="", verbose_name="订单号")
    uid = models.ForeignKey(to=UserModel,on_delete=models.CASCADE,verbose_name="用户id")
    vid = models.ForeignKey(to=VipListModel,on_delete=models.CASCADE,verbose_name="vip类型id")
    amount = models.CharField(max_length=16,verbose_name="支付金额")
    status = models.CharField(max_length=16,default=0, verbose_name="订单状态  0 待支付  1已支付  2 已取消")
    def __str__(self):
        return self.vip_order_num
    class Meta:
        db_table = 'pay_vip_model'



# 商家分类表
class CategoryModel(models.Model):
    name = models.CharField(max_length=56,default="",verbose_name="分类名")
    num = models.CharField(max_length=16, default=0,verbose_name="排序，数字越小越靠前")
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'category_model'

# 商家表
class BussessModel(models.Model):
    title = models.CharField(max_length=56,default="",verbose_name="商家名称")
    cid = models.ForeignKey(to=CategoryModel,on_delete=models.CASCADE,verbose_name="商家所属分类")
    img = models.CharField(max_length=256, default="",verbose_name="商家封面")
    start_time = models.CharField(max_length=56, default="", verbose_name="营业时间")
    address = models.CharField(max_length=124, default="",verbose_name="商家地址")
    phone= models.CharField(max_length=16,verbose_name="商家电话")
    fen=models.CharField(max_length=56, default="",verbose_name="商家评分")
    state = models.CharField(max_length=16, default=0, verbose_name="营业状态 0 下线 1上线")
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'bussess_model'

# 商家菜品表
class FoodModel(models.Model):
    b_id = models.ForeignKey(to=BussessModel, on_delete=models.CASCADE, verbose_name="所属商家")
    name = models.CharField(max_length=56,default="",verbose_name="菜品名")
    food_img = models.CharField( max_length=256, verbose_name="菜品图")
    price = models.CharField(max_length=16,verbose_name="商品价格")
    verbose_name=models.CharField(max_length=124,verbose_name="菜品评价")
    pay_count=models.CharField(max_length=16,verbose_name="菜品销量")
    cun_count = models.CharField(max_length=16,verbose_name="菜品库存量")
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'food_model'

# 用户收货地址表
class AddressModel(models.Model):
    uid=models.ForeignKey(to=UserModel,on_delete=models.CASCADE,verbose_name="收货用户")
    name=models.CharField(max_length=24,verbose_name="收货人姓名")
    phone=models.CharField(max_length=16,verbose_name="收货人电话")
    address=models.CharField(max_length=256,verbose_name="收货地址")
    is_mo=models.CharField(max_length=4,default=0,verbose_name="1为默认地址，0为不默认")
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'address_model'

# 用户优惠卷表
class CouponModel(models.Model):
    uid=models.ForeignKey(to=UserModel,on_delete=models.CASCADE,verbose_name="优惠卷用户")
    name=models.CharField(max_length=56,verbose_name="优惠卷名")
    price=models.CharField(max_length=16,verbose_name="优惠卷金额")
    type=models.CharField(max_length=56,verbose_name="优惠卷类型")
    start_time = models.DateTimeField(default=datetime.now, verbose_name="开始时间")
    end_time = models.DateTimeField(default=datetime.now, verbose_name="结束时间")
    time = models.CharField(max_length=56, default=0, verbose_name="有效期（s）")
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'coupon_model'

# 用户订单表
class PayOrderModel(models.Model):
    uid = models.ForeignKey(to=UserModel, on_delete=models.CASCADE, verbose_name="用户id")
    order_num = models.CharField(max_length=56, default="",verbose_name='订单号')
    amount = models.CharField(max_length=16, default=0, verbose_name="支付金额")
    status = models.CharField(max_length=16, default=0,verbose_name="订单状态  0 待支付  1已支付  2 已取消")
    def __str__(self):
        return self.order_num
    class Meta:
        db_table = 'pay_order_model'

class OrderModel(models.Model):
    bid = models.ForeignKey(to=BussessModel, on_delete=models.CASCADE, verbose_name="订单商家id")
    fid = models.ForeignKey(to=FoodModel, on_delete=models.CASCADE, verbose_name="菜品id")
    oid = models.ForeignKey(to=PayOrderModel,on_delete=models.CASCADE,verbose_name='订单ID')
    num = models.IntegerField(verbose_name='数量')
    class Meta:
        db_table = 'order_model'

# 商家评论表
class CommentModel(models.Model):
    user_id = models.ForeignKey(to=UserModel,on_delete=models.CASCADE,verbose_name="用户id")
    buss_id = models.ForeignKey(to=BussessModel,on_delete=models.CASCADE,verbose_name="商家id")
    context = models.CharField(max_length=256, default="",verbose_name="评论内容")
    parent_id = models.IntegerField(default=0,verbose_name="回复的评论ID")
    root_id = models.IntegerField(default=0,verbose_name="回复的评论根ID")
    def __str__(self):
        return self.context
    class Meta:
        db_table = 'comment_model'

#骑手表
class RiderModel(models.Model):
    r_name = models.CharField(max_length=32, verbose_name="用户名", unique=True)
    mobile = models.CharField(max_length=16, verbose_name="手机号", unique=True)
    img = models.CharField(max_length=256, verbose_name="头像")
    login_time = models.DateTimeField(default=datetime.now, verbose_name="登录时间")
    reg_time = models.DateTimeField(default=datetime.now, verbose_name="注册时间")
    intro = models.CharField(max_length=256, default="这个人懒，什么也没写", verbose_name="用户简介")
    status = models.CharField(max_length=32,default=0, verbose_name="是否上线 0 下线 1上线")
    def __str__(self):
        return self.r_name
    class Meta:
        db_table = 'rider_model'

#抢单大厅
class OrderLobbyModel(models.Model):
    o_id = models.ForeignKey(to=PayOrderModel,on_delete=models.CASCADE,verbose_name='订单ID')
    status = models.CharField(max_length=16,default=0,verbose_name='0 待抢单，1 已抢单')
    def __str__(self):
        return self.status
    class Meta:
        db_table = 'order_lobby_model'
#骑手订单表
class RiderOrderModel(models.Model):
    order_id = models.ForeignKey(to=OrderLobbyModel,on_delete=models.CASCADE,verbose_name='订单ID')
    status = models.CharField(max_length=16,default=0,verbose_name='0 接单 1 完成订单 2 转让订单')
    def __str__(self):
        return self.status
    class Meta:
        db_table = 'rider_order_model'























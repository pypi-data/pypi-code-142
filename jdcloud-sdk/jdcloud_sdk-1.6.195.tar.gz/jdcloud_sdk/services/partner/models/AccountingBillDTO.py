# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class AccountingBillDTO(object):

    def __init__(self, source=None, recordId=None, pin=None, appCode=None, serviceCode=None, productId=None, site=None, resourceId=None, region=None, billingType=None, formulaList=None, billFee2=None, discountFee=None, actualFee=None, cashCouponId=None, cashCouponFee=None, payCouponFee=None, freeCouponFee=None, balancePayFee=None, cashPayFee=None, performanceFee=None, billTime=None, billPayTime=None, billBeginTime=None, billEndTime=None, distributorPin=None, distributorType=None, transactionNo=None, mainTransactionNo=None, refundNo=None, opType=None, code=None, message=None):
        """
        :param source: (Optional) 产品类型
        :param recordId: (Optional) 记录ID
        :param pin: (Optional) 用户pin
        :param appCode: (Optional) 业务线
        :param serviceCode: (Optional) 产品线
        :param productId: (Optional) 产品ID
        :param site: (Optional) 站点  0:主站  其他:专有云
        :param resourceId: (Optional) 资源id
        :param region: (Optional) 区域
        :param billingType: (Optional) 计费类型
        :param formulaList: (Optional) 配置列表
        :param billFee2: (Optional) 费用
        :param discountFee: (Optional) 折扣金额
        :param actualFee: (Optional) 优惠后金额
        :param cashCouponId: (Optional) 代金券唯一标识
        :param cashCouponFee: (Optional) 代金券金额
        :param payCouponFee: (Optional) 付费代金券金额
        :param freeCouponFee: (Optional) 免费代金券金额
        :param balancePayFee: (Optional) 余额支付金额
        :param cashPayFee: (Optional) 在线支付金额
        :param performanceFee: (Optional) 业绩金额
        :param billTime: (Optional) 账单时间
        :param billPayTime: (Optional) 账单支付时间
        :param billBeginTime: (Optional) 账单开始时间
        :param billEndTime: (Optional) 账单结束时间
        :param distributorPin: (Optional) 服务商pin
        :param distributorType: (Optional) 服务商类型
        :param transactionNo: (Optional) 子订单号
        :param mainTransactionNo: (Optional) 订单号
        :param refundNo: (Optional) 退款单号
        :param opType: (Optional) 操作类型
        :param code: (Optional) 返回编码0成功-1失败
        :param message: (Optional) 返回消息
        """

        self.source = source
        self.recordId = recordId
        self.pin = pin
        self.appCode = appCode
        self.serviceCode = serviceCode
        self.productId = productId
        self.site = site
        self.resourceId = resourceId
        self.region = region
        self.billingType = billingType
        self.formulaList = formulaList
        self.billFee2 = billFee2
        self.discountFee = discountFee
        self.actualFee = actualFee
        self.cashCouponId = cashCouponId
        self.cashCouponFee = cashCouponFee
        self.payCouponFee = payCouponFee
        self.freeCouponFee = freeCouponFee
        self.balancePayFee = balancePayFee
        self.cashPayFee = cashPayFee
        self.performanceFee = performanceFee
        self.billTime = billTime
        self.billPayTime = billPayTime
        self.billBeginTime = billBeginTime
        self.billEndTime = billEndTime
        self.distributorPin = distributorPin
        self.distributorType = distributorType
        self.transactionNo = transactionNo
        self.mainTransactionNo = mainTransactionNo
        self.refundNo = refundNo
        self.opType = opType
        self.code = code
        self.message = message

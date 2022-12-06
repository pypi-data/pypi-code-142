from django.db import models
from ..utils import time_now, settings
from .utils import RateTime, Block


class RateLimit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    count = models.IntegerField(default=0)
    blocked = models.BooleanField(default=False)
    blocked_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Rate Limit'
        verbose_name_plural = 'Rate Limits'

    def __str__(self):
        if self.user:
            return self.user.username
        return self.ip


class RateLimitManager:

    def __init__(self, model):
        self.model = getattr(model, "model")

    def count(self, user_or_ip):
        model = self.get(user_or_ip)
        model.count += 1
        model.save()

    def get(self, user_or_ip):
        if self.model == "user":
            try:
                return RateLimit.objects.get(user=user_or_ip)
            except RateLimit.DoesNotExist:
                r_l = RateLimit()
                r_l.user = user_or_ip
                r_l.save()
                return r_l
        elif self.model == "ip":
            try:
                return RateLimit.objects.get(ip=user_or_ip)
            except RateLimit.DoesNotExist:
                r_l = RateLimit()
                r_l.ip = user_or_ip
                r_l.save()
                return r_l

    def delete(self, model):
        model.delete()

    def check_rate_limit(self, user_or_ip, rate_time: RateTime, block: Block):
        rate_time.check()
        rate_limit = self.get(user_or_ip)
        if rate_limit.blocked:
            if time_now() - rate_limit.blocked_at > block.time():
                rate_limit.delete()
            else:
                return False
        else:
            if time_now() - rate_limit.created_at > rate_time.time():
                self.delete(rate_limit)
            else:
                if rate_limit.count >= rate_time.count:
                    if block.active:
                        rate_limit.blocked = True
                        rate_limit.blocked_at = time_now()
                        rate_limit.save()
                    return False
        return True

    def check(self, user_or_ip, rate_time: RateTime, block: Block):
        if self.check_rate_limit(user_or_ip, rate_time, block):
            self.count(user_or_ip)
            return True
        return False


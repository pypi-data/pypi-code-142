# encoding: utf-8
"""
@project: djangoModel->regin_service
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis:
@created_time: 2022/6/10 16:08
"""
import json
import time
import uuid

from django_redis import get_redis_connection

from ..models import Region
from ..services.public_service import parse_model


class RegionService():
    def cn_parse_location_code(self, region_code):
        # 中国行政编码解析 province{2},city(2),district(2),town(3),village(3)三位
        # level？ province ==>>village : 1 ===>> 5
        if not region_code or not len(str(region_code)) == 12:
            return None
        location = {}
        region_code = str(region_code)
        location['province'] = self.get_region_info(region_code[0:2] + "0000000000")

        city = self.get_region_info(region_code[0:4] + "00000000")
        location['city'] = city if not city == location['province'] else None

        district = self.get_region_info(region_code[0:6] + "000000")
        location['district'] = district if not district == city else None

        town = self.get_region_info(region_code[0:9] + "000")
        location['town'] = town if not town == district else None

        village = self.get_region_info(region_code[0:])
        location['village'] = village if not town == village else None

        return location

    def get_region_info(self, code):
        # 查询对应的名称
        json_data = parse_model(Region.objects.filter(code=code, is_delete=0))
        if not json_data:
            return None
        else:
            return json_data

    def tree_loop(self, p_code=0, level=1):
        # 树形数据遍历
        first_level = parse_model(Region.objects.filter(level=level, is_delete=0, p_code=p_code), True)
        if first_level:
            for j in first_level:
                j['child'] = self.tree_loop(j['code'], j['level'] + 1)
        return first_level

    def tree_lock_loop(self):
        # redis 分布式锁 TODO 守护进程防止锁超时和死锁
        conn = get_redis_connection()
        region_tree = conn.get('region_tree')
        if not region_tree:  # 不存在缓存的时候
            # 当缓存失效的时候需要使用redis 锁进行阻塞，防止雪崩现象
            lock = conn.get('region_tree_lock')
            if not lock:  # 未加锁时候
                lock_key = uuid.getnode()
                conn.set('region_tree_lock', lock_key)
                conn.expire('region_tree_lock', 3)
                region_tree = self.tree_loop()
                conn.set('region_tree', json.dumps(region_tree))
                conn.delete('region_tree_lock')
            else:  # 已经被枷锁，进行自旋
                times = 0
                while True:
                    region_tree = conn.get('region_tree')
                    if not region_tree is None:
                        region_tree = json.loads(region_tree)
                        break
                    if times > 6:
                        lock = conn.get('region_tree_lock')
                        if not lock:
                            self.tree_lock_loop()
                        return None
                    times += 1
                    time.sleep(0.5)
        else:  # 存在缓存之恶返回
            region_tree = json.loads(region_tree)
        return region_tree

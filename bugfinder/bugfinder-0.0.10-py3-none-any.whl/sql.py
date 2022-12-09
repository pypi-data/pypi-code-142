#!/usr/bin/env python
import aiomysql

async def create_pool():
    from bugfinder.auth import auth as acc
    return await aiomysql.create_pool(
        host=acc.host,
        port=3306,
        user=acc.user,
        password=acc.password,
        db=acc.db,
    )

dbname = 'kvpair'

async def exec(cmd: str):
    pool = await create_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(cmd)
            resp = await cur.fetchall()
            return resp


async def load_data(key:str, limits:int=10000):
    pool = await create_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                "SELECT * FROM {} WHERE `key` = '{}' ORDER BY `id` DESC LIMIT {}".format(dbname, key, limits))
            resp = await cur.fetchall() 
            return resp


async def delete_old_than_hours(hours:int=1):
    pool = await create_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            cmd = 'DELETE FROM {} WHERE `create_time` < DATE_SUB(NOW(), INTERVAL {} HOUR)'.format(dbname, hours)
            resp = await cur.execute(cmd)
            await conn.commit()
            return resp

async def insert_once(key: str, value: str):
    pool = await create_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            cmd = 'INSERT INTO {} (`key`, `value`) VALUES ("{}", "{}") ON DUPLICATE KEY UPDATE `value` = "{}"'.format(dbname, key, value, value)
            resp = await cur.execute(cmd)
            await conn.commit()
            return resp

async def insert_many(data: dict):
    pool = await create_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            if not data:
                return None
            cmd = 'INSERT INTO {} (`key`, `value`) VALUES '.format(dbname)
            for k, v in data.items():
                cmd += '("{}", "{}"),'.format(k, v)
            cmd = cmd[:-1]
            cmd += ' ON DUPLICATE KEY UPDATE `value` = VALUES(`value`)'
            resp = await cur.execute(cmd)
            await conn.commit()
            return resp


async def insert_many_local(data: dict):
    # For backup only
    pool = await aiomysql.create_pool(
        host="127.0.0.1",
        port=3306,
        user='root',
        password=acc.local_sql_password,
        db='mysql'
    )

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            if not data:
                return None
            cmd = 'INSERT INTO {} (`key`, `value`) VALUES '.format(dbname)
            for k, v in data.items():
                cmd += '("{}", "{}"),'.format(k, v)
            cmd = cmd[:-1]
            cmd += ' ON DUPLICATE KEY UPDATE `value` = VALUES(`value`)'
            resp = await cur.execute(cmd)
            await conn.commit()
            return resp

                        
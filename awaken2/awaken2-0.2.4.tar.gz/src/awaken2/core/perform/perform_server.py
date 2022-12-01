# Copyright 2022 quinn.7@foxmail.com All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
服务执行池

"""
import gc
import psutil

from tornado.ioloop import IOLoop
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer

from .pool_runtime import POOL_RUNTIME
from ...baseic.keyword import G_KEYWORD
from ...baseic.common.configure import G_CONFIGURE
from ...baseic.broadcast.awaken_log import G_LOG
from ...server.api.awaken_app import AwakenApp
from ...kit.engine_agency import EngineAgency
from ...baseic.structural.interpreter import AwakenTask


# --------------------------------------------------------------------------
class PerformServer(object):
    """
    [ 执行服务 ]

    ---
    描述
    - 开启时, 将在本地挂起一个执行池进程与 WebAPI 服务。

    """
    _debug: bool
    """ 调试模式 """


    # ----------------------------------------------------------------------
    def running(self, 
        port: int = 3700, 
        debug: bool = G_CONFIGURE.get(G_KEYWORD.Common.Config.Debug)
    ):
        """
        [ 运行 ]

        ---
        参数:
        - port  : { int }  - 服务端口号, 默认为 3700。
        - debug : { bool } - 调试模式。

        """
        self._debug = debug
        POOL_RUNTIME.pool.apply_async(func=self.monitor)
        
        app = AwakenApp()
        http_server = HTTPServer(WSGIContainer(app.living))
        http_server.listen(port)

        if self._debug:
            G_LOG.info(f'执行服务运行中 >> 端口号 :: [ {str(port)} ] !')

        IOLoop.current().start()


    # ----------------------------------------------------------------------
    def monitor(self):
        """
        [ 监听进程 ]
        
        ---
        描述
        - 监听来自 POOL 运行时的队列信息。

        """
        if self._debug:
            G_LOG.info('监听进程已启动 ...')

        while True:
            # --------------------------------------------------------------
            # 调用多进程执行任务
            # 驱动冷启动时会占用大量的 CPU 资源, 为避免因为 CPU 占用率过高导致进程启动异常
            # 每隔 X 秒检查 CPU 占用率, 只有 CPU 占用率少于 X 时才会启动进程
            # --------------------------------------------------------------
            task = POOL_RUNTIME.task_queue.get()
            engine = POOL_RUNTIME.engine_queue.get()
            while True:
                if psutil.cpu_percent(G_CONFIGURE.get(G_KEYWORD.Common.Config.CpuPropertyTime)) <= G_CONFIGURE.get(G_KEYWORD.Common.Config.CpuPropertyCeiling):
                    POOL_RUNTIME.pool.apply_async(func=self._emit, args=[task, engine])
                    break


    # ----------------------------------------------------------------------
    def _emit(self, task: AwakenTask, engine: EngineAgency):
        """
        [ 触发工作流 ]
        
        ---
        参数:
            task   : { AwakenTask }   - 任务对象。
            engine : { EngineAgency } - 驱动对象。

        """
        # 核心执行任务
        engine.start(task)
        # 核心执行完任务后, 放回核心队列等待
        POOL_RUNTIME.engine_queue.put(engine)
        # 强制 GC 回收垃圾避免内存溢出
        gc.collect()

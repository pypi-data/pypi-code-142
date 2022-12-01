#!/usr/bin/env python3.7
import sys
import logging
import uvloop
import asyncio
from quality_estimation.engine import quality_estimation 
from aiohttp import web



asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class QualityEstimationServer:

    def __init__(self):
        self._app = web.Application()
        self._app.router.add_post("/quality_estimation", quality_estimation_server)
        
    def start(self, port: int):
        web.run_app(self._app, port=port)

async def quality_estimation_server(req):

    try:
        req = await req.json()
        srcs = req.get("srcs")
        tgts = req.get("tgts")
        # print(srcs,tgts)
        pred_scores = quality_estimation(srcs, tgts).tolist()
        print(pred_scores)
        ans = {'pred_scores':pred_scores}
        # if mode == 'EUROPEANA':
        #     for txt,label,score in zip(batch, pred_labels, pred_scores):
        #         ans['detected_langs'].append({'src_detected':label,'src_lang_score':score})
        # else:
        #     ans = {'src_detected':pred_labels,'src_lang_score':pred_scores}

        return web.json_response(ans, status=200)

    except Exception as e:
        logging.exception(str(e))
        response_obj = {'status': 'failed', 'reason': str(e)}
        return web.json_response(response_obj, status=500)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2:
        print("Three arguments needed: ")
        print("config and port")
    else:
        try:
            server = QualityEstimationServer(args[0])
            server.start(int(args[1]))
        except Exception as e:
            logging.exception(str(e))
            raise Exception("Error") from e

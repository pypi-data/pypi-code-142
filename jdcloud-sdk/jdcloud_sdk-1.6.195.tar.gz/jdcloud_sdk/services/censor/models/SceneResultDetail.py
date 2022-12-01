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


class SceneResultDetail(object):

    def __init__(self, sceneName=None, rate=None):
        """
        :param sceneName: (Optional) 场景名字，不可识别则为空.目前识别场景包含游戏画面(game)、卡通动漫(cartoon)、海滩湖泊(sea)、泳池(pool)、健身场所(gym)、绘画作品(painting)
        :param rate: (Optional) 置信度分数，0-1之间取值，1为置信度最高，0为置信度最低
        """

        self.sceneName = sceneName
        self.rate = rate

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
WEB驱动引擎方法映射

"""
import re

from .web_engine import WebEngine


WEB_ENGINE_TYPE = type(WebEngine())
WEB_ENGINE_FUNCTION_MAP = {}

for fn, fv in WEB_ENGINE_TYPE.__dict__.items():
    if fn[0] != '_':
        fn = ''.join([n.title() for n in fn.rsplit('_')])
        cn_fn = re.findall(r'\[ (.*) \]', fv.__doc__)[0]
        WEB_ENGINE_FUNCTION_MAP.update({fn:fv})
        WEB_ENGINE_FUNCTION_MAP.update({cn_fn:fv})


# --------------------------------------------------------------------------
WEB_INSTRUCTIONS = [
    {
        'title': '浏览器',
        'list': [
            {
                'type': 'Instructions',
                'name': '页面跳转',
                'help': '跳转至指向的 URL 网站。',
                'drivingCharacter': 'Goto',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': 'URL',
                        'help': '需要访问的 URL 路径。',
                        'key': 'url',
                        'value': 'https://www.baidu.com/',
                    }
                ],
                'whetherThereReturn': False,
            },
            {
                'type': 'Instructions',
                'name': '页面刷新',
                'help': '浏览器刷新当前页面。',
                'drivingCharacter': 'Reload',
                'drivingParameter': [],
                'whetherThereReturn': False,
            },
            {
                'type': 'Instructions',
                'name': '页面回退',
                'help': '浏览器回退到上一页。',
                'drivingCharacter': 'Back',
                'drivingParameter': [],
                'whetherThereReturn': False,
            },
            {
                'type': 'Instructions',
                'name': '页面前进',
                'help': '浏览器前进到下一页。',
                'drivingCharacter': 'Forward',
                'drivingParameter': [],
                'whetherThereReturn': False,
            },
            {
                'type': 'Instructions',
                'name': '获取页面名称',
                'help': '获取当前页面中的 Title 属性。',
                'drivingCharacter': 'GetPageName',
                'drivingParameter': [],
                'whetherThereReturn': True,
                'namespaceScope': 'UNIVERSE',
                'namespaceKey': '',
            },
            {
                'type': 'Instructions',
                'name': '重置上下文',
                'help': '重启浏览器并清除上下文缓存。',
                'drivingCharacter': 'NewContext',
                'drivingParameter': [],
                'whetherThereReturn': False,
            },
            {
                'type': 'Instructions',
                'name': '设置浏览器尺寸',
                'help': '设置当前浏览器的窗口尺寸。',
                'drivingCharacter': 'SetWindowSize',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '宽度',
                        'help': '浏览器宽度。',
                        'key': 'width',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '高度',
                        'help': '浏览器高度。',
                        'key': 'height',
                        'value': '',
                    }
                ],
                'whetherThereReturn': False,
            },
        ],
    },
    {
        'title': '鼠标操作',
        'list': [
            {
                'type': 'Instructions',
                'name': '鼠标单击',
                'help': '模拟鼠标进行单击元素操作。',
                'drivingCharacter': 'Click',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '元素选择器',
                        'help': '元素选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid',
                        'value': '1',
                    }
                ],
                'whetherThereReturn': False,
            },
            {
                'type': 'Instructions',
                'name': '鼠标双击',
                'help': '模拟鼠标进行双击元素操作。',
                'drivingCharacter': 'DblClick',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '元素选择器',
                        'help': '元素选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid',
                        'value': '1',
                    }
                ],
                'whetherThereReturn': False,
            },
            {
                'type': 'Instructions',
                'name': '鼠标悬停',
                'help': '模拟鼠标悬停在元素上。',
                'drivingCharacter': 'Hover',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '悬停秒数',
                        'help': '悬停等待时长。',
                        'key': 'wait',
                        'value': '1',
                    },
                    {
                        'type': 'Input',
                        'name': '元素选择器',
                        'help': '元素选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid',
                        'value': '1',
                    }
                ],
                'whetherThereReturn': False,
            },
            {
                'type': 'Instructions',
                'name': '鼠标拖拽',
                'help': '模拟鼠标拖拽行为, 将元素1拖拽至元素2, 然后松开鼠标。',
                'drivingCharacter': 'DragTo',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '元素1选择器',
                        'help': '元素1选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element1',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素1下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid1',
                        'value': '1',
                    },
                    {
                        'type': 'Input',
                        'name': '元素选择器2',
                        'help': '元素选择器2, 允许 selector 或 XPath 定位。',
                        'key': 'element2',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素2下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid2',
                        'value': '1',
                    }
                ],
                'whetherThereReturn': False,
            },
        ],
    },
    {
        'title': '通用元素',
        'list': [
            {
                'type': 'Instructions',
                'name': '获取元素数量',
                'help': '获取当前页面中定位元素的数量。',
                'drivingCharacter': 'GetElementCount',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '元素选择器',
                        'help': '元素选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element',
                        'value': '',
                    }
                ],
                'whetherThereReturn': True,
                'namespaceScope': 'UNIVERSE',
                'namespaceKey': '',
            },
            {
                'type': 'Instructions',
                'name': '获取元素文本',
                'help': '获取当前页面中定位元素的文本。',
                'drivingCharacter': 'GetElementText',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '元素选择器',
                        'help': '元素选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid',
                        'value': '1',
                    }
                ],
                'whetherThereReturn': True,
                'namespaceScope': 'UNIVERSE',
                'namespaceKey': '',
            },
            {
                'type': 'Instructions',
                'name': '获取元素属性值',
                'help': '获取输入框控件中输入的值。',
                'drivingCharacter': 'GetAttribute',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '属性名',
                        'help': '需获取值的属性名称。',
                        'key': 'name',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素选择器',
                        'help': '元素选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid',
                        'value': '1',
                    }
                ],
                'whetherThereReturn': True,
                'namespaceScope': 'UNIVERSE',
                'namespaceKey': '',
            },
        ]
    },
    {
        'title': '输入框控件',
        'list': [
            {
                'type': 'Instructions',
                'name': '输入框输入',
                'help': '该函数期望的目标控件是 Input 类型',
                'drivingCharacter': 'Send',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '文本',
                        'help': '输入的值。',
                        'key': 'key',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素选择器',
                        'help': '元素选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid',
                        'value': '1',
                    }
                ],
                'whetherThereReturn': False,
            },
            {
                'type': 'Instructions',
                'name': '获取输入框的值',
                'help': '获取输入框控件中输入的值。',
                'drivingCharacter': 'GetInputValue',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '元素选择器',
                        'help': '元素选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid',
                        'value': '1',
                    }
                ],
                'whetherThereReturn': True,
                'namespaceScope': 'UNIVERSE',
                'namespaceKey': '',
            },
        ],
    },
    {
        'title': '弹窗控件',
        'list': [
            {
                'type': 'Instructions',
                'name': '弹窗确定',
                'help': '点击一个绑定了弹窗事件的按钮元素, 然后静默确认该弹窗。',
                'drivingCharacter': 'PopupOk',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '元素选择器',
                        'help': '元素选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid',
                        'value': '1',
                    },
                    {
                        'type': 'Input',
                        'name': '填充文本',
                        'help': '如果该弹窗存在输入框, 可通过参数 text 来填充。',
                        'key': 'text',
                        'value': '',
                    }
                ],
                'whetherThereReturn': False,
            },
            {
                'type': 'Instructions',
                'name': '弹窗取消',
                'help': '点击一个绑定了弹窗事件的按钮元素, 然后静默取消该弹窗。',
                'drivingCharacter': 'PopupNo',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '元素选择器',
                        'help': '元素选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid',
                        'value': '1',
                    },
                ],
                'whetherThereReturn': False,
            },
        ],
    },
    {
        'title': '其他',
        'list': [
            {
                'type': 'Instructions',
                'name': '上传文件',
                'help': '点击一个绑定了文件上传事件的按钮元素, 然后静默处理该事件。',
                'drivingCharacter': 'Upload',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '文件路径',
                        'help': '文件完整路径。',
                        'key': 'file_path',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素选择器',
                        'help': '元素选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid',
                        'value': '1',
                    }
                ],
                'whetherThereReturn': False,
            },
            {
                'type': 'Instructions',
                'name': '下载文件',
                'help': '点击一个绑定了文件下载事件的按钮元素, 然后静默处理该事件。',
                'drivingCharacter': 'Download',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '文件路径',
                        'help': '文件保存完整路径。',
                        'key': 'file_path',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素选择器',
                        'help': '元素选择器, 允许 selector 或 XPath 定位。',
                        'key': 'element',
                        'value': '',
                    },
                    {
                        'type': 'Input',
                        'name': '元素下标',
                        'help': '若定位到多个元素, 可通过元素下标指定其一。',
                        'key': 'eid',
                        'value': '1',
                    }
                ],
                'whetherThereReturn': False,
            },
            {
                'type': 'Instructions',
                'name': '保存图片',
                'help': '保存当前屏幕截图。',
                'drivingCharacter': 'SavePng',
                'drivingParameter': [
                    {
                        'type': 'Input',
                        'name': '图片保存路径',
                        'help': '屏幕截图后需要保存至的本机完整路径。',
                        'key': 'save_path',
                        'value': '',
                    }
                ],
                'whetherThereReturn': False,
            },
        ],
    },
]

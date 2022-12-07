from mitmtools.remove import RemoveContentByUrl
from mitmtools.replace import ReplaceContentByUrl, ReplaceContentByRegex

addons = [
    # MitmproxyBase(),

    # replace
    # ReplaceContentByUrl(replace_dict={'百度一下，你就知道': '百度一下，你也不知道'}, url='https://www.baidu.com/')
    ReplaceContentByRegex(replace_dict={'百度一下，你就知道': '百度一下，你也不知道'},
                          pattern='^https://www.baidu.com.?$')

    # hook
    # HookByHtml(filepath='./static/hookfile.js'),
    # HookByJs(filepath='./static/hookfile.js'),
    # HookByJsUrl(url='', filepath='./static/hookfile.js'),

    # remove
    # RemoveContentByUrl(url='https://www.baidu.com/', remove_list=['百度一下，你就知道'])
]

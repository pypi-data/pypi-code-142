from soupwidget import Widget

from .common import *

class AlpineWidget(Widget):
    deps = {'alpinejsx': {'soup': gen_soup('<script src="https://unpkg.com/alpinejs" defer></script>'), 'priority': 0}}
    merge_data = []
    inject_data = []
    _alpine_data = None
    _fns_to_compile = {}

    def _data_safety(self):
        if self._alpine_data is None:
            self._alpine_data = {}

    def get_data(self):
        return self._alpine_data

    def set_data(self, d):
        self._data_safety()
        self._alpine_data = d

    def update_data(self, d={}):
        self._data_safety()
        #print('update_data', d)
        dict_deep_update(self._alpine_data, d)

@AlpineWidget.build_step()
def de_ps(self):
    self.set_soup_dep('alpinejs', gen_soup('<script src="https://unpkg.com/alpinejs" defer></script>'))

@AlpineWidget.build_step()
def create_xdata_attr(self):
    xdata = []
    if self.merge_data:
        for i in self.merge_data:
            self.update_data(i)
    if self.inject_data:
        for i in self.inject_data:
            i._build()
            dep_soup = i.as_soup()
            self.set_soup_dep(i.Meta.name, dep_soup)
            xdata.append(f'{i.Meta.name}()')
    data = self.get_data()
    #print('xdata.data', data)
    if data is not None:
        safe_data = json.dumps(data)
        xdata.append(safe_data)
    if xdata:
        #print('create_xdata_attr.xdata', self, xdata)
        if len(xdata) > 1:
            xdata_s = ''
            for i in xdata:
                if xdata_s:
                    xdata_s += ', '
                xdata_s += f'...{i}'
            xdata_s = '{' + xdata_s + '}'
        else:
            xdata_s = xdata[0]
        self.soup.attrs['x-data'] = xdata_s
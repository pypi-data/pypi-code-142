import pscript
import jsbeautifier
import textwrap
import json
import inspect
import re
import html as _html

def random_id():
    import random, string
    def base_n(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
        return ((num == 0) and numerals[0]) or (base_n(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
    return random.choice(string.ascii_lowercase) + base_n(random.randint(0, 99999999999999), 36)

def js_oneliner(s):
    import html
    def _remove_js_comments(string):
        import re
        pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
        regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
        def _replacer(match):
            if match.group(2) is not None:
                return ""
            else:
                return match.group(1)
        return regex.sub(_replacer, string)
    ret = s.strip().strip(';')
    ret = _remove_js_comments(ret).replace('\n', '')
    ret = re.sub(' +', ' ', ret)
    return html.unescape(ret)

class State:
    ___I_G_N_O_R_E___ = ('___I_G_N_O_R_E___', '__module__', '__doc__')

    def __new__(cls, **kw):
        class StateFromDict(cls):
            pass
        has_meta_attr = hasattr(cls, 'Meta')
        assert 'Meta' in kw or has_meta_attr, 'a State must have metadata (Meta innerclass)'
        if not has_meta_attr and isinstance(kw['Meta'], dict):
            class Meta:
                pass
            for k, v in kw['Meta'].items():
                setattr(Meta, k, v)
            kw['Meta'] = Meta
        for k, v in kw.items():
            setattr(StateFromDict, k, v)
        return StateFromDict

    @classmethod
    def js_src(cls, fn):
        setattr(fn, 'js_src', 1)
        return fn

    @classmethod
    def _fn_caller(cls, fname):
        ret = f'''
        ___literal(function() {{ {fname}.apply(this, arguments) }})literal___
        '''.strip()
        return ret

    @classmethod
    def _js_fn_caller(cls, fname, _src):
        src = js_oneliner(_src)
        ret = f'''
        ___literal(function() {{ {src} }})literal___
        '''.strip()
        return ret

    @classmethod
    def _fn_with_deps(cls, py_fn):
        py_fname = py_fn.__name__
        py_src = cls._get_dedented_src(py_fn)
        js_src = pscript.py2js(py_src)
        ret = f'''
        ___literal(
        function() {{
            {js_src}
            return {py_fname}.apply(this, arguments);
        }}
        )literal___
        '''
        ret = js_oneliner(ret)
        return ret

    @classmethod
    def _get_dedented_src(cls, fn, safe_prefix=''):
        ret = textwrap.dedent(inspect.getsource(fn))
        if safe_prefix:
            ret = re.sub('def (.*?)\(', f'def \\1_{safe_prefix}(', ret)
        return re.sub(r'(?m)^\@.*\n?', '', ret)

    @classmethod
    def _gen_js_fn_src(cls, fname, src):
        ret = f'''
        var {fname} = function() {{ {src} }}
        '''.strip()
        return ret

    @classmethod
    def _build(cls, separated_script=True):
        unique_id = random_id()
        obj = {}
        already_js = {}
        to_compile = {}
        attrs = vars(cls)
        for k in attrs:
            safe_k = f'{k}_{unique_id}'
            if k in cls.___I_G_N_O_R_E___:
                continue
            v = getattr(cls, k)
            if isinstance(v, type):
                continue
            if callable(v):
                js_src = getattr(v, 'js_src', False)
                if separated_script:
                    if js_src:
                        src = v()
                        already_js[k] = cls._gen_js_fn_src(safe_k, src)
                    else:
                        to_compile[k] = v
                    obj[k] = cls._fn_caller(safe_k)
                else:
                    if js_src:
                        src = v()
                        obj[k] = cls._js_fn_caller(safe_k, src)
                    else:
                        obj[k] = cls._fn_with_deps(v)
            else:
                obj[k] = v
        to_compile_src = ''
        for fname, fn in to_compile.items():
            to_compile_src += cls._get_dedented_src(fn, safe_prefix=unique_id)
        
        already_js_src = ''
        for fn, src in already_js.items():
            already_js_src += src + '\n'
        already_js_src = jsbeautifier.beautify(already_js_src)
    
        js = pscript.py2js(to_compile_src) + '\n' + already_js_src + '\n'
       
        obj = json.dumps(obj)
        obj = re.sub('''['"]___literal\((.*?)\)literal___['"]''', '\\1', obj).replace("'", '\\"')
        return js, obj
        
class AlpineData(State):

    @classmethod
    def as_plaintext(cls):
        js, obj = cls._build(separated_script=False)
        return obj

    @classmethod
    def as_script_and_json(cls):
        js, obj = cls._build()
        return js, obj

    @classmethod
    def as_script(cls):
        js, obj = cls._build()
        ret = f"""
        {js}
        document.addEventListener('alpine:init', () => {{
            Alpine.data('{cls.Meta.name}', () => {{
                return {obj}
            }})
        }})
        """
        ret = jsbeautifier.beautify(ret)
        ret = f'''
        <script>
        {ret.strip()}
        </script>
        '''.strip()
        return ret
    
    @classmethod
    def as_soup(cls):
        import bs4
        src = cls.as_script()
        return bs4.BeautifulSoup(src, 'html.parser')


class AlpineStore(State):
    
    @classmethod
    def as_plaintext(cls):
        js, obj = cls._build()
        return js, obj
    
    @classmethod
    def as_script(cls):
        js, obj = cls._build()
        ret = f"""
        {js}
        document.addEventListener('alpine:init', () => {{
            Alpine.store('{cls.name}', {obj})
        """
        ret = jsbeautifier.beautify(ret)
        ret = f'''
        <script>
        {ret.strip()}
        </script>
        '''.strip()
        return ret
    
    @classmethod
    def as_soup(cls):
        import bs4
        src = cls.as_script()
        return bs4.BeautifulSoup(src, 'html.parser')
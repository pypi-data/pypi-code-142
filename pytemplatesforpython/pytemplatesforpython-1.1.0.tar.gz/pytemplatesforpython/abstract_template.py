from types import CodeType
from typing import Any, Iterable, Type
from .abstract_prerender_zone import AbstractPrerenderZone, AbstractPrerenderZoneWithSubzones, PrerenderZonesParametersBase
from .pointer_string import PointerString

TAB = " "

class PrerenderZonesParameters(PrerenderZonesParametersBase):
    tabs_number: int
    template_name: str

    def __init__(self, string: str, template_name: str):
        self.tabs_number = 0
        try:
            self.pointer_original = PointerString(string)
        except IndexError:
            raise TemplateSyntaxTemplateIsEmptyError(template_name)
        self.template_name = template_name

class InnerTemplaterError(Exception):
    def __init__(self):
        super().__init__("inner templater error")

class TemplateError(Exception):
    def __init__(self, name: str):
        self._template_name = name
    
    def set_message(self, message: str):
        super().__init__(f"in the \"{self._template_name}\" template: " + message)

class TemplateSyntaxCurlyBracketsWereNotClosedError(TemplateError):
    def __init__(self, name: str):
        super().__init__(name)
        self.set_message(f"curly brackets were not closed")

class TemplateSyntaxTabsError(TemplateError):
    def __init__(self, name: str):
        super().__init__(name)
        self.set_message("\"{{-}}\" should be used in pairs with {{+}} above")

class TemplateSyntaxNewLineInCodeBlockError(TemplateError):
    def __init__(self, name: str):
        super().__init__(name)
        self.set_message("new lines in a code zone are not allowed. Use several code zones instead.")

class TemplateSyntaxCompilationError(TemplateError):
    def __init__(self, name: str, source_code: str):
        super().__init__(name)
        self.set_message(f"compilation error. Here is the source code:\n{source_code}")

class TemplateSyntaxTemplateIsEmptyError(TemplateError):
    def __init__(self, name: str):
        super().__init__(name)
        self.set_message("emply templates are not allowed")

class TemplateRenderError(TemplateError):
    def __init__(self, name: str, source_code: str):
        super().__init__(name)
        self.set_message(f"render error. Here is the source code:\n{source_code}")

class PrerenderRootZone(AbstractPrerenderZoneWithSubzones):
    _possible_subzone_types: list[Type[AbstractPrerenderZone]] = []
    symbols_to_protect: Iterable[str] = ["{", "\\"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._possible_subzone_types.append(PrerenderChangeTabsNumber)
        self._possible_subzone_types.append(PrerenderCodeZone)

    @classmethod
    def _entry_condition(cls, parameters: PrerenderZonesParameters) -> bool:
        return True

    def _entry(self, parameters: PrerenderZonesParameters) -> str:
        return ""

    def _process_symbol(self, parameters: PrerenderZonesParameters) -> str:
        result: str = parameters.pointer_original.get_symb(0)
        try:
            next_symb = parameters.pointer_original.get_symb(1)
        except IndexError:
            pass
        else:
            if result == "\\" and next_symb in self.symbols_to_protect:
                result += parameters.pointer_original.move(1)
        return result

    def _exit_condition(self, parameters: PrerenderZonesParameters) -> bool:
        return parameters.pointer_original.pointer == len(parameters.pointer_original.string)-1

    def _exit(self, parameters: PrerenderZonesParameters) -> str:
        return ""

    def _subzone_absence_entry(self, parameters: PrerenderZonesParameters) -> str:
        return parameters.tabs_number*TAB+"insert(\"\"\""

    def _subzone_absence_exit(self, parameters: PrerenderZonesParameters) -> str:
        return "\"\"\")\n"

    def _process_index_error(self, e: IndexError, parameters: PrerenderZonesParameters) -> None:
        raise InnerTemplaterError() from e
    

class PrerenderChangeTabsNumber(AbstractPrerenderZone):
    @classmethod
    def entry_condition(cls, parameters: PrerenderZonesParameters) -> bool:
        try:
            if parameters.pointer_original.get_symb(0) == parameters.pointer_original.get_symb(1) == "{":
                if parameters.pointer_original.get_symb(3) == parameters.pointer_original.get_symb(4) == "}":
                    return True
        except IndexError:
            pass
        return False

    def process(self, parameters: PrerenderZonesParameters) -> str:
        symb2 = parameters.pointer_original.get_symb(2)
        if symb2 == "+":
            parameters.tabs_number+=1
        elif symb2 == "-":
            parameters.tabs_number-=1
        parameters.pointer_original.move(4)
        return ""


class PrerenderCodeZone(AbstractPrerenderZoneWithSubzones):
    _possible_subzone_types: Iterable[Type[AbstractPrerenderZone]] = []
    exit: bool = False
    symbols_to_protect = ["}", "\\"]
    @classmethod
    def _entry_condition(cls, parameters: PrerenderZonesParameters) -> bool:
        try:
            return parameters.pointer_original.get_symb(0) == parameters.pointer_original.get_symb(1) == "{"
        except IndexError:
            return False

    def _entry(self, parameters: PrerenderZonesParameters) -> str:
        try:
            parameters.pointer_original.move(2)
            while parameters.pointer_original.get_symb(0) == " ":
                parameters.pointer_original.move(1)
        except IndexError:
            raise TemplateSyntaxCurlyBracketsWereNotClosedError(parameters.template_name)
        return parameters.tabs_number*TAB
    
    def _process_symbol(self, parameters: PrerenderZonesParameters) -> str:
        symb: str = parameters.pointer_original.get_symb(0)
        result = symb
        if symb == "\n":
            raise TemplateSyntaxNewLineInCodeBlockError(parameters.template_name)
                
        elif self.exit:
            return ""
        
        try:
            if symb == "\\" and parameters.pointer_original.get_symb(1) in self.symbols_to_protect:
                result += parameters.pointer_original.move(1)
        except IndexError:
            raise TemplateSyntaxCurlyBracketsWereNotClosedError(parameters.template_name)

        return result
    
    def _exit_condition(self, parameters: PrerenderZonesParameters) -> bool:
        try:
            if parameters.pointer_original.get_symb(1) == parameters.pointer_original.get_symb(2) == "}":
                self.exit = True
                return True
        except IndexError:
            raise TemplateSyntaxCurlyBracketsWereNotClosedError(parameters.template_name)
        return False

    def _exit(self, parameters: PrerenderZonesParameters) -> str:
        parameters.pointer_original.move(2)
        return "\n"

    def _subzone_absence_entry(self, parameters: PrerenderZonesParameters) -> str:
        return ""
    
    def _subzone_absence_exit(self, parameters: PrerenderZonesParameters) -> str:
        return ""
    
    def _process_index_error(self, e: IndexError, parameters: PrerenderZonesParameters) -> None:
        raise TemplateSyntaxCurlyBracketsWereNotClosedError(parameters.template_name)

class AbstractTemplate:
    _string: str
    name: str
    _code: CodeType
    _source_code: str
    
    @property
    def source_code(self) -> str:
        return self._source_code

    def __init__(self):
        self._prerender()
    
    def _exec_code(self, globals: dict) -> None:
        exec(self._code, globals)

    def _prerender(self) -> None:
        root: PrerenderRootZone = PrerenderRootZone()
        parameters: PrerenderZonesParameters = PrerenderZonesParameters(self._string, self.name)
        self._source_code = root.process(parameters)
        try:
            self._code = compile(self.source_code, self.name, "exec")
        except Exception as e:
            raise TemplateSyntaxCompilationError(parameters.template_name, self.source_code) from e

    def render(self, context: Any) -> str:
        result: str = ""

        def insert(string: Any) -> None:
            nonlocal result
            result += str(string)
        try:
            self._exec_code({
                "context": context, 
                "__name__": self.name, 
                "__doc__": None,
                "insert": insert,
                })
        except Exception as e:
            raise TemplateRenderError(self.name, self.source_code) from e
        return result
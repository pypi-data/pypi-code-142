#from xonsh.built_ins import XSH

import builtins

from xonsh.built_ins import XSH

from assistant.parser import ParseResult


def _convert_to_xonsh_subproc_string(parse : ParseResult):
    out = [[]]
    WORDS_THAT_SHOULD_BE_ALONE = ('|', '>>', '>', '<', '<<', '&&', '||')
    for word in parse.words:
        if word in WORDS_THAT_SHOULD_BE_ALONE:
            out.append(word)
            out.append([])
        else:
            out[-1].append(word)
    
    return out


def execute(parse: ParseResult):
    xonsh_seq = _convert_to_xonsh_subproc_string(parse)
    #xonsh_builtin.run_subproc(xonsh_seq)
    #print(xonsh_seq)
    #return __xonsh__.subproc_captured_stdout(xonsh_seq)
    try:
        results = []
        for xonsh_cmd in xonsh_seq:
            r = XSH.subproc_captured_hiddenobject(xonsh_cmd)
            if r:
                results.append(r)

        string_results = " ".join(results)
        if not string_results.find("xonsh: subprocess mode: command not found:"):
            return string_results
        else:
            return Exception(f"Assistant: {string_results}\n")
    except Exception as e:
        return None

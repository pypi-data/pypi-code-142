import inspect
import os
import click


#wrote magic to automate some things that clck doesnt do, i didnt want to have to specify each argument to click for each method when it can be done automatically using decorators
def register_fn(module,fn_name):
    fn = module.__dict__[fn_name]
    argspec = inspect.getfullargspec(fn)
    arguments = argspec.args
    defaults = argspec.defaults
    if not arguments:
        arguments = []
    if not defaults:
        defaults = []
    requireds = [index < len(arguments) - len(defaults)  for index in range(len(arguments)) ]
    for i in range( len(arguments) - 1, -1, -1) :
        fn = click.argument(arguments[i], required=requireds[i])(fn)
    fn = cli.command()(fn)
    return fn


def post_call(result):
    pass

def filter_function_name(name):
    return True

def load_module(module):
    for line in open(module.__file__):
        if line.startswith("def "):
            fn_name = line.split("def ")[1].split("(")[0]
            if filter_function_name(fn_name):
                register_fn(module,fn_name)

def instantcli(module):
    load_module(module)
    cli()

@click.group()
def cli():
    pass

@cli.result_callback()
def process_result(result):
    post_call(result)
    return result

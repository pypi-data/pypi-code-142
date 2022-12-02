import ast
from selenium.common.exceptions import WebDriverException


def wheel_element(element, deltaY = 120, offsetX = 0, offsetY = 0):
    """Scroll into an element without scrollbar (inside a web page),
    for example an html5 canvas.
    
    https://stackoverflow.com/a/47287595/2329968
    """
    error = element._parent.execute_script("""
        var element = arguments[0];
        var deltaY = arguments[1];
        var box = element.getBoundingClientRect();
        var clientX = box.left + (arguments[2] || box.width / 2);
        var clientY = box.top + (arguments[3] || box.height / 2);
        var target = element.ownerDocument.elementFromPoint(clientX, clientY);

        for (var e = target; e; e = e.parentElement) {
            if (e === element) {
            target.dispatchEvent(new MouseEvent('mouseover', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
            target.dispatchEvent(new MouseEvent('mousemove', {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY}));
            target.dispatchEvent(new WheelEvent('wheel',     {view: window, bubbles: true, cancelable: true, clientX: clientX, clientY: clientY, deltaY: deltaY}));
            return;
            }
        }    
        return "Element is not interactable";
        """, element, deltaY, offsetX, offsetY)
    if error:
        raise WebDriverException(error)


def assign_last_line_into_variable(code):
    """Take the last command and assign it to a known variable name, if it's
    not already an assignment.

    If the last command includes the "display()" function call, remove it.

    Examples
    ========

    >>> code = "p = already_an_assignment(1, 2, kw1=True, kw2=False)"
    >>> assign_last_line_into_variable(code)
    p = already_an_assignment(1, 2, kw1=True, kw2=False)

    >>> code = "some_command(1, 2, kw1=True, kw2=False)"
    >>> assign_last_line_into_variable(code)
    myk3d = some_command(1, 2, kw1=True, kw2=False)

    >>> code = ""some_other_command.display()""
    >>> assign_last_line_into_variable(code)
    myk3d = some_other_command

    """
    tree = ast.parse(code)
    ln = tree.body[-1]
    if isinstance(ln, ast.Assign):
        return code
    
    if isinstance(ln, ast.Expr):
        if (isinstance(ln.value, ast.Call) and
            isinstance(ln.value.func, ast.Attribute) and 
            (ln.value.func.attr == "display")):
            # we are in this case: k3dplot.display(). Remove display()
            tree.body[-1] = ast.parse(ln.value.func.value.id).body[0]
        
        # make an assignment
        value = tree.body[-1].value if isinstance(tree.body[-1], ast.Expr) else tree.body[-1]
        tree.body[-1] = ast.Assign(
            targets=[ast.Name(id="myk3d")], 
            value=value,
            lineno=tree.body[-1].lineno
        )
    return ast.unparse(tree)


def set_camera_position(code, camera):
    """Assing the camera position to the correct attribute and trigger a
    rendering so that axis labels will be visibile.
    """
    tree = ast.parse(code)
    tree.body.append(ast.parse("myk3d.camera = %s" % camera).body[-1])
    tree.body.append(ast.parse("myk3d.render()").body[-1])
    return ast.unparse(tree)

from pyqtgraph.Qt import QtWidgets

from qtextras import ParameterEditor, fns
from qtextras.examples.parameditor import LAST_RESULT, MyClass


def test_default_use(monkeypatch):
    pe = MyClass()
    with monkeypatch.context() as m:
        m.setattr(QtWidgets.QMessageBox, "information", lambda *args: None)

        for name, func in pe.nameFunctionMap.items():
            lowerName = name.lower()
            if "btn" in lowerName:
                assert pe.rootParameter.child(name).opts["button"]
            if func.parameters:
                paramToChange = next(iter(func.parameters.values()))
                old = LAST_RESULT.value
                if "changed" in lowerName:
                    paramToChange.sigValueChanged.emit(
                        paramToChange, paramToChange.value()
                    )
                    assert LAST_RESULT.value != old
                if "changing" in lowerName:
                    LAST_RESULT.value = old
                    paramToChange.sigValueChanging.emit(
                        paramToChange, paramToChange.value()
                    )
                    assert LAST_RESULT.value != old


def test_state_manager(tmp_path):
    pe = MyClass()
    for value, filter_ in zip(["value", "default"], (fns.valueIsNotDefault, None)):
        cmpState = fns.parameterValues(
            pe.rootParameter, value=value, valueFilter=filter_
        )
        savedState = (
            pe.getParameterDefaults() if value == "default" else pe.getParameterValues()
        )
        assert savedState == cmpState

    pe = MyClass(directory=tmp_path)
    pe.saveParameterValues(pe.stateManager.getDefaultStateName(), addDefaults=True)
    name, state = pe.stateManager.getDefaultStateName(returnStateDict=True)
    assert name.parent == tmp_path

    dummy = pe.rootParameter.addChild(dict(name="dummy", type="str", value="dummy"))
    dummy.setValue("test")
    assert "dummy" in str(pe.saveParameterValues(blockWrite=True))


def test_shortcut():
    pe = ParameterEditor()
    lastValue = None

    def on_shortcut():
        nonlocal lastValue
        lastValue = 17

    pe.registerFunction(on_shortcut, runActionTemplate={"shortcut": "Ctrl+C"})
    assert pe.nameShortcutMap["on_shortcut"].key().toString() == "Ctrl+C"
    pe.nameShortcutMap["on_shortcut"].activated.emit()
    assert lastValue == 17

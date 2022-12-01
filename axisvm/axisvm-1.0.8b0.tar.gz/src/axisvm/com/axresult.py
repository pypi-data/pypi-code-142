# -*- coding: utf-8 -*-
from .core.wrap import AxWrapper


class AxisVMResultItem(AxWrapper):
    """
    Base wrapper class for interfaces of items, such as individual
    lines, surfaces, etc.

    """

    def __init__(self, *args, parent=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent

    @property
    def model(self):
        return self.parent.model

    def _get_case_or_component(self, *args, case=None, combination=None,
                               LoadCaseId=None, LoadCombinationId=None, **kwargs):
        axm = self.model
        if case is not None:
            LoadCombinationId = None
            if isinstance(case, str):
                LoadCases = axm.LoadCases
                imap = {LoadCases.Name[i]: i for i in range(
                    1, LoadCases.Count+1)}
                if case in imap:
                    LoadCaseId = imap[case]
                else:
                    raise KeyError("Unknown case with name '{}'".format(case))
            elif isinstance(case, int):
                LoadCaseId = case
        elif combination is not None:
            LoadCaseId = None
            if isinstance(combination, str):
                LoadCombinations = axm.LoadCombinations
                imap = {LoadCombinations.Name[i]: i for i in range(
                    1, LoadCombinations.Count+1)}
                if combination in imap:
                    LoadCombinationId = imap[combination]
                else:
                    raise KeyError(
                        "Unknown combination with name '{}'".format(combination))
            elif isinstance(combination, int):
                LoadCombinationId = combination
        return LoadCaseId, LoadCombinationId

    def config(self, *args, DisplacementSystem=None,
               LoadLevelOrModeShapeOrTimeStep=None, **kwargs):
        LoadCaseId, LoadCombinationId = self._get_case_or_component(*args, **kwargs)
        resobj = self._wrapped
        if isinstance(DisplacementSystem, int):
            resobj.DisplacementSystem = DisplacementSystem
        if LoadCaseId is not None:
            resobj.LoadCaseId = LoadCaseId
        if LoadCombinationId is not None:
            resobj.LoadCombinationId = LoadCombinationId
        if LoadLevelOrModeShapeOrTimeStep is not None:
            resobj.LoadLevelOrModeShapeOrTimeStep = LoadLevelOrModeShapeOrTimeStep


class IAxisVMDisplacements(AxisVMResultItem):
    """Wrapper for the `IAxisVMDisplacements` COM interface."""
    ...


class IAxisVMForces(AxisVMResultItem):
    """Wrapper for the `IAxisVMForces` COM interface."""
    ...


class IAxisVMStresses(AxisVMResultItem):
    """Wrapper for the `IAxisVMStresses` COM interface."""
    ...


class IAxisVMResults(AxWrapper):
    """Wrapper for the `IAxisVMResults` COM interface."""
    
    def __init__(self, *args, model=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    @property
    def Displacements(self) -> IAxisVMDisplacements:
        return IAxisVMDisplacements(parent=self, wrap=self._wrapped.Displacements)

    @property
    def Forces(self) -> IAxisVMForces:
        return IAxisVMForces(parent=self, wrap=self._wrapped.Forces)

    @property
    def Stresses(self) -> IAxisVMStresses:
        return IAxisVMStresses(parent=self, wrap=self._wrapped.Stresses)

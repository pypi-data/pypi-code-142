# -*- coding: utf-8 -*-
import numpy as np
import awkward as ak

from polymesh import PointCloud, CartesianFrame
from polymesh.topo import TopologyArray
from neumann.linalg.sparse.utils import count_cols

from .core.wrap import AxWrapper, AxisVMModelItems
from .core.utils import RDisplacementValues2list

from .axnode import IAxisVMNodes
from .axdomain import IAxisVMDomains, AxDomainCollection
from .axmember import IAxisVMMembers
from .axsurface import IAxisVMSurfaces
from .axline import IAxisVMLines
from .axwindow import IAxisVMWindows
from .axresult import IAxisVMResults
from .axmaterial import IAxisVMMaterials
from .axcalculation import IAxisVMCalculation


__all__ = ['IAxisVMModels', 'IAxisVMModel']


class IAxisVMModel(AxWrapper):
    """Wrapper for the `IAxisVMModel` COM interface."""

    def __init__(self, *args, parent=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent

    @property
    def Nodes(self) -> IAxisVMNodes:
        """Returns a pointer object to the `IAxisVMNodes` COM interface."""
        return IAxisVMNodes(model=self, wrap=self._wrapped.Nodes)

    @property
    def Members(self) -> IAxisVMMembers:
        """Returns a pointer object to the `IAxisVMMembers` COM interface."""
        return IAxisVMMembers(model=self, wrap=self._wrapped.Members)

    @property
    def Domains(self) -> IAxisVMDomains:
        """Returns a pointer object to the `IAxisVMDomains` COM interface."""
        return IAxisVMDomains(model=self, wrap=self._wrapped.Domains)

    @property
    def XLAMDomains(self) -> AxDomainCollection:
        return AxDomainCollection(self.Domains.XLAMItems)

    @property
    def Lines(self) -> IAxisVMLines:
        """Returns a pointer object to the `IAxisVMLines` COM interface."""
        return IAxisVMLines(model=self, wrap=self._wrapped.Lines)

    @property
    def Surfaces(self) -> IAxisVMSurfaces:
        """Returns a pointer object to the `IAxisVMSurfaces` COM interface."""
        return IAxisVMSurfaces(model=self, wrap=self._wrapped.Surfaces)

    @property
    def Windows(self) -> IAxisVMWindows:
        """Returns a pointer object to the `IAxisVMWindows` COM interface."""
        return IAxisVMWindows(model=self, wrap=self._wrapped.Windows)

    @property
    def Results(self) -> IAxisVMResults:
        """Returns a pointer object to the `IAxisVMResults` COM interface."""
        return IAxisVMResults(model=self, wrap=self._wrapped.Results)

    @property
    def Calculation(self) -> IAxisVMCalculation:
        """Returns a pointer object to the `IAxisVMCalculation` COM interface."""
        return IAxisVMCalculation(model=self, wrap=self._wrapped.Calculation)

    @property
    def Materials(self) -> IAxisVMMaterials:
        """Returns a pointer object to the `IAxisVMMaterials` COM interface."""
        return IAxisVMMaterials(model=self, wrap=self._wrapped.Materials)

    @property
    def MeshSurfaceIds(self) -> np.ndarray:
        """Returns the indices of the surfaces of all domains in the model
        as a :class:`numpy.ndarray`."""
        d = self.Domains
        dc = d.Count
        def fnc(i): return d[i+1].MeshSurfaceIds
        return np.vstack(list(map(fnc, range(dc)))).flatten().astype(np.int64)

    def points(self, ids=None) -> PointCloud:
        frame = CartesianFrame(dim=3)
        if isinstance(ids, np.ndarray):
            ids = ids.astype(np.int32)
        elif isinstance(ids, int):
            ids = [ids]
        if ids is not None:
            coords = self.Nodes.BulkGetCoord(ids)[0]
        else:
            lines = self.Lines
            lc, mpc = lines.Count, self.Lines.MidPointCount
            ids = np.array(list(range(self.Nodes.Count))) + 1
            coords = self.Nodes.BulkGetCoord(ids)[0]
            coords = np.array([[n.x, n.y, n.z] for n in coords])
            if lc > 0 and mpc > 0:
                def fnc(i): return lines.GetMidpoint(i+1)[0]
                def xyz(n): return [n.x, n.y, n.z]
                coords_mid = np.array(list(map(xyz, map(fnc, range(lc)))))
                def fnc(i): return lines.MidpointId[i+1]
                mIDs = np.array(list(map(fnc, range(lc))))
                i = np.where(mIDs > 0)[0]
                mIDs = mIDs[i]
                coords_mid = coords_mid[i]
                coords = np.vstack([coords, coords_mid])
                ids = np.concatenate([ids, mIDs])
        return PointCloud(coords, inds=ids, frame=frame)

    def coordinates(self, ids=None) -> np.ndarray:
        """
        Returns the coordinates of the points in the model as a :class:`numpy.ndarray`. 
        
        Parameters
        ----------
        ids : int or :class:`numpy.ndarray`, Optional
            Indices of points, whose coordinates are to be returned. If there are no
            indices specified, coordinates for all points are returned. Default is None.
            
        Returns
        -------
        :class:`polymesh.PointCloud`
        """
        return self.points(ids).show()

    def topology(self) -> TopologyArray:
        res = []

        if self.Members.Count > 0:
            res.append(self.Members.topology())
        if self.Surfaces.Count > 0:
            res.append(self.Surfaces.topology())
            """s = self.Surfaces
            sIDs = self.MeshSurfaceIds
            def fnc_corner(i): return list(s[i].GetContourPoints()[0])
            def fnc_mid(i): return list(s[i].GetMidPoints()[0])
            def fnc(i): return fnc_corner(i) + fnc_mid(i)
            res.append(TopologyArray(ak.Array(list(map(fnc, sIDs)))))"""
        if len(res) >= 2:
            return np.vstack(res)
        return res[0] if len(res) == 1 else None

    def dof_solution(self, *args, DisplacementSystem=1, LoadCaseId=None,
                     LoadLevelOrModeShapeOrTimeStep=None, LoadCombinationId=None,
                     case=None, combination=None, **kwargs) -> np.ndarray:
        """
        Returns degree of freedom solution for the whole model as a :class:`numpy.ndarray`.
        
        Parameters
        ----------
        DisplacementSystem : int, Optional
            0 for local, 1 for global. Default is 1.
        
        LoadCaseId : int, Optional
            Default is None.
            
        LoadLevelOrModeShapeOrTimeStep : int, Optional
            Default is None.
            
        LoadCombinationId : int, Optional
            Default is None.
            
        case : str, Optional
            The name of a loadcase. Default is None.
        
        combination : str, Optional
            The name of a load combination. Default is None.
        
        Returns
        -------
        :class:`numpy.ndarray`
        
        """
        if case is not None:
            LoadCombinationId = None
            if isinstance(case, str):
                LoadCases = self.LoadCases
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
                LoadCombinations = self.LoadCombinations
                imap = {LoadCombinations.Name[i]: i for i in range(
                    1, LoadCombinations.Count+1)}
                if combination in imap:
                    LoadCombinationId = imap[combination]
                else:
                    raise KeyError(
                        "Unknown combination with name '{}'".format(combination))
            elif isinstance(combination, int):
                LoadCombinationId = combination
        disps = self.Results.Displacements
        if DisplacementSystem is None:
            DisplacementSystem = 1  # global
        if isinstance(DisplacementSystem, int):
            disps.DisplacementSystem = DisplacementSystem
        if LoadCaseId is not None:
            disps.LoadCaseId = LoadCaseId
        if LoadCombinationId is not None:
            disps.LoadCombinationId = LoadCombinationId
        if LoadLevelOrModeShapeOrTimeStep is None:
            LoadLevelOrModeShapeOrTimeStep = 1
        disps.LoadLevelOrModeShapeOrTimeStep = LoadLevelOrModeShapeOrTimeStep
        if LoadCaseId is not None:
            recs = disps.AllNodalDisplacementsByLoadCaseId()[0]
        elif LoadCombinationId is not None:
            recs = disps.AllNodalDisplacementsByLoadCombinationId()[0]
        return np.array(list(map(RDisplacementValues2list, recs)))

    def generalized_surface_forces(self, *args, **kwargs):
        """Returns internal forces and moments for all surfaces in the model."""
        return self.Surfaces.generalized_surface_forces(*args, **kwargs)

    def surface_stresses(self, *args, **kwargs):
        """Returns stresses for all surfaces in the model."""
        return self.Surfaces.surface_stresses(*args, **kwargs)

    def critical_xlam_data(self, *args, CombinationType=None,  AnalysisType=0, **kwargs):
        """
        Returns critical XLAM data.
        
        Parameters
        ----------
        CombinationType : int, Optional
            Default is None.
        
        AnalysisType : int, Optional
            Default is 0.
                
        """
        Domains = self.Domains
        Surfaces = self.Surfaces
        dparams = dict(
            MinMaxType=1,
            CombinationType=CombinationType,
            AnalysisType=AnalysisType,
            Component=4  # xse_Max
        )

        def get_efficiencies(i):
            return Domains[i].critical_xlam_surface_efficiencies(**dparams)
        
        vmax = 0 
        did, sid, nid, f, lc = (None,) * 5
        for d in Domains.XLAMItems:
            data = get_efficiencies(d.Index)
            cuts = count_cols(data)
            eff_max = ak.flatten(data[:, :, -1]).to_numpy()
            imax = np.argmax(eff_max)
            _vmax = eff_max[imax]
            if _vmax > vmax:
                vmax = _vmax
                did = d.Index 
                csum = np.cumsum(cuts)
                iS = np.where(csum > imax)[0][0]
                iN = imax - csum[iS-1]
                sid = d.MeshSurfaceIds[iS]
                nid = d.topology()[iS, iN]

                if cuts[iS] == 6:
                    SurfaceVertexType = 0 if iN < 3 else 1
                elif cuts[iS] == 8:
                    SurfaceVertexType = 0 if iN < 4 else 1
                else:
                    raise NotImplementedError

                sparams = dict(
                    SurfaceVertexType=SurfaceVertexType,
                    SurfaceVertexId=nid,
                    MinMaxType=1,
                    CombinationType=CombinationType,
                    AnalysisType=AnalysisType,
                    Component=4
                )
                _, f, lc = Surfaces[sid].critical_xlam_efficiency(**sparams)
                
        return f, lc, (did, sid, nid)

    def __enter__(self):
        if self._wrapped is not None:
            self._wrapped.BeginUpdate()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self._wrapped is not None:
            self._wrapped.EndUpdate()

    def _get_attrs(self):
        """Return the representation methods (internal helper)."""
        attrs = []
        attrs.append(("N Nodes", self.Nodes.Count, "{}"))
        attrs.append(("N Lines", self.Lines.Count, "{}"))
        attrs.append(("N Members", self.Members.Count, "{}"))
        attrs.append(("N Surfaces", self.Surfaces.Count, "{}"))
        attrs.append(("N Domains", self.Domains.Count, "{}"))
        """bds = self.bounds
        fmt = f"{axisvm.FLOAT_FORMAT}, {axisvm.FLOAT_FORMAT}"
        attrs.append(("X Bounds", (bds[0], bds[1]), fmt))
        attrs.append(("Y Bounds", (bds[2], bds[3]), fmt))
        attrs.append(("Z Bounds", (bds[4], bds[5]), fmt))"""
        return attrs


class IAxisVMModels(AxWrapper):
    """Wrapper for the `IAxisVMModels` COM interface."""

    __itemcls__ = IAxisVMModel

    def __init__(self, *args, app=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app

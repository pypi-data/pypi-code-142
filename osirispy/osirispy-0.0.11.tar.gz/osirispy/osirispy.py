import numpy as np
import h5py

def read(fname,req_quants=("x1","x2")):
    """
    Reads an OSIRIS output data file.

    Parameters
    ----------
    fname : str
        The path to the data file
    req_quants : list of str
        The quantities required when reading RAW or TRACKS files
    """
    f=h5py.File(fname,"r")
    datatype=f.attrs["TYPE"][0].decode('UTF-8')    
    f.close()
    data=None
    match datatype:
        case "grid":
            data=grid(fname)
        case "particles":
            data=raw(fname,req_quants)
        case "tracks-2":
            data=track(fname,req_quants)
        case _:
             exit()
    return data

class os_data:
    def __init__(self,datatype):
        self._datatype=datatype

    @property
    def datatype(self):
        return self._datatype


class axis:
    """
    A class used to represent an axis object
    ...

    Attributes
    ----------
    nx : int
        the number of grid poits along the axis
    ax_arr : np.array
        the array of points of the axis
    name : str
        the label of the axis
    """

    def __init__(self,nx,lims,name):
        self._nx=nx
        self._name=name
        self._ax_arr=np.linspace(lims[0],lims[1],nx)
        
    
    @property
    def nx(self):
        return self._nx
    
    @property
    def name(self):
        return self._name
    
    @property
    def ax_arr(self):
        return self._ax_arr

class grid(os_data):
    """
    A class used to represent a grid data object

    ...

    Attributes
    ----------
    dims : int
        a formatted string to print out what the animal says
    axis : list of axes
        a list of axis objects containg the spatial limits of the grid
    data : np.array
        the grid data
    name : str
        the label of the quantity in the grid
    time_s : np.float
        the timestamp of the grid file
    """
    def __init__(self,fname):
        os_data.__init__(self,"grid")
        self._axis=[]
        f=h5py.File(fname,"r")
        #field
        objs=f.keys()
        for name in objs:
            if isinstance(f[name], h5py.Dataset):
                dat=np.array(f[name]) #charge for density, e2 for OSIRIS fields, e3_x2_slice for slices
        #time axis
        objs=f["AXIS"].keys()
        for i,axis_n in enumerate(objs):
            ax1=f["AXIS/"+axis_n]   
            axis1=np.array(ax1)
            np.shape(dat)[-(i+1)]
            ax1name=ax1.attrs["NAME"][0].decode('UTF-8')+" ["+ax1.attrs["UNITS"][0].decode('UTF-8')+"]"
            self._axis.append(axis(np.shape(dat)[-(i+1)],axis1,ax1name))     
        
        dataname=f.attrs["NAME"][0].decode('UTF-8')+" ["+f.attrs["UNITS"][0].decode('UTF-8')+"]"
        time_s=f.attrs["TIME"][0]
        f.close()
        self._dims=len(self._axis)
        self._data=dat
        self._name=dataname
        self._time_s=time_s
        
    @property
    def axis(self):
        return self._axis

    @property
    def dims(self):
        return self._dims

    @property
    def data(self):
        return self._data
    
    @property
    def name(self):
        return self._name
    
    @property
    def data(self):
        return self._data
    
    @property
    def time_s(self):
        return self._time_s




class raw(os_data):
    """
    A class used to represent a particles data object

    ...

    Attributes
    ----------
    data : dictionary of np.arrays
        a dictionary containing the required quantities
    label : dictionary of str
        a dictionary containing the labels of required quantities
    time_s : np.float
        the timestamp of the grid file
    """
    def __init__(self,fname,req_quants):
        os_data.__init__(self,"particles")
        self._data=dict.fromkeys(req_quants,None)
        self._label=dict.fromkeys(req_quants,None)
        f=h5py.File(fname,"r")
        #field
        quants=[i.decode('UTF-8') for i in f.attrs["QUANTS"]]
        labels=[i.decode('UTF-8') for i in f.attrs["LABELS"]]
        units=[i.decode('UTF-8') for i in f.attrs["UNITS"]]
        labels=dict(zip(quants, labels))
        units=dict(zip(quants, units))
        try:
            for quant in req_quants:
                self._data[quant]=np.array(f[quant])
                self._label[quant]=labels[quant]+" ["+units[quant]+"]"
        except KeyError as ke:
            err_str="Available Objects: "+str(quants)
            raise KeyError(err_str)
        self._time_s=f.attrs["TIME"][0]
        f.close()
    @property
    def label(self):
        return self._label
    @property
    def data(self):
        return self._data
    
    @property
    def time_s(self):
        return self._time_s


class track(os_data):
    """
    A class used to represent a tracks data object

    ...

    Attributes
    ----------
    data : dictionary of lists of np.arrays
        a dictionary containing lists the required quantities for each particle
    label : dictionary of str
        a dictionary containing the labels of required quantities
    """

    def __init__(self,fname,req_quants):
        os_data.__init__(self,"tracks-v2")
        self._data=dict.fromkeys(req_quants,None)
        self._label=dict.fromkeys(req_quants,None)
        f=h5py.File(file,"r")
        quants=[i.decode('UTF-8') for i in f.attrs["QUANTS"]][1:]
        labels=[i.decode('UTF-8') for i in f.attrs["LABELS"]][1:]
        units=[i.decode('UTF-8') for i in f.attrs["UNITS"]][1:]
        labels=dict(zip(quants, labels))
        units=dict(zip(quants, units))

        itermap=np.array(f["itermap"])
        ntracks=f.attrs["NTRACKS"][0]
        for i in range(len(itermap)):
            itermap[i,2]=np.sum(itermap[:i,1])
        itermaps=[]
        for i in range(1,ntracks+1):
            itermaps.append(itermap[itermap[:,0]==i,1:])
        itermaps_tracks=[]
        for i in range(len(itermaps)):
            itermap_=[]
            if len(itermaps[i])>1:
                for bound in itermaps[i]:
                    itermap_.append(np.arange(bound[1],bound[1]+bound[0]))
                itermaps_tracks.append(np.concatenate(itermap_))
        data=np.array(f["data"])
        print(f.attrs["QUANTS"])
        f.close()
        
        try:
            for quant in req_quants:
                idx=quants.index(quant)
                print(idx)
                self._data[quant]=[]
                for track_idx in itermaps_tracks:
                    self._data[quant].append(data[track_idx,idx])
                self._label[quant]=labels[quant]+" ["+units[quant]+"]"
        except ValueError as ke:
            err_str="Available Objects: "+str(quants)
            raise ValueError(err_str)

        
    @property
    def label(self):
        return self._label
    @property
    def data(self):
        return self._data
    

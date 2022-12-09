import numpy as np
import h5py

def read(fname,req_quants=("x1","x2")):
    """Reads an OSIRIS output data file.

    :param fname: The path to the data file
    :type fname: str
    :param req_quants: The quantities required when reading RAW or TRACKS files, defaults to ("x1","x2")
    :type req_quants: tuple of str, optional
    :return: An os_data object
    :rtype: :class:`os_data`
    """  

    #retrieve the data type of the file
    f=h5py.File(fname,"r")
    datatype=f.attrs["TYPE"][0].decode('UTF-8')    
    f.close()
    data=None

    #initialize the data object according to dataype
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
    """ A class to represent a generic OSIRIS output data object.

    :param datatype: The type of OSIRIS data ('grid', 'particles' our 'tracks')
    :type datatype: str
    """    
    
    def __init__(self,datatype):
        """Constructs all the necessary attributes for the os_data object.

        :param datatype: The type of OSIRIS data ('grid', 'particles' our 'tracks')
        :type datatype: str
        """        
        self._datatype=datatype

    @property
    def datatype(self):
        return self._datatype


class axis:
    """ A class used to represent an axis object

    :param nx : The number of points along the axis
    :type nx: int
    :param ax_arr : The array containing the axis poins        
    :type ax_arr : :class:`np.array`
    :param label: The axis label
    :type label : str
    """    

    def __init__(self,nx,lims,label):
        """Constructs all the necessary attributes for the os_data object.

        :param nx: The number of points along the axis
        :type nx: int
        :param ax_arr: The array containing the axis poins        
        :type ax_arr: :class:`np.array`
        :param label: The axis label
        :type label: str 
        """

        self._nx=nx
        self._label=label
        self._ax_arr=np.linspace(lims[0],lims[1],nx)
        
    
    @property
    def nx(self):
        return self._nx
    
    @property
    def label(self):
        return self._label
    
    @property
    def ax_arr(self):
        return self._ax_arr

class grid(os_data):
    """A class used to represent a grid data object

    :param dims: A formatted string to print out what the animal says
    :type dims: int
    :param axis: A list of axis objects containg the spatial limits of the grid
    :type axis: list of :class:`axis`
    :param data: The grid data
    :type data: :class:`np.array`
    :param label: The label of the quantity in the grid
    :type label: str
    :param time_s: The timestamp of the grid file
    :type time_s: :class:`np.float`
    
    """    

    def __init__(self,fname):
        """Constructs all the necessary attributes for the grid object.

        :param fname: The path to the osiris data file
        :type fname: str
        """        

        #initialize the parent class
        os_data.__init__(self,"grid")
        #initialize the axis list
        self._axis=[]
        #open the file
        f=h5py.File(fname,"r")
        #read the dataset
        objs=f.keys()
        for name in objs:
            if isinstance(f[name], h5py.Dataset):
                dat=np.array(f[name]) #charge for density, e2 for OSIRIS fields, e3_x2_slice for slices
        #loop through the axis and fill the axis array
        objs=f["AXIS"].keys()
        for i,axis_n in enumerate(objs):
            ax1=f["AXIS/"+axis_n]   
            axis1=np.array(ax1)
            #retrieve number of point along axis
            np.shape(dat)[-(i+1)]
            #retrive axis label
            ax1name=ax1.attrs["NAME"][0].decode('UTF-8')+" ["+ax1.attrs["UNITS"][0].decode('UTF-8')+"]"
            self._axis.append(axis(np.shape(dat)[-(i+1)],axis1,ax1name))     
        #retrive data label
        dataname=f.attrs["NAME"][0].decode('UTF-8')+" ["+f.attrs["UNITS"][0].decode('UTF-8')+"]"
        #retrive data timestamp
        time_s=f.attrs["TIME"][0]
        #close the files
        f.close()
        #fill in the attributes
        self._dims=len(self._axis)
        self._data=dat
        self._label=dataname
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
    def label(self):
        return self._label
    
    @property
    def data(self):
        return self._data
    
    @property
    def time_s(self):
        return self._time_s




class raw(os_data):
    """A class used to represent a particles data object

    :param data: a dictionary containing the required quantities
    :type data:  dict of (str,np.arrays)
    :param label: a dictionary containing the labels of required quantities
    :type label: dict of (str,str)
    :param time_s: the timestamp of the grid file
    :type time_s: np.float
    """    

    def __init__(self,fname,req_quants):
        """Constructs all the necessary attributes for the raw object.
        Loads the required quantities (if available) into a dictionary of np.arrays whose keys are the requeired quantities.

        :param fname: The path to the osiris data file
        :type fname: str
        :param req_quants: A list containing the required quantities
        :type req_quants:  list of str
        :raises KeyError: If a required quantity is not available on the file
        """        
        # initialize the parent class
        os_data.__init__(self,"particles")
        #initialize the dictionaries
        self._data=dict.fromkeys(req_quants,None)
        self._label=dict.fromkeys(req_quants,None)
        #open the file
        f=h5py.File(fname,"r")
        #retrieve the available quantities
        quants=[i.decode('UTF-8') for i in f.attrs["QUANTS"]]
        #retrieve the corresponding labels
        labels=[i.decode('UTF-8') for i in f.attrs["LABELS"]]
        #retrieve the corresponding units
        units=[i.decode('UTF-8') for i in f.attrs["UNITS"]]
        #build the aux dictionaries
        labels=dict(zip(quants, labels))
        units=dict(zip(quants, units))
        #try to build the class dictionaries
        try:
            for quant in req_quants:
                self._data[quant]=np.array(f[quant])
                self._label[quant]=labels[quant]+" ["+units[quant]+"]"
        except KeyError as ke:
            err_str="Available Objects: "+str(quants)
            raise KeyError(err_str)
        #retrieve data timestamp
        self._time_s=f.attrs["TIME"][0]
        #close the files
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
    """A class used to represent a tracks data object

    :param data: a dictionary containing the required quantities for each particle
    :type data:  dict of (str,list of np.arrays)
    :param label: a dictionary containing the labels of required quantities
    :type label: dict of (str,str)
    """   

    def __init__(self,fname,req_quants):
        """Constructs all the necessary attributes for the tracks object.
        Reads fname and loads the required quantities (if available) into a dictionary of lists np.arrays whose keys are the requeired quantities.


        :param fname: The path to the osiris data file
        :type fname: str
        :param req_quants: A list containing the required quantities
        :type req_quants:  list of str
        :raises KeyError: If a required quantity is not available on the file
        """        

        # initialize the parent class        
        os_data.__init__(self,"tracks-v2")
        #initialize the dictionaries
        self._data=dict.fromkeys(req_quants,None)
        self._label=dict.fromkeys(req_quants,None)
        #open the file
        f=h5py.File(file,"r")
        #retrieve the available quantities, labels and units
        quants=[i.decode('UTF-8') for i in f.attrs["QUANTS"]][1:]
        labels=[i.decode('UTF-8') for i in f.attrs["LABELS"]][1:]
        units=[i.decode('UTF-8') for i in f.attrs["UNITS"]][1:]
        #build auxiliary dictionaries
        labels=dict(zip(quants, labels))
        units=dict(zip(quants, units))
        #retrieve the itermap array
        itermap=np.array(f["itermap"])
        #retrieve the number of tracks in the file
        ntracks=f.attrs["NTRACKS"][0]
        #modify the itermap array to contain the actual starting index for each particle instead of the relative index
        for i in range(len(itermap)):
            itermap[i,2]=np.sum(itermap[:i,1])
        #initialize the itermaps array
        itermaps=[]
        #the itermaps array is a list containing the itermap bounds for each particle (actual start and end idx for each particle in the data array)
        for i in range(1,ntracks+1):
            itermaps.append(itermap[itermap[:,0]==i,1:])
        #initialize the itermaps array
        itermaps_tracks=[]
        #the itermaps_tracks array is a list containing the itermap for each particle (all the idx for each particle in the data array)
        for i in range(len(itermaps)):
            itermap_=[]
            if len(itermaps[i])>1:
                for bound in itermaps[i]:
                    itermap_.append(np.arange(bound[1],bound[1]+bound[0]))
                itermaps_tracks.append(np.concatenate(itermap_))
        #retrieve the data array
        data=np.array(f["data"])
        print(f.attrs["QUANTS"])
        f.close()

        #try to build the class dictionaries
        try:
            for quant in req_quants:
                idx=quants.index(quant)
                print(idx)
                self._data[quant]=[]
                #loop through the particles and retireve the data usinf the arrays in itermaps_tracks 
                for track_idx in itermaps_tracks:
                    #append the data for particle x to the list in the dictionary
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
    

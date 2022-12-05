import os
import numpy as np
import netCDF4 as nc
import pyproj
from pyproj import Transformer
import pandas as pd
from pandas import DataFrame
import warnings
import glob
from datetime import timedelta,datetime
from pyproj import CRS,Transformer
import pyproj
import cartopy.crs as ccrs
warnings.filterwarnings("ignore")


#读取捕风L1C .NC文件到Dataframe
basepath = os.path.abspath(__file__)
folder = os.path.dirname(basepath)
aeffpath = os.path.join(folder, 'data','inc2eff.xlsx')
aefflist = pd.read_excel(aeffpath)
aefflist["inc_angle_int"] = aefflist.index
def ReadBF_L1C(path:str):
    """
       读取BuFeng .nc文件
       输入：文件路径path(string)：r'/share/public/group_shared/gnssr/BF-L1C/BF-1A/BF1A_DDMXX_GBAL_L1_20190801_0340_00853_00000_MS.NC'
       输出：
            格式:DataFrame
            内容:1> tx/sc_pos/vel_x/y/z  -->  卫星/接收机 的 位置/速度 的 x,y,z
                 2> sp_pos_x/y/z  -->  镜面点位置 的 x,y,z
                 3> inc/ele_angle  -->  入射角/高度角
                 4> sp_lon/lat/alt  -->  镜面点lla坐标  [alt = 0]
                 5> snr  -->  捕风ddm_snr
        注意：lla坐标用pyproj算的(x
    """
        
    ecef = pyproj.Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    lla = pyproj.Proj(proj='latlong', ellps='WGS84', datum='WGS84')

    lookup = {"tx_pos_x":"gnss_ecef.0","tx_pos_y":"gnss_ecef.1","tx_pos_z":"gnss_ecef.2","tx_vel_x":"gnss_ecef.3","tx_vel_y":"gnss_ecef.4","tx_vel_z":"gnss_ecef.5"
             ,"sc_pos_x":"remote_ecef.0","sc_pos_y":"remote_ecef.1","sc_pos_z":"remote_ecef.2","sc_vel_x":"remote_ecef.3","sc_vel_y":"remote_ecef.4"
             ,"sc_vel_z":"remote_ecef.5"}
    lookup2 = {"ele_angle":"elevation_angle","snr":"ddm_snr","PRN":"gnss_prn","sec":'second','wk':'week'}
    lookup3 = {"sp_pos_x":"reflect_ecef.0","sp_pos_y":"reflect_ecef.1","sp_pos_z":"reflect_ecef.2"}
    ncfile = nc.Dataset(path)
    dic1 = {key:ncfile.variables[value.split('.')[0]][:].data.transpose()[int(value.split('.')[1])] for key,value in lookup.items()}
    dic2 = {key:ncfile.variables[value][:].data for key,value in lookup2.items()}
    dic3 = {key:ncfile.variables[value.split('.')[0]][:].data.transpose()[int(value.split('.')[1])] for key,value in lookup3.items()}
    df1 = DataFrame(dic1)
    df2 = DataFrame(dic2)
    df3 = DataFrame(dic3)
    df = pd.concat([df2,df1,df3],axis = 1)
    #时间戳
    dts = datetime.strptime('80-01-06', '%y-%m-%d')
    td=timedelta(seconds=1)
    df['time']=dts+td*df['sec']+td*df['wk']*604800
    #计算一些有的没的
    df['Rsr'] = np.sqrt((df.sc_pos_x - df.sp_pos_x)**2+(df.sc_pos_y - df.sp_pos_y)**2+(df.sc_pos_z - df.sp_pos_z)**2)
    df['Rts'] = np.sqrt((df.tx_pos_x - df.sp_pos_x)**2+(df.tx_pos_y - df.sp_pos_y)**2+(df.tx_pos_z - df.sp_pos_z)**2)
    df["inc_angle"] = 90 - df["ele_angle"]
    df["lon"], df["lat"], df["alt"] = pyproj.transform(ecef, lla, df["sp_pos_x"].values, df["sp_pos_y"].values, df["sp_pos_z"].values, radians=False)
    df["date"] = int(path.split('/')[-1].split('.')[0].split('_')[4])
    #有效散射面积
    df["inc_angle_int"] = df["inc_angle"]//1
    df = pd.merge(df, aefflist, on=['inc_angle_int'], how='inner')
    #数据质量
    #DDM_POWER
    ddm = ncfile.variables['ddm'][:].data
    power_peak = np.array([np.max(ddm[:,:,i]) for i in range(np.shape(ddm)[2])])
    df['peak_power'] = power_peak
    #center ddm
    #df['sp_ddm'] = ddm[5,5,:]
    #center brcs
    nbrcs = ncfile.variables['nbrcs'][:].data
    df['nbrcs'] = np.sum(nbrcs,axis = (0,1))
    df['brcs'] = df.nbrcs*df.Aeff
    df['Ref_db'] = 10*np.log10(df.brcs*pow((df.Rsr + df.Rts),2)/(4*np.pi*pow((df.Rsr*df.Rts),2)))
    #Pt
    #brcs = ncfile.variables['brcs'][:].data
    #ddm = ncfile.variables['ddm'][:].data
    df = df.replace([np.inf, -np.inf], np.nan).dropna()

    return df[['inc_angle','PRN','lat','lon','Rsr','Rts','snr','peak_power','time','Aeff','nbrcs','brcs','Ref_db']]

    
        
        
#读取GNOS2L1C .NC文件到Dataframe
def Read_GNOS2_L1(path:str):
    """
       读取GNOS2 .HDF文件
       输入：文件路径path(string)：r'/share/public/group_shared/gnssr/GNOSII-Neo/20220406/FY3E_GNOSR_ORBT_L1_20220406_0111_RFLC6_V0.HDF'
       输出：
            格式:DataFrame
    """
    DDM = {'SNR':'Ddm_peak_snr','LES':'Ddm_sp_les','NBRCS':'Ddm_sp_nbrcs','sp_col':'Ddm_sp_column','sp_row':'Ddm_sp_row','qlt':'Ddm_quality_flag'}
    Recevier = {}
    Specular = {'Rsr':'Rx_sp_range','Rts':'Tx_sp_range','Lat':'Sp_lat','Lon':'Sp_lon','inc_angle':'Sp_inc_angle','G*':'Sp_antenna_gain','Land_Type':'Sp_surface_type'}
    Time = {'Sec':'Ddm_gps_second','Week':'Ddm_gps_week','Track':'Ddm_track_id'}
    Transmitter = {'PRN':'Gnss_prn_code'}
    #!下读取要求文件无损坏，可用nc.Dataset读取
    ncfile = nc.Dataset(path)
    #注意上句，无法使用简单try筛出错误文件
    DDMdic = {key:ncfile.groups['DDM'].variables[value][:].data for key,value in DDM.items()}
    Recevierdic = {key:ncfile.groups['Receiver'].variables[value][:].data for key,value in Recevier.items()}
    Speculardic = {key:ncfile.groups['Specular'].variables[value][:].data for key,value in Specular.items()}
    Timedic = {key:ncfile.groups['Time'].variables[value][:].data for key,value in Time.items()}
    Transmitter = {key:ncfile.groups['Transmitter'].variables[value][:].data for key,value in Transmitter.items()}
    df1 = DataFrame(DDMdic)
    df2 = DataFrame(Recevierdic)
    df3 = DataFrame(Speculardic)
    df4 = DataFrame(Transmitter)
    df5 = DataFrame(Timedic)
    df = pd.concat([df2,df1,df3,df4,df5],axis = 1)   
    #反射率计算
    Aeff = ncfile.groups['DDM'].variables['Ddm_effective_area'][:].data
    Aeff = np.power(10,(Aeff/10))
    aeff = Aeff.sum(axis = (0,1))
    df['Aeff'] = aeff
    df['BRCS'] = df.NBRCS*df.Aeff
    #df['Ref'] = df.BRCS*pow((df.Rsr + df.Rts),2)/(4*np.pi*pow((df.Rsr*df.Rts),2))
    df['Ref_db'] = 10*np.log10(df.BRCS*pow((df.Rsr + df.Rts),2)/(4*np.pi*pow((df.Rsr*df.Rts),2)))
    #时间信息提取
    dts = datetime.strptime('80-01-06', '%y-%m-%d')
    td=timedelta(seconds=1)
    df['time']=dts+td*df['Sec']+td*df['Week']*604800
    #预计算网格
    crs_proj = CRS('epsg:6933')
    transg = Transformer.from_crs(crs_proj.geodetic_crs, crs_proj)
    SMAPresolution=36032.22084
    y,x=transg.transform(df["Lat"].values,df["Lon"].values)
    df["x"] = (x//SMAPresolution).astype("int")
    df["y"] = (y//SMAPresolution).astype("int")
    #质量标签提取（后续可更改）
    def qlt(x1):
        if x1==-9999:
            return -1
        else:
            return int(bin(x1).split('b')[1].zfill(19)[-1])
    df['overall_qlt']= df[['qlt']].apply( lambda x: qlt(x.qlt), axis = 1)
    #信号源【BDS or GPS】识别
    df['channel'] = int(path.split('_')[7][-1])
    def NDS(x1):
        if x1 in [1,2,3,4]:
            return 0
        else:
            return 1
    df['isBDS']= df[['channel']].apply( lambda x: NDS(x.channel), axis = 1)

    return df
    

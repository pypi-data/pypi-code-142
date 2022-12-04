# -*- coding: utf-8 -*-
###Default Imports##################################################################################
from dateutil import parser
import os
import numpy as np
import pandas as pd
import pvlib
from pvlib.location import Location
from multiprocessing.pool import ThreadPool

from ccrenew.dashboard import (
    ccr,
    all_df_keys
)
from ccrenew.dashboard.data_processing import solcats_API as Cats 

df_keys = all_df_keys

"""
Imports above docstring to exclude from Sphinx AutoAPI
Created on Fri Sep 24 15:18:49 2021

@author: Chris Downs
"""
'''
purpose:
    support a library of functions that will allow for the transposition of ghi data (or data from a weather api) to POA data.
    include functions to plot calibration metrics (how well does transposed match actual?) how well does weather api match actual ghi, etc
'''
#%%                    ##Thoughts
'''
heiarchy of irradiance data
    1: native functioning POA
    2: neighbor functioning poa from a matching site (within 10 miles, same tilf or gcr, same tracking tech (back vs true))
    3: native site ghi data transposed ot POA (5 MINUTE DATA TRANSPOSED AND RESAMPLED TO HOURLY) dashboard will have an hourly ghi data plot, but transpose on more granular data
    4: neighbor GHI site (doesnt have to match) 5 minute data transposed to poa nd hourly resample
    5: weather API data transposed and resampled to hourly data

'''

#%%                    ##Functions
def simulate_trackers(df_cat, lat, lon, altitude, tz, max_angle, gcr, temp_coef):
   
    #choose tracking algorithm based upon temp_coefficient of the modules
    backtrack=True
    if temp_coef > -0.39:
        backtrack=False
  
    # altitude in meters above sea level.  name is optional, but helpful for documentation
    site_location = Location(lat, lon, altitude=altitude, tz=tz)
     
    solar_position = site_location.get_solarposition(df_cat.index, lat, lon)
    
    tracker_data = pvlib.tracking.singleaxis(solar_position['apparent_zenith'], solar_position['azimuth'],
                                         axis_tilt=0, axis_azimuth=180, max_angle=max_angle,
                                         backtrack=backtrack, gcr=gcr)
    
    #I don't want Na values filled to 0. For ava purposes, 
    #tracking matters when model is not nan, so filters are applied later using this fact
    #tracker_data=tracker_data.fillna(0)
    
    return tracker_data

def half_interval_up(times):
    """
    shift a Datetimeindex forward by half an interval
    """
    shift_quantity=(times[1]-times[0])/2. #get what half a shift would be
    times+=shift_quantity
    return times

def half_interval_down(times):
    """
    shift a Datetimeindex forward by half an interval
    """
    shift_quantity=(times[1]-times[0])/2. #get what half a shift would be
    times-=shift_quantity
    return times

def transpose(surface_tilt, surface_azimuth, albedo, solar_position,
              ghi, dni, dhi, dni_et, airmass, **kwargs):
    """
    Estimate POA irradiance. PVWatts v5 uses a similar but slightly different
    method for near-horizon diffuse irradiance.

    Parameters
    ----------
    surface_tilt, surface_azimuth : numeric
        Array orientation [degrees]
    albedo : numeric
        Ground albedo
    solar_position : pd.DataFrame
        Solar position
    ghi, dni, dhi : numeric
        The three irradiance components
    airmass : numeric
        relative airmass
    dni_et : numeric
        extraterrestrial (top of atmosphere) irradiance
    **kwargs
        Extra arguments passed to ``pvlib.irradiance.get_total_irradiance``.

    Returns
    -------
    poa : pd.DataFrame
        POA irradiance components, including ``poa_global``.
    """
    poa = pvlib.irradiance.get_total_irradiance(
        surface_tilt,
        surface_azimuth,
        solar_position['apparent_zenith'],
        solar_position['azimuth'],
        dni,
        ghi,
        dhi,
        albedo=albedo,
        airmass=airmass,
        dni_extra=dni_et,
        model='perez',
        **kwargs)
    # return the entire dataframe, not just poa_global, for component calculations
    return poa.fillna(0)

def decompose(ghi, lat, lon, elevation, tz, freq):
    """
    decompose the given ghi dataframe into both dhi and dni
    
    Parameters
    ----------
    df: pandas df of ghi data
    lat: Numeric. site latitude as a decimal
    lon: Numeric. site longitude as a decimal
    
    Returns
    -------
    dni
    dhi
    airmass
    dni_et
    """
    
    #site_location = pvlib.location.Location(lat, lon,altitude=elevation,tz=tz)
    # utc_offset = ghi.index[0].tz_localize(tz).utcoffset()
    site_location = Location(lat, lon, tz=tz, altitude=elevation)
    # freq = pd.infer_freq(df.index)
    # times = pd.date_range(start=df.index[0], end=df.index[-1], freq=freq, tz = site_location.tz)
    solar_position = site_location.get_solarposition(times=ghi.index)
    dni_et = pvlib.irradiance.get_extra_radiation(ghi.index)
    airmass = site_location.get_airmass(solar_position=solar_position)['airmass_relative']
    # airmass.index = airmass.index + utc_offset

    zenith=solar_position.apparent_zenith
    #times=df.index  #im pretty sure this line isnt used
    erb=pvlib.irradiance.erbs(ghi, zenith, ghi.index)#GHI data, zenith, datetimes
    dni = erb['dni']
    dhi = erb['dhi']
    
    return ghi,dni,dhi,airmass,dni_et,site_location,solar_position

def get_solcast_data(ccr_id,start,end):
    """
    get data off s3 for solcast data
    
    Parameters
    ----------
    ccr_id: (str) ccr_id as a string
    start: (str) timestamp in form '2022-4-3' for the start of the data request
    end: (str) timestamp in form '2022-4-4' for the end of the data request
    
    Returns
    -------
    df_cat: (df) df of the weather from solcast to nearest day
    """
    
    date_range=pd.date_range(start,end, normalize=True)
    keys = [Cats.make_key(ccr_id, date) for date in date_range]
    
    pool_size = 6
    pool = ThreadPool(pool_size)
    day_df_list = pool.map(Cats.retrieve_df, keys)
    pool.close()
    pool.join()
    
    df_cat = pd.concat(day_df_list, axis=0)
    
    return df_cat

def get_tilt(racking, project, df_cat, lat, lon, altitude, tz, max_angle, gcr, temp_coef):
    #do some cheeky stuff that is racking specific
    if racking =='Fixed':
        tracking=False
        tilt_value=df_keys['Tilt/GCR'].loc[df_keys['Project']==project].item()
        surface_azimuth_value=180
        
        #make even fixed tilts a df of values so every time slot has a value and tz localize works the same for fixed vs trackers
        tilt_data=df_cat.copy()
        tilt_data['surface_tilt']=tilt_value
        tilt_data['surface_azimuth']=surface_azimuth_value
        surface_azimuth=tilt_data.surface_azimuth
        tilt=tilt_data.surface_tilt
        gcr=None
    elif racking =='Tracker':
        tracking=True
        tracker_data=simulate_trackers(df_cat, lat, lon, altitude, tz, max_angle, gcr, temp_coef)
        surface_azimuth=tracker_data.surface_azimuth
        tilt=tracker_data.surface_tilt

    return tilt, surface_azimuth

def solcats_to_dash(project,start,end,resample=True,convert=True):
    """
    parse out solcast data and turn it into poa useable for the dashboard
    
    Parameters
    ----------
    project: (str) string name  for the site from df_keys. same used in project list for the dashboard
    start: (str) timestamp in form '2022-4-3' for the start of the data request
    end: (str) timestamp in form '2022-4-4' for the end of the data request
    resample: (Bool) true to go to hourly, false to stay at 5 minute
    
    Returns
    -------
    df_poa: (df) df of the POA,Tamb, and windspeed values from solcast with units changed to the right format for project
    df_units: (df) just a list of units used since they are converted 
    """
    #get all that ish from df_keys
    ccr_id=df_keys.CCR_ID.loc[df_keys.Project==project].item()
    tz_project='US/'+str(df_keys['Timezone'].loc[df_keys['Project']==project].item())
    tz_utc='UTC'
    lat=df_keys.GPS_Lat.loc[df_keys['Project']==project].item()
    lon=df_keys.GPS_Long.loc[df_keys['Project']==project].item()
    racking=df_keys.Racking.loc[df_keys['Project']==project].item()
    gcr=df_keys['Tilt/GCR'].loc[df_keys['Project']==project].item()
    elevation=df_keys['Elevation'].loc[df_keys['Project']==project].item()
    max_angle=df_keys['Max_angle'].loc[df_keys['Project']==project].item()
    temp_coef=df_keys['Temp_Coeff_Pmax'].loc[df_keys['Project']==project].item()
    axis_tilt=0
    albedo=1

    #pull in the solcast data:
    df_cat= get_solcast_data(ccr_id,start,end)
    freq = pd.infer_freq(df_cat.index)
    df_cat = df_cat.tz_localize(tz_project, ambiguous=True).tz_convert('UTC')
    tilt, surface_azimuth = get_tilt(racking, project, df_cat, lat, lon, elevation, tz_project, max_angle, gcr, temp_coef)

    ghi,dni,dhi,airmass,dni_et,site_location,solar_position=decompose(df_cat['ghi'],lat,lon,elevation,tz_utc,freq) 
    dni=df_cat['dni']
    dhi=df_cat['dhi']
    
    poa_df=transpose(tilt, surface_azimuth, albedo, solar_position, ghi, dni, dhi, dni_et, airmass) 
    df_cat['poa']=poa_df['poa_global']
    df_units=pd.DataFrame(data={'Temp':['Celsius'],'Wind':['m/s']})
    
    #add in a tmod column based on the conversion equation
    #Tmod = Tamb + POA *np.exp( a+ b*wind_speed)
    a_module=df_keys['a_module'].loc[df_keys['Project']==project].item()
    b_module=df_keys['b_module'].loc[df_keys['Project']==project].item()
    df_cat['Tmod']=df_cat['air_temp']+(df_cat['poa']*np.exp(a_module+b_module*df_cat['wind_speed_10m']))
    
    if convert:
        #do conversion of units
        folder=df_keys.Folder.loc[df_keys.Project==project].item()
        config_file =  project + r'_Plant_Config_MACRO.xlsm'
        config_path= os.path.join(ccr.file_project,folder,project,'Plant_Config_File',config_file)
        xl=pd.ExcelFile(config_path)
        df_config=xl.parse('Unit_Tab')
        
        #temp units
        temps=df_config.loc[df_config['Var_ID'].str.contains('amb')]['Convert_Farenheit_to_Celcius'].sum()
        temps+=df_config.loc[df_config['Var_ID'].str.contains('mod')]['Convert_Farenheit_to_Celcius'].sum()
        if temps >0:
            df_cat['Tamb']=df_cat['air_temp']*float((9/5.))+32.0
            df_units['Temp']='Fahrenheit'
            df_cat['Tmod']=df_cat['Tmod']*float((9/5.))+32.0
        else:
            df_cat['Tamb']=df_cat['air_temp']
            
        #wind units
        winds=df_config.loc[df_config['Var_ID'].str.contains('speed')]['Convert_mph_to_mps'].sum()
        if winds>0:
            df_cat['Wind_speed']=df_cat['wind_speed_10m']*float(2.23694)
            df_units['Wind']='Mph'
        else:
            df_cat['Wind_speed']=df_cat['wind_speed_10m']
    else:
        df_cat['Wind_speed']=df_cat['wind_speed_10m']
        df_cat['Tamb']=df_cat['air_temp']
    
    #do resample
    if resample:
        df_cat=df_cat.resample('H').mean().tz_convert(tz_project).tz_localize(None)
        df_cat = df_cat[~df_cat.index.duplicated(keep='first')]

        #correct for static values that solcats reports that the dashboard is gonna turn off.
        df_cat['Correction_factor']=np.where(df_cat.index.hour%2==0, 0.999, 1.001)
        df_cat['Tamb']*=df_cat['Correction_factor']
        df_cat['Tmod']*=df_cat['Correction_factor']
        df_cat['Wind_speed']*=df_cat['Correction_factor']
    return df_cat[['poa','Tamb','Tmod','Wind_speed','ghi']],df_units


def site_s3_to_poa(project,start,end,GHI_index=0,resample=True):
    """
    go get s3 data from s3 and tranpose to useable, pasteable POA data
    
    Parameters
    ----------
    project: (str) string name  for the site from df_keys. same used in project list for the dashboard
    start: (str) timestamp in form '2022-4-3' for the start of the data request
    end: (str) timestamp in form '2022-4-4' for the end of the data request
    GHI_index: (int) ghi iloc to use. 0 will use the first ghi in the list
    resample: (Bool) true to go to hourly, false to stay at 5 minute
    
    Returns
    -------
    df_poa: (df) df of the POA
    """
    #get all that ish from df_keys
    ccr_id=df_keys.CCR_ID.loc[df_keys.Project==project].item()
    tz_project='US/'+str(df_keys['Timezone'].loc[df_keys['Project']==project].item())
    tz_utc='UTC'
    lat=df_keys.GPS_Lat.loc[df_keys['Project']==project].item()
    lon=df_keys.GPS_Long.loc[df_keys['Project']==project].item()
    racking=df_keys.Racking.loc[df_keys['Project']==project].item()
    gcr=df_keys['Tilt/GCR'].loc[df_keys['Project']==project].item()
    elevation=df_keys['Elevation'].loc[df_keys['Project']==project].item()
    max_angle=df_keys['Max_angle'].loc[df_keys['Project']==project].item()
    temp_coef=df_keys['Temp_Coeff_Pmax'].loc[df_keys['Project']==project].item()
    axis_tilt=0
    albedo=1
    
    #pull in the s3 data
    df=Cats.get_df(ccr_id,start,end,prod_data=True)
    freq = pd.infer_freq(df.index)
    df = df.tz_localize(tz_project, ambiguous=True).tz_convert('UTC')

    #get just the one ghi column to use
    ghi_name=[col for col in df.columns if 'GHI' in col][GHI_index]
    
    df_cat=df[ghi_name]
    tilt, surface_azimuth = get_tilt(racking, project, df_cat, lat, lon, elevation, tz_project, max_angle, gcr, temp_coef)

    #decompose so everything is consistent, but just use the regular dni and dhi in solcats
    ghi,dni,dhi,airmass,dni_et,site_location,solar_position=decompose(df_cat,lat,lon,elevation,tz_utc,freq) 
    poa_df=transpose(tilt, surface_azimuth, albedo, solar_position, ghi, dni, dhi, dni_et, airmass) 
    df_poa=poa_df['poa_global']
    
    #do resample
    if resample:
        df_poa=df_poa.resample('H').mean().tz_convert(tz_project).tz_localize(None)
        df_poa = df_poa[~df_poa.index.duplicated(keep='first')]
        
    return df_poa
    
if __name__ == '__main__':
    solcats_to_dash('Lampwick',start='2022-11-6',end='2022-11-6',resample=True,convert=False)
    site_s3_to_poa('Thunderegg',start='2022-1-6',end='2022-11-6')
# -*- coding: utf-8 -*-

from ccrenew.dashboard.utils.logging_conf import get_logging_config
from datetime import datetime
from dateutil import parser
import logging
import logging.config
from matplotlib.pyplot import waitforbuttonpress
from numbers import Number
import numpy as np
import os
import pandas as pd
from pandas import DataFrame
from pandas.io.sql import SQLTable
import pickle
import scipy.stats as sct
import shutil
import sys
import time
import traceback
from typing import Type, Union
import warnings

from ccrenew.dashboard import (
    ccr,
    all_df_keys,
    func_timer)
from ccrenew.dashboard.plotting.plots import Plotter
from ccrenew.dashboard.project import Project
from ccrenew.dashboard.utils.df_tools import df_update_join
import ccrenew.dashboard.utils.dashboard_utils as utils
import ccrenew.dashboard.utils.project_neighbors as neighbs

    
# Python 2 compatibility
if sys.version_info.major == 3:
    unicode = str

# suppress warnings about "A value is trying to be set on a copy of a slice from a DataFrame."
pd.options.mode.chained_assignment = None

# Initialize logger
# Get logging configuration from the logging.conf file in the same directory as this file
username = os.getenv('username')
dashboard_folder = ccr.file_project
log_filename = '{}_dashboard-{}.log'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), username)
log_config = os.path.join(dashboard_folder, 'Python_Functions', 'logging.conf')
log_file = os.path.join(dashboard_folder, 'Python_Functions', '_old', 'logs', log_filename)
LOGGING_CONFIG = get_logging_config(log_file)
logging.config.dictConfig(LOGGING_CONFIG)

# Create logger
logger = logging.getLogger(__name__)
logger.info('Beginning Dashboard Session')

def _execute_insert(self, conn, keys, data_iter):
    #print "Using monkey-patched _execute_insert"
    data = [dict((k, v) for k, v in zip(keys, row)) for row in data_iter]

    # Python 2 compatibility:
    try:
        conn.execute(self.insert_statement().values(data))
    except AttributeError:
        conn.execute(self.table.insert().values(data))
    

SQLTable._execute_insert = _execute_insert

    
class DashboardSession(object):
    """Main orchestrator for processing, plotting, and exporting data for projects (i.e. sites).

    Args:
        project_list (str or list, optional): List of [Projects][ccrenew.dashboard.project.Project] to initialize when initializing the session.
        data_cutoff_date (str or datetime, optional): The last date you want to analyze. Defaults to the current date the dashboard is being run.
        data_source (str, optional): The data source to run the dashboard on.
    """

    # Instantiate globals as class variables
    dashboard_dir = ccr.file_project
    df_keys = all_df_keys

    print('Pulling diagnostic comments from Smartsheets...')
    # Smartsheet comments from previous reporting months. I'm going to hardcode Jan 2021 as the earliest date (column index 69 - Nice) but we can change that easily
    df_ss_comments: pd.DataFrame = ccr.get_ss_as_df('2819883898562436', drop_col_1=False, start_col=69, index_col='Project')

    # Site lists
    tracker_sites = ['5840 Buffalo Road', 'Alexis', 'ATOOD II', 'Bar D', 'Barnhill Road Solar', 'Bay Branch',
                     'Bonanza', 'Bovine Solar', 'Bronson', 'Cascade', 'Chisum', 'Copperfield', 'Curie',
                     'Eddy II', 'Gaston II', 'Griffin', 'Grove Solar (NC)', 'Grove', 'Hardison Farm',
                     'Hopewell Friends', 'Hyline', 'IS - 46 Tracker', 'IS 67', 'Lampwick', 'Leggett Solar',
                     'Mars', 'Neff', 'Nimitz', 'Open Range', 'Palmetto Plains', 'Prince George 1',
                     'Prince George 2', 'Railroad', 'Shoe Creek', 'Siler', 'Simba', 'Springfield', 'Sterling',
                     'Thunderegg', 'Vale', 'Wagyu', 'Warren', 'Wendell', 'West Moore II', 'Yellow Jacket']
    battery_ac_funds = ['LGE']
    battery_ac_sites = df_keys.query("Fund in @battery_ac_funds").index
    battery_dc_sites = ['Salt Point', 'Dubois']
    
    # Type annotations & docstrings for documentation
    df_keys: dict
    """Metadata for all projects."""
    df_ss_comments: dict
    """DataFrame with Smartsheet comments."""
    battery_ac_funds: list
    """Funds with projects with AC batteries."""
    battery_ac_sites: list
    """Projects with AC batteries."""
    battery_dc_sites: list
    """Projects with DC batteries."""
    tracker_sites: list
    """Projects with tracker-type racking."""

    def __init__(self,
                 project_list=None,
                 data_cutoff_date=None,
                 data_source='AE_data_',
                 **kwargs):

        print('Initializing DashboardSession...')
        
        # Initialize a dict to store projects - key = project name; value = project object
        # utils.project_dict() overrides the __repr__ method of dict to pretty print the projects when you call it
        self.project_list = utils.project_dict()

        # Add projects to the session if provided
        if project_list:
            if isinstance(project_list, (str, unicode, list)):
                self.add_projects(project_list)
            else:
                print('`project_list` must be a string or list. The projects provided were not added to the DashboardSession. Please try again in the initialized DashboardSession.')

        # Parse & add data_cutoff_date if provided. Default to current date if not provided or error during parsing 
        if data_cutoff_date:
            try:
                self.data_cutoff_date = parser.parse(data_cutoff_date)
            except:
                self.data_cutoff_date = datetime.today()
        else:
            self.data_cutoff_date = datetime.today()

        # Set data source
        self.data_source = data_source
            
        # Get snow dataframe
        self.raw_snow_df = utils.get_snow_df(dashboard_folder, data_source, file_format='csv')

        # Create list for projects that have errored out
        self.errored_projects = {}

        # List of plotter objects if you want to have multiple going in your session
        self.plotters = {}

        # Type annotations & docstrings for documentation
        self.project_list: list
        """List of [Project][ccrenew.dashboard.project.Project] objects that
        have been initialized & added to the
        [DashboardSession][ccrenew.dashboard.session.DashboardSession] instance."""
        self.raw_snow_df: pd.DataFrame
        """Snow data."""
        self.data_cutoff_date: datetime
        """Last day to process data."""

    def __str__(self):
        return 'DashboardSession object with {} projects'.format(len(self.project_list))


    def __str__(self):
        return 'DashboardSession object with {} projects'.format(len(self.project_list))


    @func_timer
    def add_project(self, project_name, get_neighbors=True):
        """Adds & initializes a [Project][ccrenew.dashboard.project.Project]
        to a [DashboardSession][ccrenew.dashboard.session.DashboardSession] instance.

        Args:
            project_name (str or Project): The name of the project to add to the [DashboardSession][ccrenew.dashboard.session.DashboardSession] instance.
            get_neighbors (bool, optional): Flag to add & initialize neighbor [Projects][ccrenew.dashboard.project.Project].
        """
        # Type validation
        if not isinstance(project_name, (str, unicode, list)):
            raise TypeError("`project_name` must be a string or Python list! Please reformat input and try again.")

        # Determine behavior based on what was passed to method
        if isinstance(project_name, list):
            self.add_projects(project_name)
        elif project_name in self.project_list:
            return
        else:
            try:
                project = self.__initialize_project(project_name, get_neighbors)
                self.project_list[project.project_name] = project
            except RuntimeError as e:
                print(e)
                logger.warn(e)
    

    def add_projects(self, project_list, get_neighbors=True):
        """Calls [add_project()][ccrenew.dashboard.session.DashboardSession.add_project] for each project in a list.

        Args:
            project_list (list, str): list of project names to add & initialize to the [DashboardSession][ccrenew.dashboard.session.DashboardSession] instance.
            get_neighbors (bool, optional): See [add_project()][ccrenew.dashboard.session.DashboardSession.add_project].
        """
        if isinstance(project_list, (str, unicode)):
            self.add_project(project_list, get_neighbors)

        elif isinstance(project_list, list):
            for project_name in project_list:
                self.add_project(project_name, get_neighbors)
        
        else:
            raise TypeError("`project_list` must be a string or Python list! Please reformat input and try again.")
                

    def __initialize_project(self, project_name, get_neighbors=True):
        """Initializes a project object with metadata

        Args:
            project_name (str): Name of a project to initialize.
            get_neighbors (bool, optional): Flag to add & initialize neighbor projects. Defaults to True.

        Returns:
            Project: An initialized Project object
        """

        try:
            df_proj_keys = self.df_keys.query("Project == @project_name").to_dict('records')[0]
            df_proj_ss_comments = self.df_ss_comments.query("index == @project_name").to_dict('records')[0]
        except IndexError:
            # Log that project was not found
            warn_msg = '"{}" not found in df keys. Please verify the project is present in df keys & the spelling is correct and try again'.format(project_name)
            print(warn_msg)
            logger.warn(warn_msg)

            # Remove project from project_list since we won't be able to initialize it
            del self.project_list[project_name]
            return

        if get_neighbors:
            # Find all neighbors that satisfy the distance and equipment requirements
            neighbor_list = neighbs.find_nearby_similar_projects(project_name, print_data=False).index.tolist()
            
            # Then remove the search project from the list
            # (Sometimes it will return an empty list if there is some data missing in `df_keys`) so we need to check if it returned a non-empty list first
            try:
                neighbor_list.remove(project_name)
            except ValueError:
                pass

            # If the project has neighbors, we'll add them to the DashboardSession instance
            # Set get_neighbors to False so we don't get neighbors of neighbors of neighbors etc.
            if neighbor_list:
                self.add_projects(neighbor_list, get_neighbors=False)
        else:
            neighbor_list = None

        Battery_AC_site = project_name in self.battery_ac_sites
        Battery_DC_site = project_name in self.battery_dc_sites
        Tracker_site = project_name in self.tracker_sites
        
        proj_init_dict = {}
        proj_init_dict['project_name'] = project_name
        proj_init_dict['df_proj_keys'] = df_proj_keys
        proj_init_dict['df_proj_ss_comments'] = df_proj_ss_comments
        proj_init_dict['dashboard_dir'] = self.dashboard_dir
        proj_init_dict['data_cutoff_date'] = self.data_cutoff_date
        proj_init_dict['data_source'] = self.data_source
        proj_init_dict['Battery_AC_site'] = Battery_AC_site
        proj_init_dict['Battery_DC_site'] = Battery_DC_site
        proj_init_dict['Tracker_site'] = Tracker_site
        proj_init_dict['raw_snow_df'] = self.raw_snow_df
        proj_init_dict['neighbor_list'] = neighbor_list

        project = Project(proj_init_dict)
        return project


    def get_project(self, project_name, get_neighbors=True):
        """Returns a [Project][ccrenew.dashboard.project.Project] object given a project name.

        Args:
            project_name (str or Project): Name of a [Project][ccrenew.dashboard.project.Project] to return from the
                [DashboardSession][ccrenew.dashboard.session.DashboardSession] instance.
                If project does not yet exist in the session, it will be added then returned.
            get_neighbors (bool, optional): Flag to add & initialize neighbor [Projects][ccrenew.dashboard.project.Project].

        Returns:
            Project: the [Project][ccrenew.dashboard.project.Project] for the given the project name.
                If the project does not exist in the session when the call is made, the project will be initialized & returned.
        """
        if isinstance(project_name, Project):
            return project_name
        try:
            project = self.project_list[project_name]
        except KeyError:
            self.add_project(project_name, get_neighbors)
            project = self.project_list[project_name]
        
        return project


    @func_timer
    def process_project(self, project_name, reprocess=False):
        """Processes data for the given [Project][ccrenew.dashboard.project.Project].

        Args:
            project_name (str or Project): The name of the [Project][ccrenew.dashboard.project.Project] to process.
            reprocess (bool, optional): Whether to reprocess the data. This option will likely
                be uncommon as any changes to a [Project's][ccrenew.dashboard.project.Project] config file or powertrack file will
                automatically reprocess that data. This could be used if any changes are made
                outside of the config/powertrack file or a change is made to a neighbor.
        """
        if isinstance(project_name, list):
            self.process_projects(project_name, reprocess)
        elif isinstance(project_name, (str, unicode, Project)):
            start = time.time()
            print(f'Processing {project_name}....')
            # Get project object
            project = self.get_project(project_name)

            # Pull the last updated dates from the filesystem for the config & Powertrack files
            last_update_config_file = os.path.getmtime(project.config_filepath)
            last_update_powertrack_file = os.path.getmtime(project.powertrack_filepath)

            # Check if the config file or the Powertrack file has been updated.
            # If not we don't need to process.
            if (
                project.last_update_config != last_update_config_file or
                project.last_update_powertrack != last_update_powertrack_file
                ):
                # Pull config and/or Powertrack data
                self.__prepare_source_data(project)
            else:
                if project.processed and not reprocess:
                    print('{} already processed'.format(project.project_name))

                    return project

            # Process data - update neighbor sensors first then process the project
            self.__get_neighbor_sensor_data(project)
            try:
                project._process_data()
            except Exception:
                print('\n')
                print('###########################')
                print(f'{project.project_name} not processed. See below for error information.')
                print(traceback.format_exc())
                print('###########################')

                project.last_update_powertrack = 0
                project.errored = True
                project.error_info = traceback.format_exc()

                return project
            project.processed = True
            project.errored = False
            print('{} successfully processed. Processing time: {:.2f}s'.format(project.project_name, time.time()-start))

            return project
        else:
            raise TypeError("`project_name` must be a string or Project object! Please reformat input and try again.")
    
    
    def process_projects(self, project_list, reprocess=False):
        """Calls [process_project()][ccrenew.dashboard.session.DashboardSession.process_project] for each
        [Project][ccrenew.dashboard.project.Project] in a list.

        Args:
            project_list (list): List of project names of [Project][ccrenew.dashboard.project.Project] objects to process.
            reprocess (bool, optional): See [process_project()][ccrenew.dashboard.session.DashboardSession.process_project].
        """
        if isinstance(project_list, (str, unicode, Project)):
            project_name = project_list
            project = self.process_project(project_name, reprocess)
            return project
        elif isinstance(project_list, list):
            for i, project_name in enumerate(project_list):
                print('*******************************************************')
                print(f'Processing {project_name} - Project {i+1} of {len(project_list)}.')
                print('*******************************************************')
                self.process_project(project_name, reprocess)
        else:
            raise TypeError("`project_list` must be a string or Python list! Please reformat input and try again.")
    

    def process_all_projects(self):
        """Processes all projects in the [project_list][ccrenew.dashboard.session.DashboardSession.project_list]
        for the [DashboardSession][ccrenew.dashboard.session.DashboardSession] instance."""
        # FIXME: add data cutoff date in here in case you want to change that in the middle of a session
        # FIXME: Same with process project object below
        project_list = list(self.project_list.keys())
        self.process_projects(project_list)


    def get_ss_comments(self, project_name:str, num_comments: int=None) -> None:
        """Prints Smartsheet comments for the [Project][ccrenew.dashboard.project.Project].

        Args:
            project_name (str): Name of the [Project][ccrenew.dashboard.project.Project] to pull comments for.
            num_comments (int, optional): Number of comments to show, starting from the
                most recent. I.e. `5` will show the most recent 5 comments in the
                Smartsheet. Defaults to None, which will show all comments starting in Jan 2021.
        """
        project = self.get_project(project_name, get_neighbors=False)
        project.get_ss_comments(num_comments)


    def save_pickle(self, project_name, store_plots=False):
        """Saves the [Project][ccrenew.dashboard.project.Project] to a serialized pickle in its
        [project_directory][ccrenew.dashboard.project.Project.project_directory].

        Args:
            project_name (str or Project): The name of the [Project][ccrenew.dashboard.project.Project] to pickle.
            store_plots(bool, optional): Option to store any plots that have been drawn with the project to the pickle.

        Raises:
            TypeError: if the wrong type is supplied to `project_name`.
        """
        if isinstance(project_name, list):
            self.save_pickles(project_name, store_plots)
        elif isinstance(project_name, (str, Project)):
            project = self.process_project(project_name)
            project.save_pickle(store_plots)
        else:
            raise TypeError("`project_name` must be a string or Project object! Please reformat input and try again.")


    def save_pickles(self, project_list, store_plots=False):
        """Calls [pickle_project()][ccrenew.dashboard.session.DashboardSession.pickle_project]
        for each [Project][ccrenew.dashboard.project.Project] in a list.

        Args:
            project_list (list, str, or Project): List of [Project][ccrenew.dashboard.project.Project] names to pickle.
            year (int, optional): See [pickle_project()][ccrenew.dashboard.session.DashboardSession.pickle_project].
            store_plots (bool, optional): See [pickle_project()][ccrenew.dashboard.session.DashboardSession.pickle_project].
        """
        if isinstance(project_list, (str, Project)):
            project_name = project_list
            self.save_pickle(project_name, store_plots)
        elif isinstance(project_list, list):
            for i, project_name in enumerate(project_list):
                print('*******************************************************')
                print(f'Pickling {project_name} - Project {i+1} of {len(project_list)}.')
                print('*******************************************************')
                self.save_pickle(project_name, store_plots)
        else:
            raise TypeError("`project_list` must be a string or Python list! Please reformat input and try again.")


    def pickle_project(self, project_name, store_plots=False):
        """Alias for [save_pickle][ccrenew.dashboard.session.DashboardSession.save_pickle].
        
        Raises:
            FutureWarning: This method will be deprecated in a future version. Use [save_pickle][ccrenew.dashboard.session.DashboardSession.save_pickle] instead.
        """

        warnings.warn('pickle_project will be deprecated in a future version. Please use `save_pickle` instead', FutureWarning)
        self.save_pickle(project_name, store_plots)


    def pickle_projects(self, project_list, store_plots=False):
        """Alias for [save_pickles][ccrenew.dashboard.session.DashboardSession.save_pickles].
        Raises:
            FutureWarning: This method will be deprecated in a future version. Use [save_pickle][ccrenew.dashboard.session.DashboardSession.save_pickle] instead.
        warnings.warn('pickle_project will be deprecated in a future version. Please use `save_pickles` instead', FutureWarning)
        """
        self.save_pickles(project_list, store_plots)


    def load_pickle(self, project_name, year=None, data_cutoff_date=None, show_plots=False):
        """Loads a pickled [Project][ccrenew.dashboard.project.Project] from file.

        Args:
            project_name (str): The name of the [Project][ccrenew.dashboard.project.Project] to load.
            year (int, optional): Year to load for the pickle. Defaults to None, which pulls the pickle for the current year.
            data_cutoff_date (str or datetime): Cutoff date for the [Project][ccrenew.dashboard.project.Project]. When
                loading a project that was pickled some time ago the [data_cutoff_date][ccrenew.dashboard.session.DashboardSession.data_cutoff_date]
                could prevent the data from loading to the current date. Default is None,
                which will reset the [data_cutoff_date][ccrenew.dashboard.session.DashboardSession.data_cutoff_date] to the current day.
            show_plots (bool, optional): Option to show plots if pickle was stored with plots saved.
        """
        if not year:
            year = datetime.now().year
        try:
            project_directory = self.df_keys.query("Project == @project_name")['Folder'].item()
        except IndexError:
            # Log that project was not found
            warn_msg = '"{}" not found in df keys. Please verify the project is present in df keys & the spelling is correct and try again'.format(project_name)
            print(warn_msg)
            logger.warn(warn_msg)
            return

        pickle_jar = os.path.join(self.dashboard_dir,
                                  project_directory,
                                  project_name,
                                  'Pickle_Jar')
        
        pickle_name = utils.picklefy_project_name(project_name)
        pickle_file = str(year) + "_" + pickle_name + ".pickle"
        pickle_path = os.path.join(pickle_jar, pickle_file)
        
        with open(pickle_path, 'rb') as f:
            project = pickle.load(f)

        # Remove plotter object if show_plots=False
        if not show_plots and project.plotter:
            project.plotter.close_plots()

        # Update filepaths to work for any user
        project = self.__update_project_filepaths(project)

        # Update data cutoff date if not explicitly supplied
        if data_cutoff_date:
            try:
                self.data_cutoff_date = parser.parse(data_cutoff_date)
            except:
                self.data_cutoff_date = datetime.today()
        else:
            self.data_cutoff_date = datetime.today()

        # Add project to project_list
        self.project_list[project_name] = project

        return project


    def load_pickles(self, project_list, year=None, data_cutoff_date=None, show_plots=False):
        """Calls [load_pickle()][ccrenew.dashboard.session.DashboardSession.load_pickle]
        for each [Project][ccrenew.dashboard.project.Project] in a list.

        Args:
            project_list (list): List of project names to load.
            year (int): See [load_pickle()][ccrenew.dashboard.session.DashboardSession.load_pickle]
            data_cutoff_date (str or datetime): See [load_pickle()][ccrenew.dashboard.session.DashboardSession.load_pickle]
            show_plots (bool): See [load_pickle()][ccrenew.dashboard.session.DashboardSession.load_pickle]
        """
        if isinstance(project_list, str):
            project_name = project_list
            self.load_pickle(project_name, year, data_cutoff_date, show_plots)
            return
        elif isinstance(project_list, list):
            for project_name in project_list:
                try:
                    project = self.load_pickle(project_name, year, data_cutoff_date, show_plots)
                    project.plotter = None
                except Exception as e:
                    print(e)
                    continue
        else:
            raise TypeError("`project_name` must be a string or Python list! Please reformat input and try again.")


    def draw_plots(self, project_name, plot_order=None, *args, **kwargs):
        """Draws plots for the given project.

        Args:
            project_name (str, Project, or list): A project name or list of project names
                to draw plots on for analysis. If a list is supplied it will plot
                the projects one-by-one. The user must press a button in the final
                plot of each project to move on to the next one.
            plot_order (list or str, optional): A list of plots to draw. This can
                be any number of plots from one to all. Defaults to None, which will draw the below plots in the order listed.

        Default Plot Order

        | Plot Alias                | Plot Description                                          |
        |---------------------------|-----------------------------------------------------------|
        |    ``xplot_pwr_poa``      |    Crossplot of power meter & POA data                    |
        |    ``xplot_temp``         |    Crossplot of power meter & POA data, colored by Tamb   |
        |    ``temps``              |    Tcell temperature comparison                           |
        |    ``inv``                |    Inverters                                              |
        |    ``pr``                 |    Hourly Performance Ratio                               |
        |    ``8760``               |    Meter Corrected vs 8760                                |
        |    ``weather``            |    Weather sensors                                        |
        |    ``mtr_corrected``      |    Meter corrections                                      |
        |    ``mtr_dif``            |    Meter correction dif                                   |
        |    ``poas``               |    POA sensors                                            |
        |    ``pwr_poa``            |    Power meter & POA Avg timeseries plot                  |
        |    ``ghi``                |    GHI sensors                                            |
        |    ``irrad``              |    POA & GHI sensors                                      |
        |    ``tz``                 |    Timezone check                                         |
        |    ``losses``             |    Losses  by type                                        |
        |    ``poa_corr``           |    POA correlation check                                  |

        Other Optional Plots

        | Plot Alias                | Plot Description                                          |
        |---------------------------|-----------------------------------------------------------|
        |    ``meters``             |    Original & corrected power and cumulative meters       |
        |    ``native``             |    Native POA/GHI/Tamb/Tmod/Wind sensor subplots          |

        Keyword Args:
            mth (int): The month to show on the Power vs POA crossplot. Defaults to current month.
            default_tool (str): The default tool for navigating around the plots. Options
                are `zoom` and `pan`. Defaults to `zoom`.
            redraw (bool): Option to force the session to redraw the plots.
            open_folder (bool): Option to open the project's folder on the filesystem. Defaults to False.
            close_plots (bool, str, or list): Option to close all or selected open plots.
                If set to True all plots will be closed. If a plot alias or list of plot
                aliases are provided only those plots will be closed. Defaults to True.
            min_date (int, str, or datetime): Option to set a minimum date on the timeseries
                plots. If an integer is supplied the minimum date will be se to that
                many days previous to the current date. If a datetime or string representation
                of a datetime is supplied it will set the minimum date to that date. Defaults to None.
            fullscreen (bool): Option to show plots as fullscreen. Defaults to True.
            screen (int): 1-based index of screen to draw plots on. I.e. a workstation
                with 3 monitors would accept 1, 2, or 3 as an argument.
            poa_onboarding (bool): Plots POA correlation for all months instead of the
                selected month. Defaults to False.
        """
        if isinstance(project_name, (str, unicode, Project)):
            redraw = kwargs.get('redraw', False)
            project = self.process_project(project_name)
            try:
                if project.errored:
                    raise Exception(f'{project.project_name} encountered an error while processing. Plots cannot be drawn at the moment. To investigate information on the error call `project.error_info`')
            except AttributeError:
                project.errored = False

            if not redraw:
                # Check if the project has an active plotter object & if the plot order is the same
                if project.plotter and project.plotter.plot_list == plot_order:
                    print('Plots already drawn. Add a new plot to the `plot_list` attribute or set `redraw` = True if you\'d like to redraw the current plots')
                    return
                else:
                    self.__draw_plots(project, plot_order, *args, **kwargs)
            else:
                self.__draw_plots(project, plot_order, *args, **kwargs)
        elif isinstance(project_name, list):
            project_list = project_name
            project_count = len(project_list)
            for i, project_name in enumerate(project_list):
                project = self.get_project(project_name, get_neighbors=False)
                self.draw_plots(project.project_name, *args, **kwargs)
                try:
                    print('Press any key in the last plot window to show plots for {}'.format(project_list[i+1]))
                except IndexError:
                    print('Last plot in the list')
                while True:
                    if i+1 == project_count:
                        break
                    if waitforbuttonpress():
                        break


    def __draw_plots(self, project, plot_order, *args, **kwargs):
        """Private method to orchestrate drawing of plots

        Args:
            project (Project): A project to use to draw plots for analysis
        """
        project_name = project.project_name
        close_plots = kwargs.get('close_plots', True)
        if not project.plotter:
            project.plotter = Plotter(project, *args, **kwargs)
        if close_plots:
            project.plotter.close_plots()
        self.plotters[project_name] = project.plotter
                
        project.plotter.draw_dashboard_plots(plot_order, *args, **kwargs)


    def __update_project_filepaths(self, project):
        """Sets filepaths for config file, Powertrack file, and Pickle Jar

        Args:
            project (Project): A `ccrenew.dashboard.project.Project`

        Returns:
            Project: a `ccrenew.dashboard.project.Project` with updated filepaths
        """
        
        # Update filepath references for the project
        project.dashboard_dir = self.dashboard_dir

        # Build filename for config file
        config_filename = project.project_name + r'_Plant_Config_MACRO.xlsm'
        project.config_filepath = os.path.join(project.dashboard_dir,
                                        project.project_directory,
                                        project.project_name,
                                       'Plant_Config_File',
                                        config_filename)

        # Find Powertrack file
        project.data_AE_dir = os.path.join(project.dashboard_dir,
                                        project.project_directory,
                                        project.project_name,
                                        'Powertrack_data')
        project.data_AE_all_files = [f for f in os.listdir(project.data_AE_dir) if os.path.isfile(os.path.join(project.data_AE_dir, f))]
        data_AE = [s for s in project.data_AE_all_files if project.data_source in s]

        # Build filename for Powertrack file
        project.powertrack_filepath = os.path.join(project.dashboard_dir, project.project_directory, project.project_name, 'Powertrack_data', data_AE[0])

        # Check for pickle jar folder & create if it doesn't exist
        project.pickle_jar = os.path.join(project.dashboard_dir,
                                       project.project_directory,
                                       project.project_name,
                                       'Pickle_Jar')
        
        return project
    

    def __prepare_source_data(self, project):

        # Update config file
        # If the config file hasn't been updated it will use the data that's already been pulled
        # If the config file has been updated it will read the file & update the data
        self.__update_project_config(project)

        # Load powertrack data
        # If the powertrack file hasn't been updated it will use the data that's already been pulled
        # If the powertrack file has been updated it will read the file & update the data
        project.load_production_data()
    

    def __update_project_config(self, project):
        
        # Store the list of sensors before pulling the config file
        sensors = project.Get_Sensor
        project._parse_config_file()

        # Check if new neighbor sensors have been added to the config & pull them if so
        if not sensors.equals(project.Get_Sensor):
            project._find_neighbor_sensors()
            self.__get_neighbor_sensor_data(project)
            
            
    def __get_neighbor_sensor_data(self, project):
        for neighbor_name in project.neighbor_sensors:
            # Update production data from neighbor
            try:
                neighbor = self.get_project(neighbor_name, get_neighbors=False)
            except KeyError:
                print('Neighbor for {} not found: {}. Sensor data for the neighbor will be blank. Check logs to determine why neighbor was not added to DashboardSession'.format(project.project_name, neighbor_name))
                continue
            
            # Reload neighbor's config or powertrack files if needed
            self.__prepare_source_data(neighbor)

            # Find the columns needed from the neighbor
            sensor_cols = project.Get_Sensor.loc[project.Get_Sensor['Source'] == neighbor_name, 'Value'].tolist()

            # Get the columns from the neighbor
            try:
                neighbor_df = neighbor.df.reindex(index=project.df.index, columns=sensor_cols)
            # If the production data hasn't been loaded for the project
            except AttributeError:
                neighbor.load_production_data()
                neighbor_df = neighbor.df.reindex(index=project.df.index, columns=sensor_cols)
            # If the neighbor errored out during initialization we'll just create a blank df for the neighbor
            except NameError:
                neighbor_cols = [col + '_' + neighbor_name for col in sensor_cols]
                project.df = project.df.reindex(columns = project.df.columns.tolist() + neighbor_cols)
                project.df_sensor_ON = project.df_sensor_ON.reindex(columns = project.df_sensor_ON.columns.tolist() + neighbor_cols)
                return

            neighbor_df.rename(columns=lambda x: np.str(x) + '_' + neighbor_name, inplace=True)
            neighbor_sensor_ON = neighbor.df_sensor_ON.reindex(index=project.df_sensor_ON.index, columns=sensor_cols)
            neighbor_sensor_ON.columns = neighbor_df.columns.tolist()

            df_cols = project.df.columns.tolist()
            project.df = df_update_join(project.df, neighbor_df)
            # project.df = project.df[df_cols + neighbor_df.columns.tolist()]

            # Add the neighbor columns to the positional references
            project._locate_column_positions()

            project.df_sensor_ON = df_update_join(project.df_sensor_ON, neighbor_sensor_ON)
            project.df_sensor_ON = project.df_sensor_ON.reindex(columns=project.df.columns.tolist())

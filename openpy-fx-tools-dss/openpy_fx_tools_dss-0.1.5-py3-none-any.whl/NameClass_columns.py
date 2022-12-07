# -*- coding: utf-8 -*-
# @Time    : 11/11/2022
# @Author  : Jorge Lara
# @Email   : jlara@iee.unsj.edu.ar
# @File    : NameClass_columns.py
# @Software: PyCharm


list_General_DSS = [
    'WireData', 'LineSpacing', 'LineGeometry', 'LineCode', 'XfmrCode', 'CNData', 'GrowthShape', 'LoadShape',
    'PriceShape', 'Spectrum', 'TCC_Curve', 'TSData', 'TShape', 'XYcurve']
dict_General = dict()
dict_General['LineCode'] = [
    'nphases', 'r1', 'x1', 'r0', 'x0', 'C1', 'C0', 'units', 'rmatrix', 'xmatrix', 'cmatrix', 'baseFreq', 'normamps',
    'emergamps', 'faultrate', 'pctperm', 'repair', 'Kron', 'Rg', 'Xg', 'rho', 'neutral', 'B1', 'B0', 'Seasons',
    'Ratings', 'LineType', 'like']
dict_General['LoadShape'] = [
    'npts', 'interval', 'mult', 'hour', 'mean', 'stddev', 'csvfile', 'sngfile', 'dblfile', 'action', 'qmult',
    'UseActual', 'Pmax', 'Qmax', 'sinterval', 'minterval', 'Pbase', 'Qbase', 'Pmult', 'PQCSVFile', 'MemoryMapping',
    'like']
dict_General['TShape'] = [
    'npts', 'interval', 'temp', 'hour', 'mean', 'stddev', 'csvfile', 'sngfile', 'dblfile', 'sinterval', 'minterval',
    'action', 'like']
dict_General['PriceShape'] = [
    'npts', 'interval', 'price', 'hour', 'mean', 'stddev', 'csvfile', 'sngfile', 'dblfile', 'sinterval', 'minterval',
    'action', 'like']
dict_General['XYcurve'] = [
    'npts', 'Points', 'Yarray', 'Xarray', 'csvfile', 'sngfile', 'dblfile', 'x', 'y', 'Xshift', 'Yshift', 'Xscale',
    'Yscale', 'like']
dict_General['GrowthShape'] = ['npts', 'year', 'mult', 'csvfile', 'sngfile', 'dblfile', 'like']
dict_General['TCC_Curve'] = ['npts', 'C_array', 'T_array', 'like']
dict_General['Spectrum'] = ['NumHarm', 'harmonic', '%mag', 'angle', 'CSVFile', 'like']
dict_General['WireData'] = [
    'Rdc', 'Rac', 'Runits', 'GMRac', 'GMRunits', 'radius', 'radunits', 'normamps', 'emergamps', 'diam', 'Seasons',
    'Ratings', 'Capradius', 'like']
dict_General['CNData'] = [
    'k', 'DiaStrand', 'GmrStrand', 'Rstrand', 'EpsR', 'InsLayer', 'DiaIns', 'DiaCable', 'Rdc', 'Rac', 'Runits', 'GMRac',
    'GMRunits', 'radius', 'radunits', 'normamps', 'emergamps', 'diam', 'Seasons', 'Ratings', 'Capradius', 'like']
dict_General['TSData'] = [
    'DiaShield', 'TapeLayer', 'TapeLap', 'EpsR', 'InsLayer', 'DiaIns', 'DiaCable', 'Rdc', 'Rac', 'Runits', 'GMRac',
    'GMRunits', 'radius', 'radunits', 'normamps', 'emergamps', 'diam', 'Seasons', 'Ratings', 'Capradius', 'like']
dict_General['LineGeometry'] = [
    'nconds', 'nphases', 'cond', 'wire', 'x', 'h', 'units', 'normamps', 'emergamps', 'reduce', 'spacing', 'wires',
    'cncable', 'tscable', 'cncables', 'tscables', 'Seasons', 'Ratings', 'LineType', 'like']
dict_General['LineSpacing'] = ['nconds', 'nphases', 'x', 'h', 'units', 'like']
dict_General['XfmrCode'] = [
    'phases', 'windings', 'wdg', 'conn', 'kV', 'kVA', 'tap', '%R', 'Rneut', 'Xneut', 'conns', 'kVs', 'kVAs', 'taps',
    'Xhl', 'Xht', 'Xlt', 'Xscarray', 'thermal', 'n', 'm', 'flrise', 'hsrise', '%loadloss', '%noloadloss', 'normhkVA',
    'emerghkVA', 'MaxTap', 'MinTap', 'NumTaps', '%imag', 'ppm_antifloat', '%Rs', 'X12', 'X13', 'X23', 'RdcOhms',
    'Seasons', 'Ratings', 'like']

list_Other_DSS = ['Vsource', 'Fault', 'GICsource', 'Isource']
dict_Other = dict()
dict_Other['Vsource'] = [
    'bus1', 'basekv', 'pu', 'angle', 'frequency', 'phases', 'MVAsc3', 'MVAsc1', 'x1r1', 'x0r0', 'Isc3', 'Isc1', 'R1',
    'X1', 'R0', 'X0', 'ScanType', 'Sequence', 'bus2', 'Z1', 'Z0', 'Z2', 'puZ1', 'puZ0', 'puZ2', 'baseMVA', 'Yearly',
    'Daily', 'Duty', 'Model', 'puZideal', 'spectrum', 'basefreq', 'enabled', 'like']
dict_Other['Fault'] = [
    'bus1', 'bus2', 'phases', 'r', '%stddev', 'Gmatrix', 'ONtime', 'temporary', 'MinAmps', 'normamps', 'emergamps',
    'faultrate', 'pctperm', 'repair', 'basefreq', 'enabled', 'like']
dict_Other['GICsource'] = [
    'Description', 'Volts', 'angle', 'frequency', 'phases', 'EN', 'EE', 'Lat1', 'Lon1', 'Lat2', 'Lon2', 'spectrum',
    'basefreq', 'enabled', 'like']
dict_Other['Isource'] = [
    'bus1', 'amps', 'angle', 'frequency', 'phases', 'scantype', 'sequence', 'Yearly', 'Daily', 'Duty', 'Bus2',
    'spectrum', 'basefreq', 'enabled', 'like']

list_PD_elements_DSS = ['Transformer', 'Line', 'Capacitor', 'AutoTrans', 'GICTransformer', 'Reactor']
dict_PD_elem = dict()
dict_PD_elem['Transformer'] = [
    'phases', 'windings', 'XfmrCode', 'buses', 'conns', 'kVs', 'kVAs', 'taps', '%Rs', 'MaxTap', 'MinTap', 'NumTaps',
    'normamps', 'emergamps', 'normhkVA', 'emerghkVA', 'wdg', 'bus', 'conn', 'kV', 'kVA', 'tap', '%R', 'Rneut', 'Xneut',
    'RdcOhms', 'XHL', 'XHT', 'XLT', 'X12', 'X13', 'X23', '%loadloss', '%noloadloss', 'Xscarray', 'thermal', 'n', 'm',
    'flrise', 'hsrise', 'sub', 'subname', '%imag', 'ppm_antifloat', 'bank', 'XRConst', 'LeadLag', 'WdgCurrents', 'Core',
    'Seasons', 'Ratings', 'faultrate', 'pctperm', 'repair', 'basefreq', 'enabled', 'like']
dict_PD_elem['Line'] = [
    'bus1', 'bus2', 'linecode', 'length', 'phases', 'r1', 'x1', 'r0', 'x0', 'C1', 'C0', 'rmatrix', 'xmatrix', 'cmatrix',
    'Switch', 'Rg', 'Xg', 'rho', 'geometry', 'units', 'spacing', 'wires', 'EarthModel', 'cncables', 'tscables', 'B1',
    'B0', 'Seasons', 'Ratings', 'LineType', 'normamps', 'emergamps', 'faultrate', 'pctperm', 'repair', 'basefreq',
    'enabled', 'like']
dict_PD_elem['Capacitor'] = [
    'bus1', 'bus2', 'phases', 'kvar', 'kv', 'conn', 'cmatrix', 'cuf', 'R', 'XL', 'Harm', 'Numsteps', 'states',
    'normamps', 'emergamps', 'faultrate', 'pctperm', 'repair', 'basefreq', 'enabled', 'like']
dict_PD_elem['AutoTrans'] = [
    'phases', 'windings', 'wdg', 'bus', 'conn', 'kV', 'kVA', 'tap', '%R', 'Rdcohms', 'Core', 'buses', 'conns', 'kVs',
    'kVAs', 'taps', 'XHX', 'XHT', 'XXT', 'XSCarray', 'thermal', 'n', 'm', 'flrise', 'hsrise', '%loadloss',
    '%noloadloss', 'normhkVA', 'emerghkVA', 'sub', 'MaxTap', 'MinTap', 'NumTaps', 'subname', '%imag', 'ppm_antifloat',
    '%Rs', 'bank', 'XfmrCode', 'XRConst', 'LeadLag', 'WdgCurrents', 'normamps', 'emergamps', 'faultrate', 'pctperm',
    'repair', 'basefreq', 'enabled', 'like']
dict_PD_elem['GICTransformer'] = [
    'BusH', 'BusNH', 'BusX', 'BusNX', 'phases', 'Type', 'R1', 'R2', 'KVLL1', 'KVLL2', 'MVA', 'VarCurve', '%R1', '%R2',
    'K', 'normamps', 'emergamps', 'faultrate', 'pctperm', 'repair', 'basefreq', 'enabled', 'like']
dict_PD_elem['Reactor'] = [
    'bus1', 'bus2', 'phases', 'kvar', 'kv', 'conn', 'Rmatrix', 'Xmatrix', 'Parallel', 'R', 'X', 'Rp', 'Z1', 'Z2', 'Z0',
    'Z', 'RCurve', 'LCurve', 'LmH', 'normamps', 'emergamps', 'faultrate', 'pctperm', 'repair', 'basefreq', 'enabled',
    'like']

list_PC_elements_DSS = [
    'Generator', 'Generic5', 'GICLine', 'IndMach012', 'Load', 'PVSystem', 'Storage', 'UPFC', 'VCCS', 'VSConverter',
    'WindGen']
dict_PC_elem = dict()
dict_PC_elem['Generator'] = [
    'phases', 'bus1', 'kv', 'kW', 'pf', 'kvar', 'model', 'Vminpu', 'Vmaxpu', 'yearly', 'daily', 'duty', 'dispmode',
    'dispvalue', 'conn', 'Rneut', 'Xneut', 'status', 'class', 'Vpu', 'maxkvar', 'minkvar', 'pvfactor', 'forceon', 'kVA',
    'MVA', 'Xd', 'Xdp', 'Xdpp', 'H', 'D', 'UserModel', 'UserData', 'ShaftModel', 'ShaftData', 'DutyStart', 'debugtrace',
    'Balanced', 'XRdp', 'UseFuel', 'FuelkWh', '%Fuel', '%Reserve', 'Refuel', 'spectrum', 'basefreq', 'enabled', 'like']
dict_PC_elem['Generic5'] = [
    'phases', 'bus1', 'kv', 'kW', 'pf', 'conn', 'kVA', 'H', 'D', 'P_ref1kW', 'P_ref2kW', 'P_ref3kW', 'V_ref1kVLN',
    'V_ref2kVLN', 'V_ref3kVLN', 'MaxSlip', 'SlipOption', 'Yearly', 'Daily', 'Duty', 'Debugtrace', 'P_refkW',
    'Q_refkVAr', 'Cluster_num', 'V_refkVLN', 'ctrl_mode', 'QV_flag', 'kcd', 'kcq', 'kqi', 'Q_ref1kVAr', 'Q_ref2kVAr',
    'Q_ref3kVAr', 'PmaxkW', 'PminkW', 'PQpriority', 'PmppkW', 'Pfctr1', 'Pfctr2', 'Pfctr3', 'Pfctr4', 'Pfctr5',
    'Pfctr6', 'PbiaskW', 'CC_Switch', 'kcq_drp2', 'Volt_Trhd', 'droop', 'spectrum', 'basefreq', 'enabled', 'like']
dict_PC_elem['GICLine'] = [
    'bus1', 'bus2', 'Volts', 'Angle', 'frequency', 'phases', 'R', 'X', 'C', 'EN', 'EE', 'Lat1', 'Lon1', 'Lat2', 'Lon2',
    'spectrum', 'basefreq', 'enabled', 'like']
dict_PC_elem['IndMach012'] = [
    'phases', 'bus1', 'kv', 'kW', 'pf', 'conn', 'kVA', 'H', 'D', 'puRs', 'puXs', 'puRr', 'puXr', 'puXm', 'Slip',
    'MaxSlip', 'SlipOption', 'Yearly', 'Daily', 'Duty', 'Debugtrace', 'spectrum', 'basefreq', 'enabled', 'like']
dict_PC_elem['Load'] = [
    'phases', 'bus1', 'kV', 'kW', 'kvar', 'kVA', 'pf', 'model', 'yearly', 'daily', 'duty', 'growth', 'conn', 'Rneut',
    'Xneut', 'status', 'class', 'Vminpu', 'Vmaxpu', 'Vminnorm', 'Vminemerg', 'xfkVA', 'allocationfactor', '%mean',
    '%stddev', 'CVRwatts', 'CVRvars', 'kwh', 'kwhdays', 'Cfactor', 'CVRcurve', 'NumCust', 'ZIPV', '%SeriesRL',
    'RelWeight', 'Vlowpu', 'puXharm', 'XRharm', 'spectrum', 'basefreq', 'enabled', 'like']
dict_PC_elem['PVSystem'] = [
    'phases', 'bus1', 'kv', 'irradiance', 'Pmpp', '%Pmpp', 'Temperature', 'pf', 'conn', 'kvar', 'kVA', '%Cutin',
    '%Cutout', 'EffCurve', 'P-TCurve', '%R', '%X', 'model', 'Vminpu', 'Vmaxpu', 'Balanced', 'LimitCurrent', 'yearly',
    'daily', 'duty', 'Tyearly', 'Tdaily', 'Tduty', 'class', 'UserModel', 'UserData', 'debugtrace', 'VarFollowInverter',
    'DutyStart', 'WattPriority', 'PFPriority', '%PminNoVars', '%PminkvarMax', 'kvarMax', 'kvarMaxAbs', 'spectrum',
    'basefreq', 'enabled', 'like']
dict_PC_elem['Storage'] = [
    'phases', 'bus1', 'kv', 'conn', 'kW', 'kvar', 'pf', 'kVA', '%Cutin', '%Cutout', 'EffCurve', 'VarFollowInverter',
    'kvarMax', 'kvarMaxAbs', 'WattPriority', 'PFPriority', '%PminNoVars', '%PminkvarMax', 'kWrated', '%kWrated',
    'kWhrated', 'kWhstored', '%stored', '%reserve', 'State', '%Discharge', '%Charge', '%EffCharge', '%EffDischarge',
    '%IdlingkW', '%Idlingkvar', '%R', '%X', 'model', 'Vminpu', 'Vmaxpu', 'Balanced', 'LimitCurrent', 'yearly', 'daily',
    'duty', 'DispMode', 'DischargeTrigger', 'ChargeTrigger', 'TimeChargeTrig', 'class', 'DynaDLL', 'DynaData',
    'UserModel', 'UserData', 'debugtrace', 'spectrum', 'basefreq', 'enabled', 'like']
dict_PC_elem['UPFC'] = [
    'bus1', 'bus2', 'refkv', 'pf', 'frequency', 'phases', 'Xs', 'Tol1', 'Mode', 'VpqMax', 'LossCurve', 'VHLimit',
    'VLLimit', 'CLimit', 'refkv2', 'kvarLimit', 'spectrum', 'basefreq', 'enabled', 'like']
dict_PC_elem['VCCS'] = [
    'bus1', 'phases', 'prated', 'vrated', 'ppct', 'bp1', 'bp2', 'filter', 'fsample', 'rmsmode', 'imaxpu', 'vrmstau',
    'irmstau', 'spectrum', 'basefreq', 'enabled', 'like']
dict_PC_elem['VSConverter'] = [
    'phases', 'Bus1', 'kVac', 'kVdc', 'kW', 'Ndc', 'Rac', 'Xac', 'm0', 'd0', 'Mmin', 'Mmax', 'Iacmax', 'Idcmax',
    'Vacref', 'Pacref', 'Qacref', 'Vdcref', 'VscMode', 'spectrum', 'basefreq', 'enabled', 'like']
dict_PC_elem['WindGen'] = [
    'phases', 'bus1', 'kv', 'kW', 'PF', 'model', 'yearly', 'daily', 'duty', 'conn', 'kvar', 'status', 'class', 'Vpu',
    'maxkvar', 'minkvar', 'pvfactor', 'debugtrace', 'Vminpu', 'Vmaxpu', 'forceon', 'kVA', 'MVA', 'Xd', 'Xdp', 'Xdpp',
    'H', 'D', 'UserModel', 'UserData', 'ShaftModel', 'ShaftData', 'DutyStart', 'Balanced', 'XRdp', 'spectrum',
    'basefreq', 'enabled', 'like']

list_Controls_DSS = [
    'CapControl', 'ESPVLControl', 'ExpControl', 'Fuse', 'GenDispatcher', 'InvControl', 'Recloser', 'RegControl',
    'Relay', 'StorageController', 'SwtControl', 'UPFCControl']
dict_Control = dict()
dict_Control['CapControl'] = [
    'element', 'terminal', 'capacitor', 'type', 'PTratio', 'CTratio', 'ONsetting', 'OFFsetting', 'Delay',
    'VoltOverride', 'Vmax', 'Vmin', 'DelayOFF', 'DeadTime', 'CTPhase', 'PTPhase', 'VBus', 'EventLog', 'UserModel',
    'UserData', 'pctMinkvar', 'Reset', 'basefreq', 'enabled', 'like']
dict_Control['ESPVLControl'] = [
    'Element', 'Terminal', 'Type', 'kWBand', 'kvarlimit', 'LocalControlList', 'LocalControlWeights', 'PVSystemList',
    'PVSystemWeights', 'StorageList', 'StorageWeights', 'Forecast', 'basefreq', 'enabled', 'like']
dict_Control['ExpControl'] = [
    'PVSystemList', 'Vreg', 'Slope', 'VregTau', 'Qbias', 'VregMin', 'VregMax', 'QmaxLead', 'QmaxLag', 'EventLog',
    'DeltaQ_factor', 'PreferQ', 'Tresponse', 'basefreq', 'enabled', 'like']
dict_Control['Fuse'] = [
    'MonitoredObj', 'MonitoredTerm', 'SwitchedObj', 'SwitchedTerm', 'FuseCurve', 'RatedCurrent', 'Delay', 'Action',
    'Normal', 'State', 'basefreq', 'enabled', 'like']
dict_Control['GenDispatcher'] = [
    'Element', 'Terminal', 'kWLimit', 'kWBand', 'kvarlimit', 'GenList', 'basefreq', 'enabled', 'like']
dict_Control['InvControl'] = [
    'DERList', 'Mode', 'CombiMode', 'vvc_curve1', 'hysteresis_offset', 'voltage_curvex_ref', 'avgwindowlen',
    'voltwatt_curve', 'DbVMin', 'DbVMax', 'ArGraLowV', 'ArGraHiV', 'DynReacavgwindowlen', 'deltaQ_Factor',
    'VoltageChangeTolerance', 'VarChangeTolerance', 'VoltwattYAxis', 'RateofChangeMode', 'LPFTau', 'RiseFallLimit',
    'deltaP_Factor', 'EventLog', 'RefReactivePower', 'ActivePChangeTolerance', 'monVoltageCalc', 'monBus',
    'MonBusesVbase', 'voltwattCH_curve', 'wattpf_curve', 'wattvar_curve', 'VV_RefReactivePower', 'PVSystemList',
    'Vsetpoint', 'basefreq', 'enabled', 'like']
dict_Control['Recloser'] = [
    'MonitoredObj', 'MonitoredTerm', 'SwitchedObj', 'SwitchedTerm', 'NumFast', 'PhaseFast', 'PhaseDelayed',
    'GroundFast', 'GroundDelayed', 'PhaseTrip', 'GroundTrip', 'PhaseInst', 'GroundInst', 'Reset', 'Shots',
    'RecloseIntervals', 'Delay', 'Action', 'TDPhFast', 'TDGrFast', 'TDPhDelayed', 'TDGrDelayed', 'Normal', 'State',
    'basefreq', 'enabled', 'like']
dict_Control['RegControl'] = [
    'transformer', 'winding', 'vreg', 'band', 'ptratio', 'CTprim', 'R', 'X', 'bus', 'delay', 'reversible', 'revvreg',
    'revband', 'revR', 'revX', 'tapdelay', 'debugtrace', 'maxtapchange', 'inversetime', 'tapwinding', 'vlimit',
    'PTphase', 'revThreshold', 'revDelay', 'revNeutral', 'EventLog', 'RemotePTRatio', 'TapNum', 'Reset', 'LDC_Z',
    'rev_Z', 'Cogen', 'basefreq', 'enabled', 'like']
dict_Control['Relay'] = [
    'MonitoredObj', 'MonitoredTerm', 'SwitchedObj', 'SwitchedTerm', 'type', 'Phasecurve', 'Groundcurve', 'PhaseTrip',
    'GroundTrip', 'TDPhase', 'TDGround', 'PhaseInst', 'GroundInst', 'Reset', 'Shots', 'RecloseIntervals', 'Delay',
    'Overvoltcurve', 'Undervoltcurve', 'kvbase', '47%Pickup', '46BaseAmps', '46%Pickup', '46isqt', 'Variable',
    'overtrip', 'undertrip', 'Breakertime', 'action', 'Z1mag', 'Z1ang', 'Z0mag', 'Z0ang', 'Mphase', 'Mground',
    'EventLog', 'DebugTrace', 'DistReverse', 'Normal', 'State', 'basefreq', 'enabled', 'like']
dict_Control['StorageController'] = [
    'Element', 'Terminal', 'MonPhase', 'kWTarget', 'kWTargetLow', '%kWBand', 'kWBand', '%kWBandLow', 'kWBandLow',
    'ElementList', 'Weights', 'ModeDischarge', 'ModeCharge', 'TimeDischargeTrigger', 'TimeChargeTrigger', '%RatekW',
    '%RateCharge', '%Reserve', 'kWhTotal', 'kWTotal', 'kWhActual', 'kWActual', 'kWneed', 'Yearly', 'Daily', 'Duty',
    'EventLog', 'InhibitTime', 'Tup', 'TFlat', 'Tdn', 'kWThreshold', 'DispFactor', 'ResetLevel', 'Seasons',
    'SeasonTargets', 'SeasonTargetsLow', 'basefreq', 'enabled', 'like']
dict_Control['SwtControl'] = [
    'SwitchedObj', 'SwitchedTerm', 'Action', 'Lock', 'Delay', 'Normal', 'State', 'Reset', 'basefreq', 'enabled', 'like']
dict_Control['UPFCControl'] = ['UPFCList', 'basefreq', 'enabled', 'like']

list_Meters_DSS = ['EnergyMeter', 'FMonitor', 'Monitor', 'Sensor']
dict_Meters = dict()

dict_Meters['EnergyMeter'] = [
    'element', 'terminal', 'action', 'option', 'kVAnormal', 'kVAemerg', 'peakcurrent', 'Zonelist', 'LocalOnly', 'Mask',
    'Losses', 'LineLosses', 'XfmrLosses', 'SeqLosses', '3phaseLosses', 'VbaseLosses', 'PhaseVoltageReport', 'Int_Rate',
    'Int_Duration', 'SAIFI', 'SAIFIkW', 'SAIDI', 'CAIDI', 'CustInterrupts', 'basefreq', 'enabled', 'like']
dict_Meters['FMonitor'] = [
    'element', 'terminal', 'mode', 'action', 'residual', 'VIPolar', 'PPolar', 'P_trans_ref', 'V_Sensor', 'P_Sensor',
    'Node_num', 'Cluster_num', 'Total_Clusters', 'Nodes', 'CommVector', 'ElemTableLine', 'P_Mode', 'CommDelayVector',
    'T_intvl_smpl', 'MaxLocalMem', 'Volt_limits_pu', 'b_Curt_Ctrl', 'up_dly', 'virtual_ld_node:', 'EGen',
    'attack_defense', 'Comm_hide', 'Comm_node_hide', 'basefreq', 'enabled', 'like']
dict_Meters['Monitor'] = [
    'element', 'terminal', 'mode', 'action', 'residual', 'VIPolar', 'PPolar', 'basefreq', 'enabled', 'like']
dict_Meters['Sensor'] = [
    'element', 'terminal', 'kvbase', 'clear', 'kVs', 'currents', 'kWs', 'kvars', 'conn', 'Deltadirection', '%Error',
    'Weight', 'action', 'basefreq', 'enabled', 'like']


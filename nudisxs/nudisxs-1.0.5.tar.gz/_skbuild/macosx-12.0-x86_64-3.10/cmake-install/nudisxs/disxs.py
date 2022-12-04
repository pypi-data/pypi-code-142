from nudisxs import _nudisxs as xs
import numpy as np
import vegas
import logging
#import cubepy
log = logging.getLogger('disxs')
logformat='[%(name)20s ] %(levelname)8s: %(message)s'
logging.basicConfig(format=logformat)
log.setLevel(logging.getLevelName("INFO"))
#logging.root.setLevel(logging.getLevelName("INFO")) # set global logging level

#def calculate_total(enu,normfactor=1,mode='cc'):
#    if mode == 'cc':
#        xs_function = xs.d2sdiscc_dxdy
#    elif mode == 'nc':
#        xs_function = xs.d2sdisnc_dxdy
#    else:
#        log.error(f'this mode={mode} is not supported')
#    low  = np.array([[0.0],[0.0]])
#    high = np.array([[1.0],[1.0]])
#    def integrand(v,enu,dummy):
#        return xs_function(enu,v[0],v[1])*np.ones_like(v)

#    value,error = cubepy.integrate(integrand,low, high,args=(enu,1),itermax=1000, reltol = 1e-8)
#    return value[0]*normfactor, error[0]*normfactor

class disxs(vegas.BatchIntegrand):
    def __init__(self):
        # init common block with default values. Can be changed explicitly
        #self.old_pdf_settings()
        log.info('initializing')
        self.init_constants()
        self.init_bend_factor()
        self.init_q2_min()
        self.init_abc()
        self.init_neutrino()
        self.init_pdf()
        self.init_target()
        self.init_structure_functions()
        self.init_r_function()
        self.init_final_hadron_mass()
        self.init_fl_function()
        self.init_qc()
        self.init_vegas_integrator()

    def __call__(self, x):
        f = np.zeros(x.shape[0])
        self.xsdis_as_array(self.enu,x[:,0],x[:,1],f,x.shape[0])
        return f

    def init_enu(self, enu):
        self.enu = enu

    def init_current(self,mode='cc'):
        if mode == 'cc':
            self.xsdis_as_array = xs.d2sdiscc_dxdy_array
        elif mode == 'nc':
            self.xsdis_as_array = xs.d2sdisnc_dxdy_array
        else:
            log.error(f'unknown current={mode}. Call init_current')

    def init_vegas_integrator(self):
        self.integrator = vegas.Integrator([[0.0,1.0], [0.0,1.0]], nhcube_batch=2000, sync_ran=False)

    def calculate_total(self,enu):
        self.init_enu(enu)
        result = self.integrator(self, nitn=10)
        return result.mean*self.normfactor

    def init_constants(self):
        GeV = 1.0
        MeV = 1e-3*GeV
        self.m_e   = 0.51099892*MeV
        self.m_mu  = 105.658369*MeV
        self.m_tau = 1.77699*GeV
        self.m_n   = 0.93956536*GeV
        self.m_p   = 0.93827203*GeV
        self.normfactor=1.678*10**(-38)

    def init_pdf(self,name='CT10nlo.LHgrid'):
        xs.initpdf(name)
        log.info(f'init_pdf with {name}')

    def init_neutrino(self,pdg=14):
        xs.n_nt.n_nt = np.sign(pdg)
        if np.abs(pdg) == 12:
            xs.m_lep.m_lep = self.m_e
        elif np.abs(pdg) == 14:
            xs.m_lep.m_lep = self.m_mu
        elif np.abs(pdg) == 16:
            xs.m_lep.m_lep = self.m_tau
        else:
            log.error('unknown pdg',pdg)
        xs.m_lep.mm_lep = xs.m_lep.m_lep**2
        log.info(f'init_neutrino with pdg={pdg}')

    def init_target(self,target='proton'):
        if target == 'proton':
            xs.n_tt.n_tt = 1
            xs.m_ini.m_ini = self.m_p
            xs.m_ini.mm_ini = self.m_p**2
        elif target == 'neutron':
            xs.n_tt.n_tt = 2
            xs.m_ini.m_ini = self.m_n
            xs.m_ini.mm_ini = self.m_n**2
        else:
            log.error(f'init_target. Unknown target={target}')
        log.info(f'init_target {target}')

    def init_structure_functions(self,model=1):
         xs.n_ag_dis.n_ag_dis = model
         log.info(f'init_structure_functions model={model}')

    def init_r_function(self,model=2,modification=1):
        xs.n_rt_dis.n_rt_dis = model
        xs.n_rc_dis.n_rc_dis = modification
        log.info(f'init_r_function model={model}, modification={modification}')

    def init_final_hadron_mass(self,m=1.2):
        xs.m_fin.m_fin = m
        xs.m_fin.mm_fin = xs.m_fin.m_fin**2
        log.info(f'init_final_hadron_mass={m} GeV')

    def init_fl_function(self,model=2):
        xs.n_fl_dis.n_fl_dis = model
        log.info(f'init_fl_function model={model}')

    def init_qc(self,model=0):
        xs.n_qc_dis.n_qc_dis = model
        log.info(f'init_qc model={model}')

    def init_bend_factor(self, f=1.0):
        xs.n_bf_dis.n_bf_dis = f
        log.info(f'init_bend_factor={f:6.3E}')

    def init_q2_min(self,q2_min=1.):
        xs.q2_dis.q2_dis = q2_min
        log.info(f'init_q2_min={q2_min:6.3E}')

    def init_abc(self,a=0.0,b=0.0,c=0.0):
        xs.a0_dis.a0_dis =  a
        xs.b0_dis.b0_dis =  b
        xs.c0_dis.c0_dis =  c
        log.info(f'init_abc parameters=({a:6.3E},{b:6.3E},{c:6.3E})')

    def xs_cc(self,Enu,x,y):
        return xs.d2sdiscc_dxdy(Enu,x,y)*self.normfactor

    def xs_nc(self,Enu,x,y):
        return xs.d2sdisnc_dxdy(Enu,x,y)*self.normfactor


    def xs_cc_as_array(self,enu,x,y):
        results = np.zeros(shape=(enu.shape[0],y.shape[0],x.shape[0]),dtype=float)
        for ie, ee in enumerate(enu):
            for iy, yy in enumerate(y):
                for ix, xx in enumerate(x):
                    results[ie,iy,ix] = xs.d2sdiscc_dxdy(ee,xx,yy)*self.normfactor
        return results

#    def init_integration(self):
#        self.low  = np.array([[0.0],[0.0]])
#        self.high = np.array([[1.0],[1.0]])
#        self.one  = np.ones_like(self.low)

#    def total_cross_section(self,enu,mode='cc'):
#        return calculate_total(enu,self.normfactor,mode)

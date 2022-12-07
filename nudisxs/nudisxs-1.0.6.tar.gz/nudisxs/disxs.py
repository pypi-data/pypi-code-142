from nudisxs import _nudisxs as xs
import numpy as np
import vegas
import math
import logging
#import cubepy
log = logging.getLogger('disxs')
logformat='[%(name)20s ] %(levelname)8s: %(message)s'
logging.basicConfig(format=logformat)
log.setLevel(logging.getLevelName("INFO"))

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
        self.init_dis_kinematics()

    def __call__(self, x):
        f = np.zeros(x.shape[0])
        self.xsdis_as_array(self.enu,x[:,0],x[:,1],f,x.shape[0])
        return f

    def init_enu(self, enu):
        self.enu = enu

    def init_current(self,mode='cc'):
        if mode == 'cc':
            self.xsdis_as_array = xs.d2sdiscc_dxdy_array
            self.lepton_pdg = np.sign(self.neutrino_pdg)*(abs(self.neutrino_pdg)-1)
            if self.target == 'proton':
                if self.neutrino_pdg>0:
                    #self.hadron_pdg = 2224 # Delta++ G4 does not recognize this particle
                    self.hadron_pdg = 211 # pi+
                else:
                    self.hadron_pdg = 111  # pi0
            elif self.target == 'neutron':
                if self.neutrino_pdg>0:
                    self.hadron_pdg = 211 # pi+
                else:
                    self.hadron_pdg = -211  # pi-
            else:
                log.error(f'unknown target={self.target}')
        elif mode == 'nc':
            self.xsdis_as_array = xs.d2sdisnc_dxdy_array
            self.lepton_pdg = self.neutrino_pdg
            if self.target == 'proton':
                    self.hadron_pdg = 211 # pi+
            elif self.target == 'neutron':
                    self.hadron_pdg = 111  # pi0
            else:
                log.error(f'unknown target={self.target}')

        else:
            log.error(f'unknown current={mode}. Call init_current')

    def init_vegas_integrator(self):
        self.integrator = vegas.Integrator([[0.0,1.0], [0.0,1.0]], nhcube_batch=2000, sync_ran=False)
        log.info('init_vegas_integrator')

    def init_dis_kinematics(self):
        self.data_type = [('pdgid',int),('Px_GeV',float),('Py_GeV',float),('Pz_GeV',float),('E_GeV',float)]
        self.particles = np.zeros(shape=(2),dtype=self.data_type)
        log.info('init_dis_kinematics')

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
        log.info('init_constants')

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
        self.neutrino_pdg = pdg
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
        self.target = target
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

    def xs_nc_as_array(self,enu,x,y):
        results = np.zeros(shape=(enu.shape[0],y.shape[0],x.shape[0]),dtype=float)
        for ie, ee in enumerate(enu):
            for iy, yy in enumerate(y):
                for ix, xx in enumerate(x):
                    results[ie,iy,ix] = xs.d2sdisnc_dxdy(ee,xx,yy)*self.normfactor
        return results

    def dis_kinematics(self,E,x,y):
        # p = target nucleon 4-momentum = (m,0). Assume at rest
        # k = neutrino 4-momentum       = (E,k)
        # ph = hadrons 4-momentum       = (Eh,ph)
        # pl = final lepton 4-momentum  = (El,pl)
        # 4-momentum conservation: p+k = pl+ph
        mT = xs.m_ini.m_ini       # target nucleon mass
        mmL = xs.m_lep.mm_lep     # final lepton mass^2
        El = E*(1.0-y)            # final lepton energy
        Eh = y*E+mT               # hadrons energy
        pl = math.sqrt(El*El-mmL) # final lepton 3-momentum abs value
        vl = pl/El                # final lepton velocity
        cos_theta_lep = (1.0-mT*x/El-0.5*mmL/E/El)/vl  # final lepton scattering cosine
        sin_theta_lep = math.sqrt(1.0-cos_theta_lep**2)# final lepton scattering   sine
        phi_lep = 2*np.pi*np.random.uniform()
        # prepare two output particles: lepton
        self.particles[0]['pdgid'] = self.lepton_pdg
        self.particles[1]['pdgid'] = self.hadron_pdg
        self.particles[0]['Px_GeV'] = pl*sin_theta_lep*math.cos(phi_lep)
        self.particles[0]['Py_GeV'] = pl*sin_theta_lep*math.sin(phi_lep)
        self.particles[0]['Pz_GeV'] = pl*cos_theta_lep
        self.particles[0]['E_GeV'] = El
        # and hadron
        self.particles[1]['Px_GeV'] = -self.particles[0]['Px_GeV']
        self.particles[1]['Py_GeV'] = -self.particles[0]['Py_GeV']
        self.particles[1]['Pz_GeV'] = E-self.particles[0]['Pz_GeV']
        self.particles[1]['E_GeV'] = Eh


#    def init_integration(self):
#        self.low  = np.array([[0.0],[0.0]])
#        self.high = np.array([[1.0],[1.0]])
#        self.one  = np.ones_like(self.low)

#    def total_cross_section(self,enu,mode='cc'):
#        return calculate_total(enu,self.normfactor,mode)

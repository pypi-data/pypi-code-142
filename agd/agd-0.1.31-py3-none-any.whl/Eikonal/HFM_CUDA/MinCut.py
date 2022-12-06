# Copyright 2022 Jean-Marie Mirebeau, ENS Paris-Saclay, CNRS, University Paris-Saclay
# Distributed WITHOUT ANY WARRANTY. Licensed under the Apache License, Version 2.0, see http://www.apache.org/licenses/LICENSE-2.0

import os
import numpy as np
from types import SimpleNamespace
import time
import cupy as cp
from cupyx.scipy import fft 
from cupyx.scipy.spatial import distance

from . import cupy_module_helper
from .cupy_module_helper import SetModuleConstant
from . import Eigh

bc_id = SimpleNamespace(void=2,source=-1,sink=1,keypoint=0)

def meshgrids(shape,corners,sparse=False):
	"""
	Generates the grid, staggered grid, and boundary conditions, as suitable for the mincut
	problem, for a rectangular domain. Grids use 'ij' indexing.
	Input : 
	 - shape (tuple) : the domain dimensions (n1,...,nd)
	 - corners (array of shape (2,d)) : the extreme points of the domain
	 - sparse (bool) : wether to generate a dense or a sparse grid 
	Output : Xm,Xϕ,dx,bc
	 - Xm : grid for the metric (one point at the center of each pixel)
	 - Xϕ : grid for the boundary conditions and level set function (one point at the bottom of each pixel)
	 - dx : the discretization scale
	 - bc : empty boundary conditions, except for a sink on the domain boundary
	"""
	float_t = np.float32
	bot,top = cp.asarray(corners,dtype=float_t)
	dx = (top-bot)/cp.asarray(shape,dtype=float_t)
	Xϕ = tuple(boti+dxi*cp.arange(si,dtype=float_t) for (boti,dxi,si) in zip(bot,dx,shape))
	Xm = tuple(dxi/2.+axi for (dxi,axi) in zip(dx,Xϕ))
	bc = cp.full(shape,bc_id.void,np.int8)
	for i in range(bc.ndim): bc.__setitem__((slice(None),)*i+(slice(1),), bc_id.sink)

	def make_grid(X):
		if sparse: return tuple(axi.reshape((1,)*i+(-1,)+(1,)*(bc.ndim-i-1)) for i,axi in enumerate(X))
		else: return cp.asarray(cp.meshgrid(*X,indexing='ij'),dtype=float_t)

	return make_grid(Xm),make_grid(Xϕ),dx,bc

def metric(m=None,w=None,a=None,overwrite_m=False,
	ret_func_metric=False,**kwargs):
	"""
	The asymmetric quadratic metric defined as 
		F(x) = sqrt(a**2*x.m.x + sign(a)*(x.w_asym)_+^2)
	is formatted in a way suitable for the mincut proximal solver. 
	The metric is positive definite under the compatibility conditions 
		m > 0   and   abs(a)+sign(a) w.m^-1.w > 0
	Input : 
	 - m (optional, default Id): array of shape (n1,...,nk,d,d), symmetric w.r.t the last two axes
	 - w (optional, default=0) : array of shape (n1,...,nk,d). 
	 - a (optional, default=1) : array of shape (n1,...,nk).
	 - overwrite_m (optional) : if true, the contents of m are destroyed
	 - ret_func_metric : return a callable class representing the metric 
	 - quaternion, kwargs : passed to Eigh.eigh
	Output : 		
	 - λ (array, positive, dtype=float32): eigenvalues of m, shape (n1,...,nd, d) or 
		  (n1,...,nd, d+1) for asymmetric quadratic metric where the additional 
		  eigenvalues replaces the first one.
	 - v (array, dype=float32): eigenvectors of m, shape (n1,...,nd,d,d). 
		  Special convention (n1,n2,2) and (n1,n2,n3,4) using the first vector or unit quaternions. 
		(s,w_asym) : converted to above format
	"""
	# --- Produce a metric function ---
	if ret_func_metric:
		from ... import Metrics
		if m is None:
			if w is None: return Metrics.Isotropic(np.abs(a))
			vdim = w.shape[-1]
			m = np.broadcast_to(cp.eye(vdim),(*w.shape,vdim))
		if not overwrite_m: 
			m = m.copy()
			if w is not None: w = w.copy()
		if a is not None: 
			m *= (a**2)[...,None,None]
			if w is not None:
				pos = a<0
				w[pos] *= -1
				#m[pos] -= np.outer(w[pos],w[pos]) # Some issues with empty shapes
				m -= pos*np.outer(w,w)
		m = np.moveaxis(m,(-2,-1),(0,1))
		if w is None: return Metrics.Riemann(m)
		w = np.moveaxis(w,-1,0)
		return Metrics.AsymQuad(m,w)

	# --- Produce metric data for the mincut problem ---
	if m is None: 
		assert a is not None
		if w is None: return "iso",(np.abs(a),)
		return "iso_asym",(a,w)

	if not overwrite_m: m = m.copy()
	if a is not None: m *= (a**2)[...,None,None]
	eigm = Eigh.eigh(m,quaternion=True,**kwargs) # eigm = np.linalg.eigh(m) 
	if w is None: return "riemann",eigm
	if a is None: m += np.outer(w,w)
	else: m += np.outer(w,w)*np.sign(a)[...,None,None]
	return "riemann_asym",(*eigm,*Eigh.eigh(m,quaternion=True,**kwargs),w) # np.linalg.eigh(m)
	
def mincut(
	bc,metric,dx,w_rander=None,ret_prox_metric=False,
	τ=1.,maxiter=1000,rtol=0.05,xpu=None):
	"""
	Numerically solves the mincut problem, on the GPU, using the ADMM.
	Geometric input : 
	- bc (array, dtype=int8) : source (=-1), keypoint (=0), sink (=1), and void (=2) 
	  regions in the domain. See bc_id in the same module. 
	  Shape (n1,...,nd) where d=1,2,3.
	- metric: the metric on the domain, output of metric function.
		A Randers asymmetric perturbation can be added as well, see input w_rander.
	- dx : the grid scales, along each axis
	- w_rander (optional, array, dtype=float32) : drift field for Randers geometry
	- ret_prox : return the proximal operator of the metric (intended for debug)

	ADMM input : 
	- τ (optional) : proximal step size
	- maxiter (optional) : number of proximal iterations
	- xpu (optional, overwritten if present, array, dtype=float32) : 
		initial guess x+u for the ADMM method
	
	Output : 
	- dict containing
	 - levelsetfunc : the level set function of the mincut surface
	 - xpu,u,z : the last elements produced by the ADMM solver
	 - norm2hist : distances between iterates of the ADMM solver (regularly sampled)
	"""
	# ------- Check inputs -------
	int_t = np.int32
	float_t = np.float32

	shape = bc.shape
	size = bc.size
	vdim = bc.ndim

	metric_type,metric_data = metric
	metric_shapes = tuple(e.shape for e in metric_data)
	s0,s1,s2 = shape,(*shape,vdim),(*shape,{1:1,2:2,3:4}[vdim])
	assert metric_shapes == {'iso':(s0,),'iso_asym':(s0,s1),'riemann':(s1,s2),
		'riemann_asym':(s1,s2,s1,s2,s1)}[metric_type]

	if isinstance(dx,float): dx = (dx,)*vdim
	idx = cp.array([1/dxi for dxi in dx], dtype=float_t)
	assert idx.shape == (vdim,)

	if w_rander is None: w_rander = cp.zeros(1,dtype=float_t)
	else: assert w_rander.shape == (*shape,vdim)
	
	τ = float_t(τ)
	maxiter = int(maxiter)
	rtol = float_t(rtol)

	if xpu is None: 
		ϕ = cp.zeros(shape,dtype=float_t)
		η = cp.zeros((*shape,vdim),dtype=float_t)
	else: ϕ,η = xpu

	assert ϕ.shape == shape
	assert η.shape == (*shape,vdim)

	# TODO : perf warning if not continuguous and of correct type ? 
	bc = cp.ascontiguousarray(bc,dtype=np.int8)
	w_rander,ϕ,η = [cp.ascontiguousarray(e,dtype=float_t) for e in (w_rander,ϕ,η)]
	metric_data = tuple(cp.ascontiguousarray(e,dtype=float_t) for e in metric_data)

	# -------- Prepare the FFT multipliers --------

	axes = [cp.linspace(0,2*np.pi,s,endpoint=False,dtype=float_t) for s in shape]
	axes[-1] = axes[-1][...,:shape[-1]//2+1] # rfft halves the shape of last axis
	shape_fft=tuple(len(ax) for ax in axes)
	fft_der  = tuple((np.exp(-1j*axi)-1.)/dxi for axi,dxi in zip(axes,dx))
	fft_mean = tuple((np.exp(-1j*axi)+1.)/2.  for axi in axes)
	fft_data = tuple(val for pair in zip(fft_der,fft_mean) for val in pair)
	for e in fft_data: assert e.dtype==np.complex64 and e.flags['C_CONTIGUOUS']
	#fft_der2 = tuple(e.real**2+e.imag**2 for e in fft_der)
	#fft_mean2= tuple(e.real**2+e.imag**2 for e in fft_mean)
#	assert fft_der[0].dtype  == fft_mean[0].dtype  == np.complex64
	# assert fft_der2[0].dtype == fft_mean2[0].dtype == float_t 
#	for e in (fft_der,fft_mean): assert e[0].flags['C_CONTIGUOUS'] #,fft_der2,fft_mean2

	# --------- Generate the cupy module -----------
	def ceil(a): return int(np.ceil(a))
	shape_i = {1:(64,),2:(8,8),3:(4,4,4)}[vdim]
	shape_e = tuple(s+1 for s in shape_i)
	shape_o = tuple(ceil(s_t/s_i) for (s_t,s_i) in zip(shape,shape_i))
	traits = {
		'ndim_macro':vdim,
		'Int':int_t,
		'Scalar':float_t,
		'rander_macro':w_rander.ndim>1,
		'shape_i':shape_i,
		'shape_e':shape_e,
		'newton_maxiter':7,
		'metric_type_macro':{'iso':1,'iso_asym':2,'riemann':3,'riemann_asym':4}[metric_type]
	}
#	print(traits)

	cuda_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"cuda")
	date_modified = cupy_module_helper.getmtime_max(cuda_path)
	source = cupy_module_helper.traits_header(traits,size_of_shape=True)

	source += [
	'#include "Kernel_MinCut.h"',
	f"// Date cuda code last modified : {date_modified}"]
	cuoptions = ("-default-device", f"-I {cuda_path}") 

	source = "\n".join(source)
	module = cupy_module_helper.GetModule(source,cuoptions)
	def setcst(*args): SetModuleConstant(module,*args)
	setcst('shape_tot',shape,int_t)
	setcst('size_tot',size,int_t)
	setcst('idx',idx,float_t)
	setcst('tau',τ,float_t)
	setcst('itau',1./τ,float_t)
	setcst('shape_fft',shape_fft,int_t)
	setcst('size_fft',np.prod(shape_fft),int_t)
	setcst('shape_o',shape_o,int_t)

	_fft_sum = module.get_function("fft_sum")
	_stag_gradient = module.get_function("stag_gradient")
	_prox_metric = module.get_function("prox_metric")
	_prox_bc = module.get_function("prox_bc")

	block_size_sum = 512
	grid_size_sum = ceil(size/block_size_sum)
	def fft_sum(*args): 
		return _fft_sum((grid_size_sum,),(block_size_sum,),args+fft_data)

	block_size_gradient = np.prod(shape_i)
	grid_size_gradient = np.prod(shape_o)
	def stag_gradient(*args): 
		return _stag_gradient((grid_size_gradient,),(block_size_gradient,),args)

	block_size_metric = 512
	grid_size_metric = ceil(size/block_size_metric)
	def prox_metric(*args):
		return _prox_metric((grid_size_metric,),(block_size_metric,),args+(*metric_data,w_rander))

	block_size_bc = 1024
	grid_size_bc = ceil(size/block_size_bc)
	def prox_bc(*args):
		return _prox_bc((grid_size_bc,),(block_size_bc,),args+(bc,))

	if ret_prox_metric: 
		def prox(η):
			η = cp.ascontiguousarray(η,dtype=float_t)
			assert η.shape==(*shape,vdim)
			a,b = η.copy(),η.copy()
			prox_metric(η,a,b)
			return a+b
		return prox

	# -------- Run the ADMM algorithm -----
	# The method is based on the successive updates
	# z' = prox_g(x+u), u' = x+u-z', x' = prox_f(z'-u')
	# where f(ϕ,η) = χ_{η=grad(ϕ)} and g(ϕ,η) = χ_{ϕ satisfies bc} + G(η).
	# We denoted characteristic functions by χ, and the metric by G
	def dist2(a,b): return np.sum((a-b)**2)
		#return distance.euclidean(a.reshape(-1),b.reshape(-1),2)**2
	ϕ_xpu = ϕ;                η_xpu = η; 
	ϕ_u   = cp.empty_like(ϕ); η_u   = np.empty_like(η)
	ϕ_zmu = cp.empty_like(ϕ); η_zmu = np.empty_like(η)
	ϕ = None; η = None
	rtol_period = 5
	norm_hist = [] # History of |xpu(n+1)-xpu(n)|, every rtol_perior iterations
	admm_time = time.time()

	for i in range(maxiter):
		# First prox operation. _xpu = x+u, _u = u', _zmu = z'-u'
		prox_bc(ϕ_xpu, ϕ_u,ϕ_zmu)
		prox_metric(η_xpu, η_u,η_zmu)
		# Valid : u,zmu. Old : xpu
#		print(f"ϕ_z={ϕ_zmu+ϕ_u}, η_z={(η_zmu+η_u).T}")
#		print(f"{ϕ_u=}, {η_u.T=}")
#		print(f"ϕ_z={ϕ_zmu+ϕ_u},  {ϕ_u=}")
#		print(f"η_z={(η_zmu+η_u).T},  {η_u.T=}")


		# Second prox operation, associated with constraint η = grad(ϕ)
		ϕ_fft = fft.rfftn(ϕ_zmu,overwrite_x=True)
		ϕ_zmu = None
		η_fft = fft.rfftn(η_zmu,overwrite_x=True,axes=tuple(range(vdim)))
		η_x = η_zmu; η_zmu = None
#		print(f"{ϕ_fft=}, {η_fft.T=}")
		fft_sum(ϕ_fft,η_fft)
#		print(f"(gpu) ψ={ϕ_fft}")
		ϕ_x = fft.irfftn(ϕ_fft,shape,overwrite_x=True)
#		ϕ_x = cp.ascontiguousarray(cp.array(np.meshgrid(np.arange(shape[0]),np.arange(shape[1]),indexing='ij')[1]),dtype=float_t)
		stag_gradient(ϕ_x,η_x)

#		print(f"{ϕ_x=}")
#		print("η_x=",np.moveaxis(η_x,-1,0))
		ϕ_xpu,ϕ_xpu_old,ϕ_x,ϕ_zmu = ϕ_x,ϕ_xpu,None,ϕ_xpu; ϕ_xpu+=ϕ_u
		η_xpu,η_xpu_old,η_x,η_zmu = η_x,η_xpu,None,η_xpu; η_xpu+=η_u
		# valid : xpu,xpu_old. Invalid : x,zmu

		if i%rtol_period==0: 
			norm_hist.append(np.sqrt(dist2(ϕ_xpu,ϕ_xpu_old)+dist2(η_xpu,η_xpu_old)))
			if norm_hist[-1]<=rtol*norm_hist[0]: break
	else: 
		if rtol>0: print(f"Exhausted iteration budget ({maxiter=}) without satisfying convergence "
		"criterion. Provided rtol parameter exceeds relative error "
		f"|xpu(n+1)-xpu(n)| / |xpu(1)-xpu(0)| = {norm_hist[-1]/norm_hist[0]}.")
	admm_time = time.time()-admm_time;
	print(f"Solver took {admm_time} s, for {i+1} iterations")

	# ---------- Optionally print memory usage of main variables ----------
	# import sys
	# local_vars = list(locals().items())
	# for var, obj in local_vars:
	# 	if isinstance(obj,cp.ndarray): print(var,obj.nbytes/1024**2)

	# mempool = cp.get_default_memory_pool()
	# pinned_mempool = cp.get_default_pinned_memory_pool()

	# print(f"{mempool.used_bytes()/1024**2}")              # 0
	# print(f"{mempool.total_bytes()/1024**2}")             # 0
	# print(pinned_mempool.n_free_blocks())    # 0
	# print(mempool.get_limit())


	# ---- One more half ADMM iteration to extract the desired data ----
	prox_bc(ϕ_xpu, ϕ_u,ϕ_zmu)
	prox_metric(η_xpu, η_u,η_zmu)
	ϕ_zmu+=ϕ_u; η_zmu+=η_u
	out = {
	'norm_hist':norm_hist,
	'iter':i,
	'xpu':(ϕ_xpu,η_xpu),
	'u':(ϕ_u,η_u),  # Note : not same iteration as xpu... 
	'z':(ϕ_zmu,η_zmu),
	'levelsetfunc':ϕ_zmu
	}
	return out


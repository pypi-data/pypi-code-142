'''Grids for direct evaluation fits
'''

class Grid(object):
    '''\
    Mesh object
    '''
    def __init__(
                 self,
                 Y,
                 lnL,
                 limits,
                 norm_limit=100.,
                ):
        '''Initialize a mesh object

        Parameters
        ----------
        Y: array like, shape = (npts,ndim)
            Input Samples to fit
        L: array like, shape = (npts,)
            Input sample likelihood values
        std: array like, shape = (ndim,)
            Input sample variance, useful for some things
        limits: array like, shape = (2,ndim)
            Input limits for space of mesh
        norm_limit: float (optional)
            Input maximum normalization constant, relative to guess
        '''
        # Imports
        from gwalk.utils.multivariate_normal import params_of_norm_mu_cov
        import numpy as np
        # Exponentiate likelihood
        L = np.exp(lnL)
        # Downselect data
        keep = L > 0
        Y = Y[keep]
        L = L[keep]
        lnL = lnL[keep]
        # Normalize
        Lsum = np.sum(L)
        lnLsum = np.log(Lsum)
        # Save data
        self.Y = Y
        self.L = L#/Lsum
        self.L_norm = L/Lsum
        self.lnL = lnL# - lnLsum
        self.lnL_norm = lnL - lnLsum

        # Hold onto these
        self.npts = Y.shape[0]
        self.ndim = Y.shape[1]
        self.limits = limits
        # Core calculations
        self.mean = np.average(Y,weights=L,axis=0)
        self.cov = np.cov(Y.T,aweights=L)
        self.std = np.sqrt(np.diag(self.cov))
        # Derived calculations
        self._mu_scaled = self.mean/self.std
        self._cov_scaled = self.cov/np.outer(self.std,self.std)
        X_test = params_of_norm_mu_cov(1., self._mu_scaled, self._cov_scaled)
        self.norm_est = self.estimate_normalization_constant(X_test)
        self.norm_limit = norm_limit
        self.X_simple = params_of_norm_mu_cov(self.norm_est, self._mu_scaled, self._cov_scaled)

    def best_samples(self, n):
        ''' Find the best samples from our set

        Parameters
        ----------
        n: int
            Number of samples to find
        '''
        import numpy as np
        sort_indx = np.argsort(self.lnL)[::-1]
        best_indx = sort_indx[-n:]
        best_samp = self.Y[best_indx]
        best_L    = self.L[best_indx]
        best_lnL  = self.lnL[best_indx]
        return best_samp, best_L, best_lnL
        

    def estimate_normalization_constant(self, X_test, n=3):
        ''' Estimate the normalization constant for the fit

        Parameters
        ----------
        n: int
            Number of samples to use
        '''
        import numpy as np
        from gwalk.utils.multivariate_normal import params_of_norm_mu_cov
        from gwalk.utils.multivariate_normal import multivariate_normal_pdf
        # Identify the highest likelihood point
        best_samp, best_L, best_lnL = self.best_samples(n)
        # Find the value of the multivariate normal distribution for the best points
        best_lnL_test = multivariate_normal_pdf(X_test, best_samp, scale=self.std, log_scale=True)
        norm_simple = np.mean(best_lnL - best_lnL_test)
        return norm_simple

    def polyfit_mu_sig_1d(self, x, y, sig_default, limits):
        '''\
        Return polynomial coefficients or best guess

        Parameters
        ----------
        x: array like, shape = (npts,)
            Input space values
        y: array like, shape = (npts,)
            Input function values
        sig_default: float
            Input default value of sigma
        limits: array like, shape = (2,)
            Input limits for x space
        '''
        # Imports 
        import numpy as np
        # Call polyfit
        a, b, c = np.polyfit(x,y,2)
        # check if a is viable
        if a < 0:
            # Use polynomial coefficients
            mu = -(0.5*b/a)
            sig = -0.5/a
        else:
            # Use maximum of data
            x = x[1:-1]
            y = y[1:-1]
            mu = x[np.argmax(y)]
            sig = sig_default
        # check limits
        if (mu < limits[0]) or (mu > limits[1]):
            # Use maximum of data
            x = x[1:-1]
            y = y[1:-1]
            mu = x[np.argmax(y)]

        return mu, sig

    ######## MultivariateNormal tools ########

    #### Call Constructor ####
    def construct_nal(
                      self,
                      seed=0,
                      sig_max=None,
                      labels=None,
                     ):
        ''' Construct a bounded multivariate normal model

        Parameters
        ----------
        seed: int, optional
            Input seed for random state
        sig_max: float, optional
            Input maximum sigma parameters, relative to scale
        '''
        # Imports
        import numpy as np
        from gwalk.model.parameter import Parameter
        from gwalk.bounded_multivariate_normal import MultivariateNormal
        # Initialize parameter list
        params = []
        # Loop parameters
        for i in range(self.ndim):
            # Pick a parameter guess
            guess = (self.limits[i][1] + self.limits[i][0])/2

            # Pick a label
            if labels is None:
                label = None
            else:
                label = labels[i]

            # Construct parameter 
            p = Parameter("p_%d"%i,guess,self.limits[i],label)
            params.append(p)

        pnorm = Parameter("norm", self.norm_est, [0,self.norm_limit*self.norm_est], "norm")

        # Construct Bounded Multivariate Normal object
        MV = MultivariateNormal(
                                params,
                                self.std,
                                seed,
                                sig_max,
                                norm=pnorm,
                               )
        self.X_lims = MV.read_limits()
        self.scale=MV.scale
        return MV

    def nal_save_kl(
                    self,
                    MV,
                    fname_nal,
                    label,
                    attrs=None,
                    mode='mean',
                    better='False',
                   ):
        '''Save MV object with kl divergence
        
        Parameters
        ----------
        MV: MultivaraiteNormal object
            Input bounded multivariate normal object
        fname_nal: str
            Input file location for nal fits
        label: str
            Input path to fit group
        attrs: dict, optional
            Input additional attributes to save with nal fit
        better: bool, optional
            Input save fit only if better?
        '''
        # Imports
        from gwalk.bounded_multivariate_normal import MultivariateNormal
        # Initialize attrs if none
        if attrs is None:
            attrs = {}
        # Get kl divergence
        attrs["kl"] = self.nal_kl_div(MV,MV.read_guess(),mode=mode).flatten()
        # Check for better
        if better:
            # Check if the fit already exists
            if MV.exists(fname_nal, label):
                # Load the existing fit
                MVexist = MultivariateNormal.load(fname_nal, label)
                # check MVexist[kl]
                kl_exist = self.nal_kl_div(MVexist,MVexist.read_guess(),mode=mode).flatten()
                # If kl_exist is lower than kl, return
                if kl_exist < attrs["kl"]:
                    return
        # Save fit
        MV.save(fname_nal, label, attrs=attrs)

    #### Convergence ####
    def nal_kl_div(
                   self,
                   MV,
                   X=None,
                  ):
        ''' Calculate the KL Divergence for a set of parameters

        Parameters
        ----------
        MV: MultivariateNormal object
            Input bounded multivariate normal object
        X: array like, shape = (npts, nparams),optional
            Input test params for kl divergence
        '''
        # Imports 
        import numpy as np
        from relative_entropy_cython import relative_entropy_alt
        # Use built in value for X
        if X is None:
            X = MV.read_guess()
        ## Prep ##
        X = MV.check_sample(X)
        ## Calculate kl divergences ##
        # Get lnL_norm
        lnL_norm = MV.likelihood(
                                 self.Y,
                                 X=X,
                                 scale=MV.scale,
                                 log_scale=True,
                                )
        # Normalization of Q is handled by relative entropy alt
        #lnL_norm /= np.sum(lnL_norm)

        # Calculate the kl divergence
        kl = relative_entropy_alt(self.L_norm, self.lnL_norm, lnL_norm)
        return kl

    def nal_least_squares(
                          self,
                          MV,
                          X=None,
                          scalar=True,
                         ):
        ''' Calculate the least squares difference for a set of parameters

        Parameters
        ----------
        MV: MultivariateNormal object
            Input bounded multivariate normal object
        X: array like, shape = (npts, nparams),optional
            Input test params for kl divergence
        scalar: bool (otpional)
            Input decide if you want a single number output instead of an array
        '''
        # Imports 
        import numpy as np
        # Use built in value for X
        if X is None:
            X = MV.read_guess()
        ## Prep ##
        X = MV.check_sample(X)
        keep = MV.satisfies_constraints(X)
        ## Calculate kl divergences ##
        # Get lnL_norm
        lnL = np.zeros((X.shape[0],self.npts))
        if np.sum(keep) > 0:
            lnL[keep] = MV.likelihood(
                                      self.Y,
                                      X=X[keep],
                                      scale=MV.scale,
                                      log_scale=True,
                                      lnL_offset=X[:,0],
                                     )
        lstsq = np.sum((self.lnL[None,:] - lnL)**2,axis=1)
        if scalar:
            lstsq = np.prod(lstsq)
        return lstsq


    def nal_kl_opt_fn(self,MV,k=-1.):
        ''' Return a function which evaluates the kl divergence given params

        Parameters
        ----------
        MV: MultivariateNormal object
            Input bounded multivariate normal object
        k: float, optional
            Input power of kl divergence
        '''
        import numpy as np
        def kl_div(X):
            kl = self.nal_kl_div(MV,X=X)
            return np.power(kl,k)
        return kl_div

    #### Guessing ####
    def nal_grid_guesses(
                         self,
                         MV,
                        ):
        ''' Fit the bounded multivariate normal model to the grid
        
        Parameters
        ----------
        MV: MultivariateNormal object
            Input some initialized Multivariate Normal object
        '''
        # Imports 
        import numpy as np
        from gwalk.utils.multivariate_normal import params_of_norm_mu_cov
        # Identify number of guesses
        n_guess = 2
        # Initialize guesses
        Xg = np.tile(MV.read_guess(),(n_guess,1))
        Xg[1] = self.X_simple
        '''
        # Generate 1D evaluation guesses
        for i in range(self.ndim):
            y_test = y_test[keep].flatten()/MV.scale[i]
            L_test = np.log(L_test[keep].flatten())
            # Find maximum
            mu, sig = self.polyfit_mu_sig_1d(y_test, L_test, X[i+self.ndim], self.limits[i])
            Xg[0,i] = mu
            Xg[0,i+self.ndim] = sig

        # Generate 1D training guesses
        for i in range(self.ndim):
            # Load values
            y_train = self.marginals["1d_%d_x_train"%i]
            L_train = self.marginals["1d_%d_y_train"%i]
            bins = int(self.marginals["1d_%d_bins"%i])

            # Rescale training set 1
            y_train_1 = y_train[:bins].flatten()/MV.scale[i]
            L_train_1 = L_train[:bins].flatten()
            keep_1 = L_train_1 > 0
            y_train_1 = y_train_1[keep_1]
            L_train_1 = np.log(L_train_1[keep_1])
            # Rescale training set 2
            y_train_2 = y_train[bins:].flatten()/MV.scale[i]
            L_train_2 = L_train[bins:].flatten()
            keep_2 = L_train_2 > 0
            y_train_2 = y_train_2[keep_2]
            L_train_2 = np.log(L_train_2[keep_2])

            # fit training set 1
            mu, sig = self.polyfit_mu_sig_1d(y_train_1, L_train_1, X[i+self.ndim], self.limits[i])
            Xg[1,i] = mu
            Xg[1,i+self.ndim] = sig

            # fit training set 2
            mu, sig = self.polyfit_mu_sig_1d(y_train_2, L_train_2, X[i+self.ndim], self.limits[i])
            Xg[2,i] = mu
            Xg[2,i+self.ndim] = sig
        '''

        return Xg


    #### Fit methods ####

    def nal_fit_to_samples(self,MV,**kwargs):
        ''' Fit the bounded multivariate normal model to some samples
        Parameters
        ----------
        MV: MultivariateNormal object
            Input some initialized Multivariate Normal object
        '''
        # Imports
        import numpy as np
        from gwalk.utils.multivariate_normal import params_of_norm_mu_cov
        # Generate simple guess
        Xs = params_of_norm_mu_cov(self.norm_est,self._mu_scaled,self._cov_scaled)
        # Fit to samples
        MV.assign_guess(Xs)
        return MV

    def nal_fit_scipy(self, MV, objective="kl", method="L-BFGS-B", **kwargs):
        ''' Fit the bounded multivariate normal model using scipy.optimize

        Parameters
        ----------
        MV: MultivariateNormal object
            Input some initialized Multivariate Normal object
        '''
        # Imports
        import numpy as np
        import scipy.optimize
        from gwalk.utils.multivariate_normal import mu_of_params
        from gwalk.utils.multivariate_normal import cov_of_params
        def kl_objective(X):
            kl = self.nal_kl_div(MV, X=X)
            return kl
        def lstsq_objective(X):
            lstsq = self.nal_least_squares(MV, X=X)
            return lstsq
            

        if objective == "kl":
            fn = kl_objective
        elif objective == "lstsq":
            fn = lstsq_objective
        else:
            raise RuntimeError("objective options: 'kl', 'lstsq'")

        MV.scipy_out = scipy.optimize.minimize(
                                               fn,
                                               self.X_simple,
                                               method=method,
                                               bounds=self.X_lims,
                                              )

        X_scipy = MV.scipy_out.x.flatten()
        if objective == "kl":
            # Still need a least squares fit for the normalization constant
            def lstsq_norm(X0):
                X_norm = np.copy(X_scipy)
                X_norm[0] = X0
                lstsq = self.nal_least_squares(MV, X=X_norm)
                return lstsq
            # Minimize this one
            norm_scipy_out = scipy.optimize.minimize(
                    lstsq_norm,X_scipy[0],method=method,bounds=[self.X_lims[0]])
            X_scipy[0] = norm_scipy_out.x.flatten()
                
        MV.assign_guess(X_scipy)
        return MV
            
            


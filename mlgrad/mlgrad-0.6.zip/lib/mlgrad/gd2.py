
class MultiGD:
    #
    def fit(self):
        for gd in self.gds:
            gd.init()
        
        lval_min = risk.evaluate()
        param_min = np.array(risk.model.param)
        
        for K in range(self.n_iter):
            
            for gd in self.gds:
                gd.fit()

            lval = risk.evaluate()
            self.lvals.append(lval)

            is_complete = False
            if fabs(lval - lval_min) / (1 + fabs(lval_min)) < self.tol:
                is_complete = True

            if lval < lval_min:
                lval_min = lval
                param_min[:] = risk.model.param
                
            if is_complete:
                break
                
        self.risk.param[:] = param_min
        self.lval_min = lval_min
            

# coding: utf-8

# The MIT License (MIT)
#
# Copyright (c) <2015-2022> <Shibzukhov Zaur, szport at gmail dot com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from sys import float_info

import numpy as np
from mlgrad.gd import FG
from mlgrad.model import ModelComposition, ModelComposition_j
from mlgrad.risk import ERisk, MRisk

class IRGD2:
    #
    def __init__(self, X, Y, model_comp, avr_func, loss_func, 
                 tol=1.0e-6, n_iter=100, tol2=1.0e-6, n_iter2=100, h_anneal=0.96, 
                 M=40, callback=None):
        """
        """
        self.model_comp = model_comp
        self.avr_func = avr_func
        self.loss_func = loss_func
        self.X = X
        self.Y = Y
        self.tol = tol
        self.n_iter = n_iter
        self.tol2 = tol2
        self.n_iter2 = n_iter2
        self.M = M
        self.K = 0
    #
    def fit(self):
        X = self.X
        Y = self.Y
        self.K = 0
        
        model_comp = self.model_comp
        loss_func = self.loss_func
        avr_func = self.avr_func
        
        risks = [ \
            ERisk(X, Y, ModelComposition_j(model_comp, j), loss_func) \
            for j, mod in enumerate(model_comp.models)]
        gds = [ \
            FG(risk, tol=self.tol2, n_iter=self.n_iter2) \
            for risk in risks]
        risk = self.risk = MRisk(X, Y, model_comp, loss_func, avr_func)
        
        self.lval_best = risk.evaluate()
        self.lvals = [self.lval_best]
        self.param_best = np.array(risk.param, copy=True)
        
        is_completed = False
        m = len(gds)
        for K in range(self.n_iter):
            
            Yp = model_comp.evaluate_all(X)
            L = loss_func.evaluate_all(Yp, Y)
            avr_func.fit(L)
            W = avr_func.gradient(L)
            for j in range(m):
                gd = gds[j]
                gd.risk.use_weights(W)
                gd.fit()
                        
            self.lval = self.risk.evaluate()
            self.lvals.append(self.lval)
                
            if self.stop_condition():
                is_completed = 1

            if self.lval < self.lval_best:
                self.param_best[:] = risk.param
                self.lval_best = self.lval

            # if K > 11 and self.lval > self.lvals[-1]:
            #     self.gd.h_rate.h *= self.h_anneal
            #     self.gd.h_rate.init()

            if is_completed:
                break            
        #
        self.K += K
        self.finalize()

    #
    def finalize(self):

        print(self.lval_best)
        self.risk.param[:] = self.param_best
    #
    def stop_condition(self):
        
        if abs(self.lval - self.lval_best) / (1 + abs(self.lval_best)) < self.tol:
            return True
        
        return False


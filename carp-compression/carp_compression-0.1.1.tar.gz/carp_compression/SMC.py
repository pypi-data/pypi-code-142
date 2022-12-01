#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 01:20:09 2022

@author: ivantao
"""

import numpy as np
from numpy import random
import math
import pywt
from datetime import datetime
#from sklearn.preprocessing import StandardScaler

def DrawChildrenNodes(rank_node, t,lambda_mat, rank_left_child, rank_right_child, keep_all = 1):
    #draw t-step children nodes of rank_node (scalar)
    #input: rank_node,t,keep_all: int; lambda_mat: dataframe; rank_left_child, rank_right_child: np.array
    #'lamda_mat','rank_left_child','rank_right_child' are global variables
    #'lamda_mat' is a dataframe
    #if nargin < 6:
    #   keep_all = 1
    #keep all levels or just the very last child level
    N = lambda_mat.shape[0]
    output = np.array([rank_node])
    direction = np.array([None])#0 means it is the origin of this child tree
    for ith_step in range(1,t+1):
        divide_prob = lambda_mat[rank_node-1,:]
        #print(divide_prob.shape[0])
        flag = np.squeeze((np.random.rand(1,int(divide_prob.size/divide_prob.shape[0]))<divide_prob.T[0]))#if 1, then direction 1; if 0, then direction 2
        which_direction = 2-flag
        #so there are only 2 dimensions can be divided at all
        #direction_in{l+1}=which_direction
        #row: rank_node; col: which_direction
        #idx_selected = (which_direction - 1)*N + rank_node
        idx_selected_row = rank_node - 1
        idx_selected_col = which_direction - 1
        
        rank_node_next_level = np.array([rank_left_child[idx_selected_row, idx_selected_col],rank_right_child[idx_selected_row, idx_selected_col]])
        rank_node = np.squeeze(rank_node_next_level.T.reshape(rank_node_next_level.size, 1))
        output = np.append(output, rank_node)
        direction = np.append(direction, which_direction)
    if keep_all == 0:
        output = rank_node
    direction = np.delete(direction,[0])
    result = {'output':output,'direction':direction.astype('int16')}
    return result

#this function is to re_assign the columns of the input
#the input_ is a np.array
#flag is a list
def re_assign(input_, flag):
    output = input_
    nflag = len(flag)
    
    if min(input_.shape) == 1:
        for i in range(nflag):
            output[i] = input_[flag[i]]
    else:
        output[:,range(nflag)] = input_[:,flag]
            
    return output

def normlike(mu, sigma, data):
    normlike = np.sum(1/2*math.log(2*math.pi*(sigma**2))+((data-mu)**2)/(2*(sigma**2)))
    return normlike



def log_expey(x, y):
    if (math.isinf(math.fabs(x)) == True) and (math.isinf(math.fabs(y)) == False):
        result = y
    elif (math.isinf(math.fabs(x)) == False) and (math.isinf(math.fabs(y)) == True):
        result = x
    elif (math.isinf(math.fabs(x)) == True) and (math.isinf(math.fabs(y)) == True):
        result = x
    elif (x - y >= 100):
        result = x
    elif (x - y <= 100):
        result = y
    else:
        if (x > y):
            result = y + math.log(1+math.exp(x-y))
        else:
            result = x + math.log(1+math.exp(y-x))
    return result
    
    
    
#wavecoef2logL calculates the logL contributed from a single wavelet coef
#wavecoef:np.array level:int; par:dataframe; sigma_hat:float
def wavecoef2logL(wavecoef, level, par, sigma_hat):
    if par[level,0] == 1:
        log1_par = float('-inf')
    else:
        log1_par = math.log(1-par[level,0])
    if par[level,0] ==0:
        logpar = float('-inf')
    else:
        logpar = math.log(par[level,0])
    nlogL1 = -log1_par+normlike(0,sigma_hat,wavecoef)
    nlogL2 = -logpar+normlike(0,math.sqrt(1+par[level,1])*sigma_hat,wavecoef)
    logL = log_expey(-nlogL1, -nlogL2)
    return logL



# dwt for sparse observations to mimic matlab 'dwt' function
# SparseUpdateOneLevel updates (mother) wavelet coefficients if the next
# level father wavelet coefficients change sparsely
# father coefficients 'father_child' are updated using (idx_child,
# value_child), i.e., the new father coef of the child level become
# father_child + value_child at idx_child
# (approx_coef, detail_coef)
# 'level' is the updating level; number of wavelet coefs = 2^level

def dwt_sparse(level, c_idx, c_diff, Lo, Hi):
    # idx_child starts with length length(g)/2, affecting at most length(g) - 1
    # c_idx takes value from 0, 1, 2, ..., (2^c_level - 1)

    # vectors could be both col or row vectors 
    x = c_diff
    #compute sizes and shape.
    lf = len(Lo)
    lx = len(x)
    lenEXT = lf/2
    
    #Figure out: 'first', 'last', 'idx' and 'c_idx'
    first = int((lenEXT + c_idx)%2)
    len_full_conv = lx +lf -1
    c_idx = (math.ceil((c_idx - lenEXT)/2))%pow(2,(level - 1))
    
    #compute coefficients of approximation
    z = np.convolve(x,Lo,'full')
    a = z[first:len_full_conv:2]
    
    #compute coefficients of detail
    z = np.convolve(x,Hi,'full')
    d = z[first:len_full_conv:2]
    
    output = {'a':a, 'd':d, 'c_idx':c_idx}
    return output



# SparseUpdateOneLevel updates (mother) wavelet coefficients if the next
# level father wavelet coefficients change sparsely
# father coefficients 'father_child' are updated using (idx_child,
# value_child), i.e., the new father coef of the child level become
# father_child + value_child at idx_child
# (approx_coef, detail_coef)
# 'level' is the updating level; number of wavelet coefs = 2^level

def SparseUpdateOneLevel(c_idx, c_diff, operator, level):
    # idx_child starts with length length(g)/2, affecting at most length(g) - 1
    # all vectors are row vectors
    
    if c_idx<0:
        print('c_idx must be nonnegative')
    # c_idx takes value from 0, 1, 2, ..., (2^c_level - 1)
    
    c_idx_last = (c_idx+len(c_diff)-1)%(pow(2, level))
    flag = [c_idx%2, c_idx_last%2]
    
    #expand c_diff into size-2 blocks
    c_bin_diff = c_diff
    
    if flag[0] == 1:
        c_bin_diff = np.append([0], c_bin_diff)
    
    if flag[1] == 0:
        c_bin_diff = np.append(c_bin_diff, [0])
    
    #affects to the parent level
    #block_idx in the children levels is affected
    block_idx = math.floor(c_idx/2)
    l = len(operator)/2 # operator must have even length
    p_idx = (block_idx-l+1)%(pow(2, level-1))
    
    b = len(c_bin_diff)/2
    p_length = b+l-1
    p_diff = np.zeros(p_length)
    
    # utilize the fact that the number of affected blocks b is at most l
    for i in range(1, b+l):# number of overlaped items
        for j in range(max(1, i-l+1),min(i,b)+1):
            #each overlapyed item uses jth block * (l + j - i)th operator block
            p_diff[i-1] = p_diff[i-1]+operator[2*(l+j-i)-2]*c_bin_diff[2*j-2]+operator[2*(l+j-i)-2]*c_bin_diff[2*j-1]
    output = {'p_idx':p_idx, 'p_diff':p_diff}
    return output



#c_diff: row vector
#all vectors are row vectors
def SparseWavelet(level, c_idx, c_diff, Lo, Hi):
    # SPARSEWAVELET obtains wavelet coefficients for sparse observations; stored sparsely
    # INPUT:
    # length of observation = 2^level;
    # a wavelet vector = (father coef, mother coef's);
    # c_idx is the index of the first observation that is changed (on the observation domain)
    c = [];idx = [];l = []
    
    x = c_diff #row vector
    cutoff_level = math.ceil(math.log2(2*len(Lo))) #such that 2*length(filter)<=2^cutoff_level
    
    for i in range(level-1,cutoff_level-2,-1):
        outcome = dwt_sparse(i+1, c_idx, x, Lo, Hi)
        x = outcome.get('a')
        d = outcome.get('d')
        c_idx = outcome.get('c_idx')
        #idx in the original wavelet vector: father coef is included
        idx_update = np.mod(range(c_idx,c_idx+len(x)),pow(2,i))+pow(2,i)
        c = np.append(d,c); idx = np.append(idx_update, idx)
        l = np.append(np.array(np.zeros(len(x))+i),l)
        
    #sort x : fully update at coarse levels
    i = cutoff_level-1
    order_x = np.zeros(pow(2, i))# row vector
    order_idx = np.mod(range(c_idx,c_idx+len(x)),pow(2,i))
    order_x[order_idx] = x
    #the global dwtmode is 'per'
    wavelet = pywt.Wavelet(filter_bank=(Lo,Hi,Lo,Hi))
    d = pywt.wavedec(order_x, wavelet, 'per', cutoff_level-1)
    d0 = np.array(d[0]); m=0
    keeper = []
    for j in d:
        m = m+1
        keeper.append(len(j))
        if m<len(d):
            d0 = np.append(d0, np.array(d[m]))
    c = np.append(d0,c); idx = np.append(range(0,pow(2,i)), idx)
    l = np.concatenate(([0],np.repeat(range(0,i), keeper[1:i+1]), l))
    output = {'idx': idx.astype('int16'), 'c': c, 'l':l.astype('int16')}
    return output



#the output and input follows: python = matlab
def ind2sub(array_shape, ind):
    ind = ind - 1
    ind[ind<0] = -1
    ind[ind>=array_shape[0]*array_shape[-1]] = -1
    cols = (ind/array_shape[0]).astype('int')+1
    rows = ind%array_shape[0]+1
    return (rows.astype('int16'), cols.astype('int16'))



def sub2ind(array_shape, rows, cols):
    cols = cols - 1; rows = rows - 1
    ind = rows + cols*array_shape[0]
    if ind.any() < 0:
        ind = -1
        print('Index Value ERROR!')
    elif ind.any() >= array_shape[0]*array_shape[-1]:
        ind = -1
        print('Index Value OVERFLOW!')
    else:
        ind = ind + 1
        return ind.astype('int16')
    


#the input log_weight is numpy.array
def normalize(log_weight):
    log_weight = log_weight.ravel()
    margin = log_weight-log_weight.max()
    weight = []
    for i in margin:
        weight_i = math.exp(i)
        weight.append(weight_i)
    weight = np.array(weight)
    weight = weight/weight.sum()
    return weight

#obs,dimension,dividible,lambda_map,y: 1D np.array
#par: 2D np.array
def SMC(obs, dimension, num_particle, ESS, lambda_map, rank_left_child, rank_right_child, dividible, par, y, length_filter):
    
    #global settings
    total_level = int(math.log2(obs.size))
    num_node = 2*dimension - 1
    N = np.prod(num_node)
    sigma_hat = par[total_level, 2]
    #dwtmode = 'per'
    #periodization: this boundary mode makeks c the same as obs

    #'n_' stores various length information
    #clear n
    n_obs = obs.size
    #wavelet filter length = 2*n_filter
    n_filter = length_filter#'db2' filter('db1' is Haar)
    nm = 'db%s'%n_filter
    wavelet = pywt.Wavelet(nm)

    Lo = pywt.Wavelet(nm).get_filters_coeffs()[0]
    Hi = pywt.Wavelet(nm).get_filters_coeffs()[1]
    n_tree = num_particle#number of trees
    n_dict_node = N#number of nodes in the dictionary
    n_tree_size = n_obs#size of each tree = num of observation less 1
    n_tree_level = total_level#max level in each tree

    #in cpp: code this efficiently
    lambda_mat = np.zeros((n_dict_node, 2))
    lambda_mat.T[dividible.T>0] = np.exp(lambda_map)
    log_ratio_lambda_mat = np.zeros((n_dict_node, 2))#log(prior/posterior)
    log_ratio_lambda_mat.T[dividible.T>0] = math.log(1/2) - lambda_map

    wave_coef = np.zeros((n_obs, n_tree))
    wave_coef[0,:] = y[0]/np.sqrt(n_obs)
    #available node for branching after accounting for near atomic & pruning
    wave_open = np.ones(wave_coef.shape) #level 0, 1, ..., n.tree_level - 1 INCLUDING 1 father coef - same index as 'wave_coef'

    # % 1 - available; 0 - taken
    # node_available = ones([n.obs - 1, n.tree]);
    # % starting idx and ending idx at each level in Matlab (starting from 0)
    # node_available_start = 2.^(0:(n.tree_level - 1));
    # node_available_end = 2.^(1:(n.tree_level)) - 1;
    # % levels 0 to (level_cutoff) are taken
    # node_available(1:node_available_end(level_cutoff + 1), :) = 0;

    wave_keeper = np.repeat(range(0,n_tree_level), np.power(2,range(0,n_tree_level)))#house keeper of wave_coef less father coef
    wave_coef_logL = np.zeros((n_obs,n_tree))

    logL_target = np.zeros((n_tree,1))
    diff_log_ratio_lambda = np.zeros((n_tree,1))#store difference of log_ratio_lambda at each move(dynamic)
    diff_logL_target = np.zeros((n_tree,1))#=new-old

    #initialize
    node_in = np.ones((1,n_tree))# the root node
    log_weight = np.zeros((n_tree,1))

    #convenient tility functions
    # convinient utility functions
    #conv_DrawChildren = @(rank, step) DrawChildrenNodes(rank, ...
        #step, lambda_mat, rank_left_child, rank_right_child);
    # conv_DrawChildren_neat = @(rank, step) DrawChildrenNodes(rank, ...
    #     step, lambda_mat, rank_left_child, rank_right_child, 0); % only keep the last level

    ## starting from level 0: draw multiple steps simultaneously
    # if level_cutoff < min(dimension(1), dimension(2)) then no need to
    # consider nearly atomic nodes but possible has prunning
    level_cutoff = length_filter
    keeper = np.repeat(range(0,level_cutoff+1),np.power(2,range(0,level_cutoff+1)))
    idx_cutoff = np.argwhere(keeper==level_cutoff).reshape(-1)
    node_in_new = np.zeros((pow(2,level_cutoff),n_tree))

    for ith_tree in range(1,n_tree+1):
        rank_node = int(node_in[0,ith_tree-1])
        draw_children = DrawChildrenNodes(rank_node,level_cutoff,lambda_mat,rank_left_child,rank_right_child)
        child_node = draw_children.get('output')
        d = draw_children.get('direction')
        #generate the likelihood ratio
        #temp_obs = sum of obs at each node / sqrt(number of pixels at each node)
        temp_obs = y[child_node[idx_cutoff]-1]/np.sqrt(np.power(2,n_tree_level-level_cutoff))
        node_in_new[:, ith_tree-1] = child_node[idx_cutoff]

        #wavelet coefficients
        c2 = pywt.wavedec(temp_obs, wavelet, 'per', level_cutoff)
        l2 = []
        for j in c2:
            l2.append(len(j))
        
        for l in range(0,level_cutoff):
            wave_coef[pow(2,l):(pow(2,l+1)),ith_tree-1] = c2[-(level_cutoff-l)]
            wave_open[pow(2,l):(pow(2,l+1)-1),ith_tree-1] = wave_open[pow(2,l):(pow(2,l+1)-1),ith_tree-1]+1
            
        for l in range(1,pow(2,level_cutoff)):
            #logL_haar(ith_tree) = logL_haar(ith_tree) + M_d_mat(child_node(l),d(l))
            diff_log_ratio_lambda[ith_tree-1] = diff_log_ratio_lambda[ith_tree-1]+log_ratio_lambda_mat[child_node[l-1]-1,d[l-1]-1]
            wave_coef_logL[l,ith_tree-1] = wavecoef2logL(wave_coef[l,ith_tree-1], wave_keeper[l-1], par, sigma_hat)
            logL_target[ith_tree-1] = logL_target[ith_tree-1]+wave_coef_logL[l,ith_tree-1]
            
        log_weight[ith_tree-1] = diff_log_ratio_lambda[ith_tree-1]+logL_target[ith_tree-1]
        
    weight = np.exp(log_weight-np.max(log_weight)); W = np.sum(weight)
    weight_norm = weight/W
    log_W = np.log(W)+np.max(log_weight)

    print('ESS = %.2f \n' %(1/np.sum(np.power(weight_norm,2))))
    if (1/np.sum(np.power(weight_norm,2))<ESS): #resample
        print('resample needed | \n')
        flag_resample = np.zeros((n_tree,1))
        for ith_tree in range(1,n_tree+1):
            flag_resample[ith_tree-1] = np.argwhere(random.multinomial(1,weight_norm)).reshape(-1)
        log_weight = np.zeros((n_tree,1))+log_W-np.log(n_tree)

        #re-assign according to flag_resample
        node_in_new = re_assign(node_in_new, flag_resample)
        wave_coef = re_assign(wave_coef, flag_resample)
        wave_coef_logL = re_assign(wave_coef_logL, flag_resample)
        diff_log_ratio_lambda = re_assign(diff_log_ratio_lambda, flag_resample)
        logL_target = re_assign(logL_target, flag_resample)

    #fprintf(sprintf('ends: took %.2fs \n', toc))

    ##next levels: node by node
    #legend:
    # j-branching level(previous branchin_level)
    # k-branching node(from 0 to 2^j - 1)

    for j in range(level_cutoff, n_tree_level):
        tic = datetime.now()
        print('%dth level starts: resample at'%j)
        child_level = j+1
        #pre_allocate level storage
        node_in = node_in_new
        node_in_new = np.zeros((pow(2,child_level), n_tree))
        dummy_obs = y[node_in.astype('int16')-1]/np.sqrt(np.power(2, n_tree_level-j)) #obs at jth level - old
        update_obs = np.zeros((pow(2,j),n_tree)) #dynamically changed obs at jth level
        #determine nearly-atomic nodes
        for k in range(0, pow(2,j)):
            for ith_tree in range(1,n_tree+1):
                rank_node = int(node_in[k,ith_tree-1])
                draw_children = DrawChildrenNodes(rank_node, 1, lambda_mat, rank_left_child, rank_right_child)
                child_node = draw_children.get('output')
                d = draw_children.get('direction')
                temp_obs = y[child_node[1:3]-1]/np.sqrt(np.power(2,n_tree_level-child_level))
                node_in_new[(2*k):(2*k+2), ith_tree-1] = child_node[1:3]
                diff_log_ratio_lambda[ith_tree-1] = log_ratio_lambda_mat[rank_node-1, d-1]
                a = dwt_sparse(j+1, 2*k, temp_obs, Lo, Hi).get('a')
                d = dwt_sparse(j+1, 2*k, temp_obs, Lo, Hi).get('d')
                c_idx = dwt_sparse(j+1, 2*k, temp_obs, Lo, Hi).get('c_idx')
                
                #changes in the branching level 'approximation coef'
                idx = np.mod(range(c_idx, c_idx+len(d)), pow(2, j))
                idx_row = (idx+1)%(pow(2,j))-1
                idx_col = (np.ceil((idx+1)/pow(2,j))-1).astype('int16')
                update_obs[idx_row, idx_col] = d+update_obs[idx_row,idx_col]
                c_diff = update_obs[idx_row,idx_col]-dummy_obs[idx_row,idx_col]
                dummy_obs[idx_row, idx_col] = update_obs[idx_row, idx_col]            
                
                #update wavelet coef at all previous levels
                output_idx = SparseWavelet(j, c_idx, c_diff, Lo, Hi).get('idx')
                output_diff = SparseWavelet(j, c_idx, c_diff, Lo, Hi).get('c')
                output_keeper = SparseWavelet(j, c_idx, c_diff, Lo, Hi).get('l')
                #combine wavelet coef changes
                output_idx = np.append(output_idx, idx+pow(2,j))
                output_diff = np.append(output_diff, a)
                output_keeper = np.append(output_keeper, np.zeros((len(idx),1))+j).astype('int16')
                #update likelihood
                ss = 0
                for ii in range(1, len(output_idx)+1):
                    wave_coef[output_idx[ii-1], ith_tree-1] = wave_coef[output_idx[ii-1], ith_tree-1]+output_diff[ii-1]
                    new_logL = wavecoef2logL(wave_coef[output_idx[ii-1], ith_tree-1], output_keeper[ii-1], par, sigma_hat)
                    ss = ss + new_logL - wave_coef_logL[output_idx[ii-1], ith_tree-1]
                    wave_coef_logL[output_idx[ii-1], ith_tree-1] = new_logL
                    
                diff_logL_target[ith_tree-1] = ss
            
            #update log_weight
            log_weight = log_weight + diff_logL_target + diff_log_ratio_lambda
            weight = np.exp(log_weight - np.max(log_weight))
            W = np.sum(weight); log_W = np.log(W)+np.max(log_weight)
            
            weight_norm = weight/W

            if (1/np.sum(np.power(weight_norm, 2)) < ESS):#resample
                print('%d | \n'%k)
                # fprintf('ESS = %.2f : resample needed | \n', 1 / sum(weight_norm .^2));
                flag_resample = np.zeros((n_tree, 1))
                for ith_tree in range(1,n_tree+1):
                    flag_resample[ith_tree-1] = np.argwhere(random.multinomial(1,np.squeeze(weight_norm.T))).reshape(-1)
                log_weight = np.zeros((n_tree, 1)) + log_W - np.log(n_tree)
                #re-assian according to flag_resample
                node_in = node_in.astype('int16')
                flag_resample = np.squeeze(flag_resample.astype('int16'))
                node_in  = re_assign(node_in, flag_resample)
                node_in_new = re_assign(node_in_new, flag_resample)
                wave_coef = re_assign(wave_coef, flag_resample)
                wave_coef_logL = re_assign(wave_coef_logL, flag_resample)
                logL_target = re_assign(logL_target, flag_resample)
        toc = datetime.now()
        seconds = (toc-tic).total_seconds()
        print('\n    ends: took %.2fs \n'%seconds)


    #reconstruct images
    est_all = np.zeros((obs.size, n_tree))

    tic = datetime.now()
    for ith_tree in range(1, n_tree+1):
        i,j = ind2sub(num_node, node_in_new[:, ith_tree-1])
        position = sub2ind(dimension, i - dimension[0]+1, j - dimension[1]+1)
        obs_vec = obs[position-1]
        #wavelet denoising: use functions 'wavedec' and 'waverec'
        c0 = pywt.wavedec(obs_vec.T, wavelet, 'per',int(math.log2(len(obs_vec))))
        m = 0; wave_level = []; c = np.array(c0[0])
        for ci in c0:
            m = m+1
            if m<len(c0):
                c = np.append(c, np.array(c0[m]))
            wave_level.append(np.array(np.squeeze(ci)).size)
        wave_level.append(np.sum(wave_level))
        
        ##calculate the likelihoods and their ratios
        #tau - should have length (total_level) NOT total_level + 1
        #last element of tau is not useful - double check
        
        tau_level = np.repeat(par[0:n_tree_level, 1], wave_level[1:n_tree_level+1])
        rho_level = np.repeat(par[0:n_tree_level, 0], wave_level[1:n_tree_level+1])
        
        w_d = np.array(c[1:])
        nlogL = np.zeros((total_level, 2))
        for l in range(0, total_level):
            nlogL1 = -np.log(1-par[l,0]) + normlike(0,sigma_hat, w_d[(pow(2,l)-1):(pow(2,l+1)-1)])
            nlogL2 = -np.log(par[l,0]) + normlike(0,np.sqrt(1+par[l,1])*sigma_hat, w_d[(pow(2,l)-1):(pow(2,l+1)-1)])
            nlogL[l,:] = [nlogL1, nlogL2]
        logL = -nlogL
        
        log_expey_result = []
        for i_logL in range(0,len(logL[:,0])):
            log_expey_result.append(log_expey(logL[i_logL,0], logL[i_logL,1]))
        log_weight[ith_tree-1] = log_weight[ith_tree-1] + np.sum(log_expey_result) - logL_target[ith_tree-1]
        
        ## smoothing - target wavelet - NOT haar wavelet
        # rho_tilde - posterior spike probability
        # = \frac{1}{ 1 + (1/rho - 1) * M_d_0 /M_d_1 }
        
        M_d_ratio = np.sqrt(1+tau_level)*np.exp(-np.power(w_d,2)/(2*np.power(sigma_hat, 2))/(1+1/tau_level))
        rho_post = 1/(1+(1/rho_level-1)*M_d_ratio)
        
        post_mean = rho_post*w_d/(1+1/tau_level)
        m=0; rec_coef = []
        for i in range(len(wave_level)-1):
            rec_coef.append(np.array(np.append(c[0],post_mean)[m:m+wave_level[i]]))
            m=m+wave_level[i]
        est_target = pywt.waverec(rec_coef, wavelet, 'per')
        est = np.zeros(dimension)
        position_row = position%(dimension[0])-1
        position_col = (np.ceil(position/dimension[0])-1).astype('int16')
        est[position_row,position_col] = est_target
        est_all[:, ith_tree-1] = np.squeeze(est.T.reshape(1,est.size))
    final_weight = normalize(log_weight)
    final_est = np.sum(est_all*final_weight, 1)

    result = {'final_est': final_est,
              'final_weight': final_weight,
              'est_all': est_all}
    return result
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 08:41:12 2022

@author: ivantao
"""
import numpy as np
from numpy import random
import pywt
import math
import pandas as pd
import matplotlib.pyplot as plt
import py_tree
import scipy.io as scio
import os
import re
import csv

def idx2cor(mat, idx):
    #idx:matlab output:python
    row_num = mat.shape[0]
    col = (np.ceil(idx/row_num)-1).astype('int64')
    row = (idx%row_num-1).astype('int64')
    output = {'row':row,'col':col}
    return output
    

def dir2pos_short(direction, prun_num, dimension):
    prun_block = {}
    m = dimension.size
    J = int(math.log2(np.prod(dimension)))
    level = J+1
    dim_level_old = {(1,1):dimension}
    ind = np.array(range(1,np.prod(dimension)+1)).reshape(dimension).T
    ind_level_old = {(1,1):ind}
    dir_l = direction[0]
    node_in = 1
    long_prun = 0
    prun_k = 1
    dim_level_new = {}; ind_level_new = {}
    for l in range(1, level):
        print('Total level:',level,'. Current level:',l,'\n')
        len_level = dir_l.size
        #print('len_level:',len_level)
        long_dir_new = np.squeeze(-2*np.ones((1,2*len_level)))
        long_prun_new = np.squeeze(np.zeros((1,2*len_level)))
        #print('dim_level_old:',dim_level_old,'\n')
        for t in range(1, len_level+1):
            dim0 = dim_level_old[(1,t)]
            ind0 = ind_level_old[(1,t)]
            if dir_l.size==1:
                dir0 = dir_l + 1
            else:
                dir0 = dir_l[t-1]+1
            dir0 = int(dir0)
            if dir0 > 0:
                cut_point = math.floor(dim0[dir0-1]/2)
                dim_tmp=[]
                for i in dim0:
                    dim_tmp.append(i)
                dim_tmp[dir0-1] = cut_point
                dim_level_new[(1,2*(t-1)+1)] = dim_tmp
                dim_level_new[(1,2*t)] = dim_tmp
            if m == 2:
                if dir0 == 1:
                    ind_level_new[(1,2*(t-1)+1)] = ind0[0:cut_point, :]
                    ind_level_new[(1,2*t)] = ind0[cut_point:,:]
                elif dir0 == 2:
                    ind_level_new[(1,2*(t-1)+1)] = ind0[:,0:cut_point]
                    ind_level_new[(1,2*t)] = ind0[:,cut_point:]
                elif dir0 == 0:
                    if dim0[1] > 1:
                        cut_point = math.floor(dim0[1]/2)
                        dim_tmp=[]
                        for i in dim0:
                            dim_tmp.append(i)
                        dim_tmp[1] = cut_point
                        dim_level_new[(1,2*(t-1)+1)] = dim_tmp
                        dim_level_new[(1,2*t)] = dim_tmp
                        ind_level_new[(1,2*(t-1)+1)] = ind0[:,0:cut_point]
                        ind_level_new[(1,2*t)] = ind0[:,cut_point:]
                        long_dir_new[(2*(t-1)):(2*t)] = -1
                    elif dim0[0] > 1:
                        cut_point = math.floor(dim0[0]/2)
                        dim_tmp=[]
                        for i in dim0:
                            dim_tmp.append(i)
                        dim_tmp[0] = cut_point
                        dim_level_new[(1,2*(t-1)+1)] = dim_tmp
                        dim_level_new[(1,2*t)] = dim_tmp
                        ind_level_new[(1,2*(t-1)+1)] = ind0[0:cut_point,:]
                        ind_level_new[(1,2*t)] = ind0[cut_point:,:]
                        long_dir_new[(2*(t-1)):(2*t)] = -1
                    if l>1 and long_prun[t-1]==1:
                        prun_block[(prun_k,1)] = ind0
                        prun_k = prun_k + 1
            elif m == 3:
                if dir0 == 1:
                    ind_level_new[(1,2*(t-1)+1)] = ind0[0:cut_point,:,:]
                    ind_level_new[(1,2*t)] = ind0[cut_point:,:,:]
                elif dir0 ==2:
                    ind_level_new[(1,2*(t-1)+1)] = ind0[:,1:cut_point,:]
                    ind_level_new[(1,2*t)] = ind0[:,cut_point:,:]
                elif dir0 ==3:
                    ind_level_new[(1,2*(t-1)+1)] = ind0[:,:,0:cut_point]
                    ind_level_new[(1,2*t)] = ind0[:,:,cut_point:]
                elif dir0 == 0:
                    if dim0[2]>1:
                        cut_point = math.floor(dim0[2]/2)
                        dim_tmp=[]
                        for i in dim0:
                            dim_tmp.append(i)
                        dim_tmp[2] = cut_point
                        dim_level_new[(1,2*(t-1)+1)] = dim_tmp
                        dim_level_new[(1,2*t)] = dim_tmp
                        ind_level_new[(1,2*(t-1)+1)] = ind0[:,:,0:cut_point]
                        ind_level_new[(1,2*t)] = ind0[:,:,cut_point:]
                        long_dir_new()[(2*(t-1)):(2*t)] = -1
                    elif dim0[1]>1:
                        cut_point = math.floor(dim0[1]/2)
                        dim_tmp=[]
                        for i in dim0:
                            dim_tmp.append(i)
                        dim_tmp[1] = cut_point
                        dim_level_new[(1,2*(t-1)+1)] = dim_tmp
                        dim_level_new[(1,2*t)] = dim_tmp
                        ind_level_new[(1,2*(t-1)+1)] = ind0[:,0:cut_point,:]
                        ind_level_new[(1,2*t)] = ind0[:,cut_point:,:]
                        long_dir_new[(2*(t-1)):(2*t)] = -1
                    elif dim0[0]>1:
                        cut_point = math.floor(dim0[0]/2)
                        dim_tmp=[]
                        for i in dim0:
                            dim_tmp.append(i)
                        dim_tmp[0] = cut_point
                        dim_level_new[(1,2*(t-1)+1)] = dim_tmp
                        dim_level_new[(1,2*t)] = dim_tmp
                        ind_level_new[(1,2*(t-1)+1)] = ind0[0:cut_point,:,:]
                        ind_level_new[(1,2*t)] = ind0[cut_point:,:,:]
                        long_dir_new[(2*(t-1)):(2*t)] = -1
                    if l>1 and long_prun[t-1]==1:
                        prun_block[(prun_k,1)] = ind0
                        prun_k = prun_k + 1
            elif m == 4:
                if dir0 == 1:
                    ind_level_new[(1,2*(t-1)+1)] = ind0[0:cut_point,:,:,:]
                    ind_level_new[(1,2*t)] = ind0[cut_point:,:,:,:]
                elif dir0 ==2:
                    ind_level_new[(1,2*(t-1)+1)] = ind0[:,1:cut_point,:,:]
                    ind_level_new[(1,2*t)] = ind0[:,cut_point:,:,:]
                elif dir0 ==3:
                    ind_level_new[(1,2*(t-1)+1)] = ind0[:,:,0:cut_point,:]
                    ind_level_new[(1,2*t)] = ind0[:,:,cut_point:,:]
                elif dir0 ==4:
                    ind_level_new[(1,2*(t-1)+1)] = ind0[:,:,:,0:cut_point]
                    ind_level_new[(1,2*t)] = ind0[:,:,:,cut_point:]
                elif dir0 == 0:
                    if dim0[3]>1:
                        cut_point = math.floor(dim0[3]/2)
                        dim_tmp=[]
                        for i in dim0:
                            dim_tmp.append(i)
                        dim_tmp[3] = cut_point
                        dim_level_new[(1,2*(t-1)+1)] = dim_tmp
                        dim_level_new[(1,2*t)] = dim_tmp
                        ind_level_new[(1,2*(t-1)+1)] = ind0[:,:,:,0:cut_point]
                        ind_level_new[(1,2*t)] = ind0[:,:,:,cut_point:]
                        long_dir_new()[(2*(t-1)):(2*t)] = -1
                    elif dim0[2]>1:
                        cut_point = math.floor(dim0[2]/2)
                        dim_tmp=[]
                        for i in dim0:
                            dim_tmp.append(i)
                        dim_tmp[2] = cut_point
                        dim_level_new[(1,2*(t-1)+1)] = dim_tmp
                        dim_level_new[(1,2*t)] = dim_tmp
                        ind_level_new[(1,2*(t-1)+1)] = ind0[:,:,0:cut_point,:]
                        ind_level_new[(1,2*t)] = ind0[:,:,cut_point:,:]
                        long_dir_new()[(2*(t-1)):(2*t)] = -1
                    elif dim0[1]>1:
                        cut_point = math.floor(dim0[1]/2)
                        dim_tmp=[]
                        for i in dim0:
                            dim_tmp.append(i)
                        dim_tmp[1] = cut_point
                        dim_level_new[(1,2*(t-1)+1)] = dim_tmp
                        dim_level_new[(1,2*t)] = dim_tmp
                        ind_level_new[(1,2*(t-1)+1)] = ind0[:,0:cut_point,:,:]
                        ind_level_new[(1,2*t)] = ind0[:,cut_point:,:,:]
                        long_dir_new[(2*(t-1)):(2*t)] = -1
                    elif dim0[0]>1:
                        cut_point = math.floor(dim0[0]/2)
                        dim_tmp=[]
                        for i in dim0:
                            dim_tmp.append(i)
                        dim_tmp[0] = cut_point
                        dim_level_new[(1,2*(t-1)+1)] = dim_tmp
                        dim_level_new[(1,2*t)] = dim_tmp
                        ind_level_new[(1,2*(t-1)+1)] = ind0[0:cut_point,:,:,:]
                        ind_level_new[(1,2*t)] = ind0[cut_point:,:,:,:]
                        long_dir_new[(2*(t-1)):(2*t)] = -1
                    if l>1 and long_prun[t-1]==1:
                        prun_block[(prun_k,1)] = ind0
                        prun_k = prun_k + 1
        long_dir_new = np.squeeze(long_dir_new)
        long_prun_new = np.squeeze(long_prun_new)
        if l<(level-1):
            empty_indx = np.squeeze(np.argwhere(long_dir_new==-2))
            if empty_indx.size>0:
                empty_len = empty_indx.size
                long_dir_new[empty_indx] = direction[node_in:(node_in+empty_len)]
                long_prun_new[empty_indx] = 1*(direction[node_in:(node_in+empty_len)]==-1)
                dir_l = long_dir_new
                long_prun = long_prun_new
                node_in = node_in + empty_len
            else:
                dir_l = np.squeeze(long_dir_new)
                long_prun = long_prun_new
                node_in = node_in + 0
        for key,value in dim_level_new.items():
            dim_level_old[key] = value
        for key,value in ind_level_new.items():
            ind_level_old[key] = value
    #position = []
    #for value in ind_level_new.values():
    #    position = np.append(position, value)
    #position = position.astype('int64')
    #output = {'position':position, 'prun_block':prun_block}
    #return output
    return prun_block

class huffmannode(object):
    def __init__(self):
        self.parent = 0
        self.weight = 0
        self.lchild = 0
        self.rchild = 0

def fre_str(str_list):
    str_unique_list = list(set(str_list))
    fre_list = dict.fromkeys(str_unique_list, 0)
    for s in str_list:
        fre_list[s] = fre_list[s] + 1
    return fre_list


# a = fre_str(str_ori_list)
# print(a)

# 在huffman树节点中选择权重最小的两个节点
def selectNode(huffmantree):
    s1 = -1
    s2 = -1
    min1 = -1
    min2 = -1
    for node in huffmantree:
        if node.parent == 0 and node.weight > 0:
            if s1 < 0 or min1 > node.weight:
                s2 = s1
                min2 = min1
                s1 = huffmantree.index(node)
                min1 = node.weight
            elif s2 < 0 or min2 > node.weight:
                s2 = huffmantree.index(node)
                min2 = node.weight

    return s1, s2


# 哈夫曼编码
def huffman_code(str_ori_list,fre_str_dict):
    # 每个节点的权重赋值
    n = len(fre_str_dict)
    m = 2 * len(fre_str_dict) - 1
    huffman_tree = []
    for i in fre_str_dict:
        temp_huffmancode = huffmannode()
        temp_huffmancode.weight = fre_str_dict[i]
        huffman_tree.append(temp_huffmancode)
    # 选择权重最小的两个节点，建立树结构
    for i in range(n, m):
        # 在huffman树节点中选择权重最小的两个节点
        s1, s2 = selectNode(huffman_tree)
        huffman_tree[s1].parent = huffman_tree[s2].parent = i
        temp_huffmancode1 = huffmannode()
        temp_huffmancode1.lchild = s1
        temp_huffmancode1.rchild = s2
        temp_huffmancode1.weight = huffman_tree[s1].weight + huffman_tree[s2].weight
        huffman_tree.append(temp_huffmancode1)
    # 根据构建好的huffman树进行编码
    str_list = list(set(str_ori_list))
    codeing_dict = dict.fromkeys(str_list, None)
    #print(codeing_dict)
    for i in range(0, n):
        temp_list = []
        node = i
        parent = huffman_tree[i].parent
        while parent != 0:
            if huffman_tree[parent].lchild == node:
                temp_list.append(0)
            else:
                temp_list.append(1)
            node = parent
            parent = huffman_tree[node].parent
        codeing_dict[str_list[i]] = list(reversed(temp_list))

    return codeing_dict

def de2bi(de_array):
    bin_all=[];len_bin=[]
    for i in de_array:
        bin0=[]
        if i == 0:
            bin0 = np.append(bin0,np.array([i])).astype('int16')
        while i>0:
            bin0 = np.append(bin0,np.array([i%2])).astype('int16') #a对2求余，添加到字符串m最后
            i=i//2
        bin_array=bin0[::-1]
        bin_all.append(bin_array)
        len_bin.append(bin_array.shape[0])
    #print(bin_all)
    #print(len_bin)
    num_col = np.max(len_bin) 
    num_row = len(de_array)
    bin_mat = np.zeros((num_row,num_col))
    m=0
    for i in bin_all:
        l=len_bin[m]
        bin_mat[m,-l:] = i
        m = m+1
    m=0
    for i in range(math.floor(num_col/2)):
        tmp = bin_mat[:,i].copy()
        bin_mat[:,i] = bin_mat[:,num_col-i-1]
        bin_mat[:,num_col-i-1] = tmp
    return bin_mat.astype('int16')

def hyper_3D_default(obs, dimension, sigma_hat, pruning = True):
    if pruning:
        eta_list = np.array([0.3, 0.4, 0.5])
    else:
        eta_list = np.array([0])
        
    total_level = math.log2(obs.size)
    idx = np.linspace(1, obs.size-1, int(obs.size/2)).astype('int16')
    a = (obs[idx-1] - obs[idx])/math.sqrt(2)

    #last tau, last_rho, alpha, eta
    n_value = np.array([3, 3, 1 ,eta_list.size])
    n_grid = np.prod(n_value)

    last_tau = 1/pow(sigma_hat,2)*np.repeat(np.arange(1,4)/10, n_grid/n_value[0])
    last_rho = np.tile(np.repeat(np.arange(1,4)/10, int(n_grid/n_value[0]/n_value[1])),(1,n_value[0]))
    beta = 1
    alpha = np.tile(np.array([0.5]),(1, int(n_grid/n_value[2])))
    eta = np.tile(eta_list, (1, int(n_grid/n_value[3])))
    adjust = np.zeros((1, n_grid))


    hyper = np.vstack((np.log(beta)+adjust, np.log(last_rho)+math.log(2)*beta*total_level, -np.log(1/eta-1)+adjust, np.log(alpha)+adjust, np.log(last_tau)+alpha*total_level*math.log(2), math.log(sigma_hat)+adjust))
    x = hyper[:,1]
    
    return x
    if pruning:
        eta_list = np.array([0.3, 0.4, 0.5])
    else:
        eta_list = np.array([0])
        
    total_level = math.log2(obs.size)
    idx = np.linspace(1, obs.size-1, int(obs.size/2)).astype('int16')
    a = (obs[idx-1] - obs[idx])/math.sqrt(2)

    #last tau, last_rho, alpha, eta
    n_value = np.array([3, 3, 1 ,eta_list.size])
    n_grid = np.prod(n_value)

    last_tau = 1/pow(sigma_hat,2)*np.repeat(np.arange(1,4)/10, n_grid/n_value[0])
    last_rho = np.tile(np.repeat(np.arange(1,4)/10, int(n_grid/n_value[0]/n_value[1])),(1,n_value[0]))
    beta = 1
    alpha = np.tile(np.array([0.5]),(1, int(n_grid/n_value[2])))
    eta = np.tile(eta_list, (1, int(n_grid/n_value[3])))
    adjust = np.zeros((1, n_grid))


    hyper = np.vstack((np.log(beta)+adjust, np.log(last_rho)+math.log(2)*beta*total_level, -np.log(1/eta-1)+adjust, np.log(alpha)+adjust, np.log(last_tau)+alpha*total_level*math.log(2), math.log(sigma_hat)+adjust))
    x = hyper[:,1]
    
    return x

def if_equal(x, y):
    z = x-y
    return np.count_nonzero(z)

def argwhere2list(x):
    y=[]
    for x1 in x:
        for x2 in x1:
            y.append(x2)
    return y

#mat = pd.read_csv('mat.csv')
#MAP_0 = pd.read_csv('MAP_0.csv')
#mat = mat.values
#MAP_0 = MAP_0.values.astype('int16')
#print('mat:',mat)
#print('MAP:',MAP_0.shape,'\n',MAP_0)

def CARP(mat, hyper):
    #print(mat.shape)
    sigma_hat = 0.01
    dimension = np.array(mat.shape)
    n = mat.size
    total_level = math.log2(n)
    obs = np.squeeze(mat.T.reshape(1,mat.size))
    MAP_0 = np.array(py_tree.get_MAP(obs, dimension, hyper)).astype('int64')

    #layout of 'smp_all'
    direction_1 = MAP_0[:,0]
    pruning_1 = MAP_0[:,1]
    #shorten direction
    pruning_opt = direction_1.copy()
    pruning_opt[pruning_1==1] = 3
    #find all the children
    J = int(math.log2(np.prod(dimension)))
    level = J+1
    L = pruning_opt.size
    for l in range(1,level-1):
        node_l = pruning_opt[(pow(2,l-1)-1):(pow(2,l)-1)]
        indx = argwhere2list(np.argwhere(node_l == 3)+1)
        if len(indx)>0:
            d = len(indx)
            for t in range(1,d+1):
                node_idx = pow(2,l-1)-1+indx[t-1]
                child_indx = []
                for j in range(1,level-l):
                    child_indx = np.append(child_indx, range(node_idx*pow(2,j),node_idx*pow(2,j)+pow(2,j))).astype('int64')
                pruning_opt[child_indx-1] = 4
    ShortenPruning = pruning_opt[pruning_opt!=4]
    LengthRateShort = ShortenPruning.size/L
    ShortenDirection = ShortenPruning.copy()
    ShortenDirection[ShortenDirection==3] = -1
    #ShortenDirection = np.squeeze(np.array(scio.loadmat(path2)['ShortenDirection']))
    prun_num = np.sum(ShortenDirection==-1)
    #output = dir2pos_short(ShortenDirection, prun_num, dimension)
    #position_new = output.get('position')
    #prun_block = output.get('prun_block')
    prun_block = dir2pos_short(ShortenDirection, prun_num, dimension)
    rec_mat = mat.copy()
    comp_mat = mat.T.reshape(mat.size,1)
    total_block_avg = np.zeros((prun_num,1))
    for t in range(1, prun_num+1):
        #print('t:',t)
        block_t = np.squeeze(prun_block[(t,1)])
        if t==1:
            total_block = block_t.T.reshape(block_t.size,1)
        else:
            total_block = np.append(total_block, block_t.T.reshape(block_t.size,1),axis = 0)
        cor1 = idx2cor(rec_mat, block_t)
        total_block_avg[t-1] = np.mean(rec_mat[cor1.get('row'),cor1.get('col')])
        rec_mat[cor1.get('row'),cor1.get('col')] = total_block_avg[t-1]
    comp_mat = np.delete(comp_mat.T,total_block-1).T
    if len(comp_mat)==0:
        comp_mat = total_block_avg
    else:
        comp_mat = np.append(np.array([comp_mat]).T, total_block_avg, axis=0)
    comp_mat_size = len(comp_mat)
    wavelet = pywt.Wavelet('db1')
    rec_c00 = pywt.wavedec(np.squeeze(comp_mat.T), wavelet, 'per', int(math.log2(n)))
    rec_wave_level = []; rec_c0 = []
    for j in rec_c00:
        rec_c0 = np.append(rec_c0, j)
        rec_wave_level.append(len(j))
    #soft_threshold
    r1 = 0.0001
    coeff_mat_rec = rec_c0
    coeff_mat_rec[np.abs(rec_c0)<r1] = 0
    coeff_mat_rec[rec_c0>r1] = coeff_mat_rec[rec_c0>r1]-r1
    coeff_mat_rec[rec_c0<-r1] = coeff_mat_rec[rec_c0<-r1]+r1
    m=0; coeff_mat_rec0 = []
    #print(coeff_mat_rec)
    for i in range(len(rec_wave_level)):
        coeff_mat_rec0.append(np.array(coeff_mat_rec[m:m+rec_wave_level[i]]))
        m=m+rec_wave_level[i]
    rec_mat_vec_final = pywt.waverec(coeff_mat_rec0, wavelet, 'per')
    final_mat = rec_mat
    block_num = len(prun_block)
    for kk in range(1,block_num+1):
        cor2 = idx2cor(final_mat, np.squeeze(prun_block[(kk,1)]))
        final_mat[cor2.get('row'), cor2.get('col')] = rec_mat_vec_final[comp_mat_size-block_num+kk-1]
    rec = final_mat

    #Huffman encoding
    coeff_mat_rec_ed = coeff_mat_rec
    coeff_mat_rec_ed = np.delete(coeff_mat_rec_ed.T, np.squeeze(np.argwhere(coeff_mat_rec_ed==0).T)).T
    coeff_mat_rec_ed = np.floor((coeff_mat_rec_ed - np.min(coeff_mat_rec_ed))/(np.max(coeff_mat_rec_ed)-np.min(coeff_mat_rec_ed))*255)
    prob = fre_str(coeff_mat_rec_ed)
    huff_dict = huffman_code(coeff_mat_rec_ed, prob)
    enco = []
    for i in coeff_mat_rec_ed:
        enco = np.append(enco,huff_dict[i]).astype('int64')
    FinalCompressedImage = enco.size
    #Calculate the compression rate
    binarySig = de2bi(np.abs(np.floor((np.squeeze(255*mat.T.reshape(1,mat.size)))))).astype('int64')
    seqLen = binarySig.size
    compressRate = seqLen/(FinalCompressedImage+math.log2(3)*comp_mat_size)

    #Calculate the PSNR and MSE
    D = np.power(np.abs(mat-final_mat),2)
    mse = np.sum(D)/np.prod(dimension)
    psnr = 10*math.log10(pow(1,2)/mse)
    print('Compression ratio is', round(compressRate,3),'\n')
    print('PSNR value is',round(psnr,3),'\n')
    print('MSE is',round(mse,3),'\n')
    plt.imshow(final_mat)
    return comp_mat, final_mat
                
    
    
    
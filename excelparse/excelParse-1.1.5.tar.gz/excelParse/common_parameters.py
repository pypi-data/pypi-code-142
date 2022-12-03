#!/usr/bin/env python3
# encoding: UTF-8
"""
2022.12.3 by ganjun
Usage: 所有流程通用变量
"""

import os
import yaml

# 目录
PRO_DIR = config["project_dir"]
BIN_DIR = pipe_dir + "/bin"
SCRIPT_DIR = pipe_dir + "/script"
SIF_DIR = pipe_dir + "/sif"
PIPE_DIR = pipe_dir + "/pipeline"

# snakemake rule  配置文件
ruleyaml = open(os.path.join(PRO_DIR,"pipeline.yaml"))
ruleconfig = yaml.load(ruleyaml,Loader = yaml.FullLoader)
ruleyaml.close()

# 流程通用变量
SAMPLES = config["samples"]
GROUPS = config["groups"]

# singularity 挂载信息
roots= []
singularity_args = ''
for i in [PIPE_DIR , PRO_DIR]:
    i = i.split("/")[1]
    roots.append(i)
roots = set(roots)
for i in roots:
    singularity_args += "-B /%s:/%s " %(i,i)
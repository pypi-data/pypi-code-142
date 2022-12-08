from ldimbenchmark import LDIMMethodBase, BenchmarkLeakageResult


from datetime import timedelta
from sklearn.linear_model import LinearRegression
import sklearn
import pickle
import math

import numpy as np
import pandas as pd


class MNF(LDIMMethodBase):
      """
    Minumum Night Flow Method from
    https://github.com/KIOS-Research/LeakDB/tree/master/CCWI-WDSA2018/Detection%20Algorithms/MNF
    """
    def __init__(self):
        super().__init__(
            name="MNF",
            version="1.0",
            # hyperparameters={"est_length": "3 days", "C_threshold": 3, "delta": 4},
        )

    def train(self, train_data):
        pass

    def detect(self, evaluation_data, additional_output_path=""):
# Not implemented, as this is a datapoint

        # MNF code from MATLAB
        # w=10; % window
        # k = 1:w;
        # Labels_Sc=[];

        # MNF = min(reshape(LScFlows,48,365));
        # for j=(w+1):365
        #     minMNFW = min(MNF(k));
        #     e = MNF(j)-minMNFW;
        #     if e>minMNFW*gamma
        #         Labels_Sc(j) = 1;
        #     else
        #         Labels_Sc(j) = 0;
        #         k(w+1) = j;
        #         k(1) = [];
        #     end
        # end

        # Labels_Sc_Final1 = [];
        # j=48;
        # for d=1:size(Labels_Sc,2)
        #     Labels_Sc_Final1(j-47:j,1)=Labels_Sc(d);
        #     j = j+48;
        # end

        # clear Labels_Sc
        # Labels_Sc = [datestr(timeStamps, 'yyyy-mm-dd HH:MM') repmat(', ',length(timeStamps),1) num2str(repmat(Labels_Sc_Final1, 1))];
        # Labels_Sc = cellstr(Labels_Sc);


        results = []
        # for leak_pipe, leak_start in zip(leaks.index, leaks):
        #     results.append(
        #         {
        #             "pipe_id": leak_pipe,
        #             "leak_start": leak_start,
        #             "leak_end": leak_start,
        #             "leak_peak": leak_start,
        #         }
        #     )
        return results

    def detect_datapoint(self, evaluation_data):
        pass

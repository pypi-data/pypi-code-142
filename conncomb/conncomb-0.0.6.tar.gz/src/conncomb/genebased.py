import pandas as pd
import numpy as np
import networkx as nx
import math
import random
import os
from scipy import stats

from conncomb.randomconnectivity import randomConnectivity


def geneBased(disease, network, networkPath, currencyMetaPer, 
        countDataPath, sampleDataPath, diseaseGenesPath, 
        upORdownRegulated, 
        minNumNodesR, numRandomGroups,
        pGRange, fRange,
        diseaseStatus_patient, diseaseStatus_control,
        directory,
        method="geneBase",
        combination = "X0"):     
    
    
    if not os.path.exists("result/"+directory):
        os.makedirs("result/"+directory)
    
# =============================================================================
# Data Import  
# =============================================================================
    ##### Network #####
    GC = nx.read_gexf(networkPath) 
    
    ##### Gene Expression Data #####
    countData = pd.read_csv(countDataPath, index_col=0)
    
    if any("ENSG" in s for s in countData.index):
        countData = countData.T
    
    ##### Patient/Control Data #####
    sampleData = pd.read_csv(sampleDataPath, index_col=0)
    
    ##### GWAS Data #####
    diseaseGenesListEnsembl = pd.read_csv(diseaseGenesPath, index_col=0)         
    
    ##### Gene Centric Metabolic Network & Expression Data Intersection #####
    GCS = GC.subgraph(set(countData.T.index))
    
    
    
# =============================================================================
# Expression Data Cleaning            
# =============================================================================
    
    #patient & control data
    sampleDataS = sampleData.loc[countData.index]

    healthyID = list(sampleDataS[(sampleDataS["diseaseStatus"]==diseaseStatus_control)].index)
    patientID = list(sampleDataS[(sampleDataS["diseaseStatus"]==diseaseStatus_patient)].index)
    
    numSamples = np.min([len(healthyID), len(patientID)])    
    
    Controls = random.sample(healthyID, numSamples)
    Patients = random.sample(patientID, numSamples)
    
    #expression data
    expressionMetabolicS = countData.loc[Patients+Controls, list(GCS.nodes())]    
    expressionMetabolicS = expressionMetabolicS.apply(pd.to_numeric, errors='coerce')
    
    
    fRange = [i for i in fRange if i<=numSamples]
    
    
# =============================================================================
# Connectivity    
# =============================================================================
    
    #connectivity - control
    
    connAnalysisControlAll = connectivityGeneBase(GCS, expressionMetabolicS, Controls, 
                                                  pGRange, fRange, upORdownRegulated)
    
    #connectivity - patient
    
    connAnalysisPatientsAll = connectivityGeneBase(GCS, expressionMetabolicS, Patients, 
                                                   pGRange, fRange, upORdownRegulated)
    
    
    #number of nodes
    numNodEdgC = connAnalysisControlAll[1]
    numNodEdgP = connAnalysisPatientsAll[1]
    
    #connectivity random
    randomConnectivityData = randomConnectivity(GCS, numNodEdgP, numNodEdgC, numRandomGroups)
    
    randomConnectivityControlMean = randomConnectivityData[0]
    randomConnectivityControlStd = randomConnectivityData[1]
    randomConnectivityPatientMean = randomConnectivityData[2]
    randomConnectivityPatientStd = randomConnectivityData[3]
    
# =============================================================================
# Min Number of Nodes Limit & Max Diff     
# =============================================================================
    resultDF0 = pd.DataFrame()
    
    for minNumNodes in minNumNodesR:
        
        #revise control connectivity wrt min num of nodes
        numNodEdgBinC = np.where(numNodEdgC<minNumNodes,0,1)
        connAnalysisControl = connAnalysisControlAll[0]*numNodEdgBinC
        
        #revise patient connectivity wrt min num of nodes
        numNodEdgBinP = np.where(numNodEdgP<minNumNodes,0,1)
        connAnalysisPatients = connAnalysisPatientsAll[0]*numNodEdgBinP
        
        connAnalysisDiff = connAnalysisPatients-connAnalysisControl
        
        #revise random connectivity wrt min num of nodes
        randomConnectivityControlMeanB = randomConnectivityControlMean * numNodEdgBinC
        randomConnectivityControlStdB = randomConnectivityControlStd * numNodEdgBinC
        randomConnectivityPatientMeanB = randomConnectivityPatientMean * numNodEdgBinP
        randomConnectivityPatientStdB = randomConnectivityPatientStd * numNodEdgBinP
        
        #avoid dividing by zero
        randomConnectivityControlStdB = randomConnectivityControlStdB.replace(0, 1)
        randomConnectivityPatientStdB = randomConnectivityPatientStdB.replace(0, 1)
        
        #calculate z-scores
        connAnalysisControl_zscore = (connAnalysisControl-randomConnectivityControlMeanB)/randomConnectivityControlStdB
        connAnalysisPatient_zscore = (connAnalysisPatients-randomConnectivityPatientMeanB)/randomConnectivityPatientStdB
        zScoreDiff = connAnalysisPatient_zscore-connAnalysisControl_zscore
     
    
        # find the index that max diff
        indexMaxZ = list(zScoreDiff.stack().idxmax())
        #maxZscore = zScoreDiff.max().max()
       
    
        ##### Max Diff Filtered Genes #####
        pGZ, fZ = indexMaxZ

        numUpDownZ = math.ceil(len(expressionMetabolicS) * pGZ)
        
        
        PatientGenesZ_patients = filteredGenesGeneBase(GCS, Patients, expressionMetabolicS,
                                                numUpDownZ, fZ, upORdownRegulated)
        
        PatientGenesZ_controls = filteredGenesGeneBase(GCS, Controls, expressionMetabolicS,
                                                numUpDownZ, fZ, upORdownRegulated)
        
        #connectivity
        SPZ = GCS.subgraph(PatientGenesZ_patients)        
        
        
        ##### GWAS Match #####
        IntersectionZ = len(set(SPZ.nodes()).intersection(set(list(diseaseGenesListEnsembl.ensembl))))
        detectedDiseaseGenesZ = set(SPZ.nodes()).intersection(set(list(diseaseGenesListEnsembl.ensembl)))
        diseaseGenesInGraph = len(set(GCS.nodes()).intersection(set(list(diseaseGenesListEnsembl.ensembl))))
    
        
# =============================================================================
# Intersection vs Random    
# =============================================================================
        if SPZ.number_of_nodes() == GCS.number_of_nodes():
                        
            intRandomMeanZ = IntersectionZ#####################
            intRandomStdZ = 0
            intZscoreZ = 0
            
        elif SPZ.number_of_nodes() == 0:
            intRandomMeanZ = 0
            intRandomStdZ = 0
            intZscoreZ = 0       
            
        else:
            numDetGeneZ = SPZ.number_of_nodes()
            
            intersectionSampleSizeZ=[]
            for i in range(numRandomGroups):
                sampZ = random.sample(list(expressionMetabolicS.columns), numDetGeneZ)
                intersectionSampleZ = len(set(diseaseGenesListEnsembl.ensembl).intersection(set(sampZ)))
                intersectionSampleSizeZ.append(intersectionSampleZ)
                
        
            intRandomMeanZ = np.mean(intersectionSampleSizeZ)
            intRandomStdZ = np.std(intersectionSampleSizeZ)
            intZscoreZ = (IntersectionZ-intRandomMeanZ)/intRandomStdZ########################
       
# =============================================================================
#     
# =============================================================================
        
        # find the index that max diff
        indexMaxC = list(connAnalysisDiff.stack().idxmax())
        #maxZscore = zScoreDiff.max().max()
       
    
        ##### Max Diff Filtered Genes #####
        pGC, fC = indexMaxC

        numUpDownC = math.ceil(len(expressionMetabolicS) * pGC)
        
        
        PatientGenesC_patients = filteredGenesGeneBase(GCS, Patients, expressionMetabolicS,
                                                numUpDownC, fC, upORdownRegulated)
        
        PatientGenesC_controls = filteredGenesGeneBase(GCS, Controls, expressionMetabolicS,
                                                numUpDownC, fC, upORdownRegulated)
        
        #connectivity
        SPC = GCS.subgraph(PatientGenesC_patients)        
        
        
        ##### GWAS Match #####
        IntersectionC = len(set(SPC.nodes()).intersection(set(list(diseaseGenesListEnsembl.ensembl))))
        detectedDiseaseGenesC = set(SPC.nodes()).intersection(set(list(diseaseGenesListEnsembl.ensembl)))
        #diseaseGenesInGraph = len(set(GCS.nodes()).intersection(set(list(diseaseGenesListEnsembl.ensembl))))
    
 
        if SPC.number_of_nodes() == GCS.number_of_nodes():
                        
            intRandomMeanC = IntersectionC#####################
            intRandomStdC = 0
            intZscoreC = 0
            
        elif SPC.number_of_nodes() == 0:
            intRandomMeanC = 0
            intRandomStdC = 0
            intZscoreC = 0       
            
        else:
            numDetGeneC = SPC.number_of_nodes()
            
            intersectionSampleSizeC=[]
            for i in range(numRandomGroups):
                sampC = random.sample(list(expressionMetabolicS.columns), numDetGeneC)
                intersectionSampleC = len(set(diseaseGenesListEnsembl.ensembl).intersection(set(sampC)))
                intersectionSampleSizeC.append(intersectionSampleC)
                
        
            intRandomMeanC = np.mean(intersectionSampleSizeC)
            intRandomStdC = np.std(intersectionSampleSizeC)
            intZscoreC = (IntersectionC-intRandomMeanC)/intRandomStdC########################

# =============================================================================
#  Save       
# =============================================================================
        
        resultDict = {"disease":disease, "network": network,
                    "currencyMetaPer": currencyMetaPer,
                    "upORdownRegulated": upORdownRegulated,
                    "method": method,
                    "combination": combination,
                    "minNumberNodes": minNumNodes, #eliminate graphs that has less than "minNumberNodes" nodes
                    "numRandomGroups":numRandomGroups,#number of randomly generated groups to estimate avg, std connectivity
                    "numNodes":GCS.number_of_nodes(),
                    "numEdges":GCS.number_of_edges(),
                    "numSamples":numSamples, #patient+control
                    
                    "numDiseaseGenes":len(diseaseGenesListEnsembl),
                    "numDiseaseGenesInGraph":diseaseGenesInGraph,
                    
                    
                    "numDetectedDiseaseGenesBYZ":SPZ.number_of_nodes(),
                    
                    "subgraphEdgesBYZ":SPZ.number_of_edges(),
                    "maxDiffIndex_pG_BYZ":indexMaxZ[0],
                    "maxDiffIndex_f_BYZ":indexMaxZ[1],
                    
                    "maxDiffPatientConn_BYZ":connAnalysisPatients.loc[pGZ, fZ],
                    "maxDiffControlConn_BYZ":connAnalysisControl.loc[pGZ, fZ],
                    "maxDiffConnDiff_BYZ":connAnalysisPatients.loc[pGZ, fZ]-connAnalysisControl.loc[pGZ, fZ],
                    "maxDiffPatientZScore_BYZ":connAnalysisPatient_zscore.loc[pGZ, fZ],
                    "maxDiffControlZScore_BYZ":connAnalysisControl_zscore.loc[pGZ, fZ],
                    "maxDiffZScoreDiff_BYZ":connAnalysisPatient_zscore.loc[pGZ, fZ]-connAnalysisControl_zscore.loc[pGZ, fZ],
                    
                    "intersection_BYZ":IntersectionZ,
                    
                    "randomIntersectionNumNodesMean_BYZ": intRandomMeanZ,
                    "randomIntersectionNumNodesStd_BYZ": intRandomStdZ,
                    "randomIntersectionNumNodesZScore_BYZ": intZscoreZ,
                    
                    
                    
                    "numDetectedDiseaseGenesBYC":SPC.number_of_nodes(),
                    
                    "subgraphEdgesBYC":SPC.number_of_edges(),
                    "maxDiffIndex_pG_BYC":indexMaxC[0],
                    "maxDiffIndex_f_BYC":indexMaxC[1],
                    
                    "maxDiffPatientConn_BYC":connAnalysisPatients.loc[pGC, fC],
                    "maxDiffControlConn_BYC":connAnalysisControl.loc[pGC, fC],
                    "maxDiffConnDiff_BYC":connAnalysisPatients.loc[pGC, fC]-connAnalysisControl.loc[pGC, fC],
                    
                    
                    "intersection_BYC":IntersectionC,
                    
                    "randomIntersectionNumNodesMean_BYC": intRandomMeanC,
                    "randomIntersectionNumNodesStd_BYC": intRandomStdC,
                    "randomIntersectionNumNodesZScore_BYC": intZscoreC
                    
                    }
        
        resultDF = pd.DataFrame.from_dict(resultDict, orient="index")
        resultDF0 = pd.concat([resultDF0, resultDF.T])
      
        
        fn1="result/" + directory + "/"
        fn2= "_" +method + "_" + combination + "_" + disease +"_"+ network + "_" + upORdownRegulated + "_currMet" + str(currencyMetaPer).replace(".", "") +"_minNode"+str(minNumNodes)+ ".csv"
        
        resultDF0.to_csv(fn1+"resultSummary"+fn2)
        
        pd.DataFrame(PatientGenesZ_patients).to_csv(fn1+"patientGeneListBYZ"+fn2)
        pd.DataFrame(PatientGenesZ_controls).to_csv(fn1+"controlGeneListBYZ"+fn2)
        pd.DataFrame(detectedDiseaseGenesZ).to_csv(fn1+"detectedDiseaseGenesBYZ"+fn2)
        
        pd.DataFrame(PatientGenesC_patients).to_csv(fn1+"patientGeneListBYC"+fn2)
        pd.DataFrame(PatientGenesC_controls).to_csv(fn1+"controlGeneListBYC"+fn2)
        pd.DataFrame(detectedDiseaseGenesC).to_csv(fn1+"detectedDiseaseGenesBYC"+fn2)
        
        numNodEdgC.to_csv(fn1+"numberNodesControl"+fn2)
        numNodEdgP.to_csv(fn1+"numberNodesPatient"+fn2)
        
        zScoreDiff.to_csv(fn1+"zScoreDiff"+fn2)
        connAnalysisControl_zscore.to_csv(fn1+"connAnalysisControl_zscore"+fn2)
        connAnalysisPatient_zscore.to_csv(fn1+"connAnalysisPatient_zscore"+fn2)
                
                
        connAnalysisPatients.to_csv(fn1+"connAnalysisPatients"+fn2)
        connAnalysisControl.to_csv(fn1+"connAnalysisControl"+fn2)
        
        randomConnectivityControlMean.to_csv(fn1+"randomConnectivityControlMean"+fn2)
        randomConnectivityControlStd.to_csv(fn1+"randomConnectivityControlStd"+fn2)
        randomConnectivityPatientMean.to_csv(fn1+"randomConnectivityPatientMean"+fn2)
        randomConnectivityPatientStd.to_csv(fn1+"randomConnectivityPatientStd"+fn2)        
        
        
    #return resultDF0






def filteredGenesGeneBase(G, Patients, expressionMetabolic, numUpDown, f,
                          upORdownRegulated):
    
    
    
    expressionMetabolicBinary = pd.DataFrame(index=expressionMetabolic.index,
                                           columns=expressionMetabolic.columns, data=0)

    for i in list(expressionMetabolic.columns):
        if upORdownRegulated == "updown":
            z = np.abs(stats.zscore(expressionMetabolic.loc[:,i]))
            z = pd.Series(z)
            patientsList = list(z.sort_values(ascending=False).head(numUpDown).index)
        
        elif upORdownRegulated == "up":
            z = stats.zscore(expressionMetabolic.loc[:,i])
            z = pd.Series(z)
            patientsList = list(z.sort_values(ascending=False).head(numUpDown).index)
            
        elif upORdownRegulated == "down":
            z = stats.zscore(expressionMetabolic.loc[:,i])
            z = pd.Series(z)
            patientsList = list(z.sort_values(ascending=False).tail(numUpDown).index)      
        
        #expressionMetabolic.loc[:,i] = 0
        expressionMetabolicBinary.loc[patientsList,i] =1 
 
    
    allDiseaseRelated={}
        
    for i in (Patients):       
        patientGenes = list(expressionMetabolicBinary.columns[expressionMetabolicBinary.loc[i, ]==1])
        #count each gene
        for ii in patientGenes:
            if ii in allDiseaseRelated.keys():
                allDiseaseRelated[ii]=allDiseaseRelated[ii]+1
            else:
                allDiseaseRelated[ii]=1

    filteredPatientGenesList=[]

    if f > 0:
        for (key, value) in allDiseaseRelated.items():
            if value>=f:
                filteredPatientGenesList.append(key)
    elif f < 0:
        for (key, value) in allDiseaseRelated.items():
            if value<=-f:
                filteredPatientGenesList.append(key)
    elif f == 0:
        filteredPatientGenesList = list(allDiseaseRelated.keys())
        
    return filteredPatientGenesList



def connectivityGeneBase(G, expressionMetabolic, Patients,
                         pGRange, fRange, upORdownRegulated="updown"):  
    
    """
    G: gene centric metabolic network
    expressionMetabolic: expression matrix
    Patients: patients list
    pGRange: density values list
    fRange: filtering threshold values list
    minNumEdges: graphs that have less than "minNumEdges" edges will be eliminated
    """  

    
    connP = pd.DataFrame(index=pGRange, columns=fRange)
    numNodEdg = pd.DataFrame(index=pGRange, columns=fRange)
   
    for pG in (pGRange):
        
        numUpDown = math.ceil(len(expressionMetabolic) * pG)
        
        for f in fRange:

            PatientGenes = filteredGenesGeneBase(G, Patients, expressionMetabolic,
                                                    numUpDown, f, upORdownRegulated)                              
            
            #connectivity
            SP = G.subgraph(PatientGenes)
            
            if SP.number_of_nodes() > 1:
                connectivityP = 1-(nx.number_of_isolates(SP) / SP.number_of_nodes())
            else:
                connectivityP=0

            connP.loc[pG, f] = connectivityP
            numNodEdg.loc[pG, f] = SP.number_of_nodes()#, SP.number_of_edges())
            
    connP = connP.apply(pd.to_numeric, errors='coerce')
            
    return connP, numNodEdg



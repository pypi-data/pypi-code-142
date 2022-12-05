import pandas as pd
import math
# !pip install networkx[default]
# !pip install matplotlib==3.1.3
import networkx as nx
import numpy as np
np.random.seed(1000)
from pprint import pprint
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def init_graph_attr1(G,crop,statesList,taluk_attri_Dict,states): 
  nodeAttr = {}
  init_graph1(G,states,crop,statesList)
  for i in range(len(states)):
      temp = {}
      temp['OldDeltaVector'] = np.zeros(2)
      temp["DeltaVectornodesStress"] = 0 
      temp['NewDeltaVector'] = np.zeros(2)
      temp["sdgvec"] = taluk_attri_Dict[statesList[i]]
      temp["tempsdgvec"] = taluk_attri_Dict[statesList[i]]
      temp["oldsdgvec"] = taluk_attri_Dict[statesList[i]]
      temp["nodesStress"] = 0
      temp["meansdg"] = np.mean(taluk_attri_Dict[statesList[i]])
      temp["name"] = statesList[i]
      # temp["Tempsdgvec"] = stateSDGDict[i] 
      nodeAttr[i] = temp
  print(nodeAttr)
  nx.set_node_attributes(G, nodeAttr)

def init_graph1(G,states,crop,statesList): #states is a dataframe
    G.add_nodes_from([i for i in range(0,len(states))])
    # print(len(states))
    labels = {}
    labels = states.columns
    print(labels[0])
    for i in range(len(states)):
      #  labels[i] = statesList[i]
      #  print(states.columns[1][i])
      #  print( states[labels[0]][i])
       snode=  states[labels[0]][i]-1
       temp = states[labels[2]][i]
      #  print(temp)
      #  temp=states[str(states.columns[2])][i]
       #print(temp)
       if ',' in str(temp):
          sedge_arr=temp.split(',')
          #print(sedge_arr)
          for i in range(0,len(sedge_arr)):
              G.add_edge(snode,int(sedge_arr[i])-1)
              
       elif math.isnan(temp) :
          print()
       else :
          G.add_edge(snode,temp-1)
          # print(snode,temp-1)
    # my_pos = nx.spring_layout(G, seed = 1000)
    # node_sizes = df[crop]*3000
    # print(statesList)
    # H1=nx.draw(G,pos=my_pos,with_labels=True, labels=labels,node_size=node_sizes,node_color=df[crop].astype(float)*300, cmap=plt.cm.Blues)
    return 

def getMeanSDGGraph2(G,label,num):
  meanSDG = 0
  for n in G.nodes():
    meanSDG += np.mean(np.array(G.nodes[n][label]))
  #print(meanSDG," ",num)
  return meanSDG / num

def getGraphStress2(G,label):
  for n in G.nodes():
    nodeStress = 0
    neigList = list(G.neighbors(n))
    for nei in neigList:
      a = np.array(G.nodes[n][label])
      b = np.array(G.nodes[nei][label])
      nodeStress += np.linalg.norm((a - b), ord=1)
    G.nodes[n]["nodesStress"] = nodeStress
    
  stress = 0
  for n in G.nodes():
    stress += G.nodes[n]["nodesStress"]
  return stress

def StressReduction(G, label1,label2,numSDG):
  for n in G.nodes():
      nodeStress = 0
      neigList = list(G.neighbors(n))
      a = np.zeros(numSDG)
      for nei in neigList:
        a = np. add(a,np.array(G.nodes[nei][label1]))
      if len(neigList)!=0:
        a = a/len(neigList)
        G.nodes[n][label2] = np.add(G.nodes[n][label2],np.add(a,-1*np.array(G.nodes[n][label1]))).tolist()
  for n in G.nodes():
    G.nodes[n][label1] = G.nodes[n][label2].copy()
  return 


def graphCalliberation(numRounds,EpsilonStress,crop,statesList,numSDG,final,attribute_list,taluk_attri_Dict,states):
  statesDict = {}
  for i in statesList:
    statesDict[i] = []
  G3= nx.Graph()
  MeanSDGs = []
  MeanStress = [] 
  XAxis = []
  init_graph_attr1(G3,crop,statesList,taluk_attri_Dict,states)
  # print("Punjabs SDG 5 after Policy Intervention:",G2.nodes[19]['sdgvec'])
  # PolicyIntervention(G,label,nodeIDs,Policies)
  for i in range(numRounds):
    temp1 = getMeanSDGGraph2(G3,"sdgvec",len(attribute_list))
    temp2 = getGraphStress2(G3,"sdgvec")
    XAxis.append(i)
    #print(" Mean SDG Graph is: ",temp1," Graph Stress is:",temp2)
    MeanSDGs.append(temp1)
    MeanStress.append(temp2)
    for n in G3.nodes(): 
      print(G3.nodes[n]["name"])
      statesDict[G3.nodes[n]["name"]].append(G3.nodes[n]["sdgvec"])
    if temp2>=EpsilonStress:
      # PolicyIntervention(G,Policies,NodeIDs,numSDGs,label)
      StressReduction(G3,"sdgvec" ,"tempsdgvec",numSDG)
    else:
      break
  print("Till her it cames\n")
  for n in G3.nodes(): 
    statesDict[G3.nodes[n]["name"]].append(G3.nodes[n]["sdgvec"])
  print("Till here also it cames\n")
  return statesDict


def StressModelling(numNodes,numSDG,numOfRounds,BeforeATEFile,AfterATEFile,adjList):
    # Importing neccessary libraries
 

    # numNodes = 10  # Input 
    # numSDG = 2  #Input
    # numOfRounds = 3 #Input 
    myseed = 1000
    epsilonStress = 0.5
    maxRounds = 1000 
    numPolicies = 100
    # BeforeATEFile = "/content/sample_data/ATEAfter.xlsx" #Input 
    # AfterATEFile = '/content/sample_data/ATEBefore.xlsx' #Input 
    # adjList = '/content/sample_data/Adjacent list ac zones.xlsx' #Input 
    df = pd.read_excel(BeforeATEFile)
    df2=pd.read_excel(AfterATEFile)
    attribute_list= list(df.columns[2:])
    labels = list(df[df.columns[1]])
    print(attribute_list)
    print(labels)

    df['sdgvec'] = df[attribute_list].values.tolist()
    taluk_attri_Dict = dict(zip(df[df.columns[1]], df.sdgvec))
    df2['sdgvec'] = df2[attribute_list].values.tolist()
    states=pd.read_excel(adjList)
    statesList = list(states[states.columns[1]])
    print("States is: ")
    print(states)
    # G1 = nx.Graph()
    # init_graph_attr1(G1,attribute_list[0])
    final = {}
    return graphCalliberation(numOfRounds,epsilonStress,attribute_list[0],statesList,numSDG,final,attribute_list,taluk_attri_Dict,states)

# Results = StressModelling(10,2,3,r"./ATEBefore.xlsx",r"./ATEAfter.xlsx",r"./Adjacent list ac zones.xlsx")
# def print_obj(Results):
#   for i in Results.keys():
#     print(Results[i])
# print_obj(Results)

# [1, 0.6072341817382682, 0.27183721596378846]
# [2, 0.6052543238455066, 0.47738041800580117]
# [3, 0.6410805675368592, 0.48453300733656623]
# [4, 0.6065932080056674, 0.38434592963797076]
# [5, 0.6100092966386761, 0.33331147865550675]
# [6, 0.6084824906414215, 0.31281713769793634]
# [7, 0.6034939935041791, 0.3100125548854487]
# [8, 0.6083756577938256, 0.3121952851981454]
# [9, 0.6101261019554216, 0.32884948600885133]
# [10, 0.6084663183549093, 0.3272474482163977]



#3Version 2 Code ( fake git lessgo)
import pandas as pd
import math
# !pip install networkx[default]
# !pip install matplotlib==3.1.3
import networkx as nx
import numpy as np
np.random.seed(1000)
from pprint import pprint
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import os 



# class Graph:
#     G = nx.Graph()
#     nodeAttr = {}
#     def __init__(self,graph,attributes):
#         self.G = graph
#         self.nodeAttr = attributes
class Scalarization:
    def __init__(self):
        pass
    
    def L2_Norm(self,val1,val2,val3):
        return (val1**2+val2**2+val3**3)**(0.5)

    def ATE(self,val1,val2,val3):
        return (val1*1+val2*2+val3*3)/3
    
    def getFunction(self,selection="L2 Norm"):
        if selection=="L2 Norm":
            return self.L2_Norm
        elif selection == "ATE":
            return self.ATE

#add more here

class GraphCreator:
    BeforeInterventionFile = ""
    AfterInterventionFile = "" 
    adjList = ""
    def getMeanSDGGraph2(self,label):
        meanSDG = 0
        for n in self.G.nodes():
            meanSDG += np.mean(np.array(self.G.nodes[n][label]))
        #print(meanSDG," ",num)
        return meanSDG / self.values.no_attri

    def getGraphStress2(self,label):
        for n in self.G.nodes():
            nodeStress = 0
            neigList = list(self.G.neighbors(n))
            for nei in neigList:
                a = np.array(self.G.nodes[n][label])
                b = np.array(self.G.nodes[nei][label])
                nodeStress += np.linalg.norm((a - b), ord=1)
            self.G.nodes[n]["nodesStress"] = nodeStress
            
        stress = 0
        for n in self.G.nodes():
            stress += self.G.nodes[n]["nodesStress"]
        return stress

    def __init__(self):
        # self.BeforeATEFile = BeforeATEFile
        # self.AfterATEFile = AfterATEFile
        # self.adjList = adjList
        pass
        # return self.MakeGraph()

    def MakeGraph(self,BeforeInterventionFolder,AfterInterventionFolder,adjList,col_select =[2,3],function ="L2 Norm"):
        scalrization_func=Scalarization().getFunction(function)
        self.values=Values(BeforeInterventionFolder, AfterInterventionFolder,adjList,col_select,scalrization_func)
        self.G= nx.Graph()
        self.init_graph_attr1()
        return self

    def init_graph_attr1(self): 
        nodeAttr = {}
        self.init_graph1()
        for i in range(self.values.no_nodes):
            temp = {}
            # temp['OldDeltaVector'] = np.zeros(2)
            temp["DeltaVectornodesStress"] = 0 
            # temp['NewDeltaVector'] = np.zeros(2)
            temp["sdgvec"] = self.values.node_attri_dict[self.values.node_list[i]]
            temp["tempsdgvec"] = self.values.node_attri_dict[self.values.node_list[i]]
            temp["oldsdgvec"] = self.values.node_attri_dict[self.values.node_list[i]]
            temp["nodesStress"] = 0
            temp["meansdg"] = np.mean(self.values.node_attri_dict[self.values.node_list[i]])
            temp["name"] = self.values.node_list[i]
            nodeAttr[i] = temp
        print(nodeAttr)
        nx.set_node_attributes(self.G, nodeAttr)

    def init_graph1(self): #states is a dataframe
        self.G.add_nodes_from([i for i in range(0,self.values.no_nodes)])
        labels = {}
        labels = self.values.node_adj_frame.columns
        print(labels)
        print(self.values.node_adj_frame)
        for i in range(self.values.no_nodes):
            snode=  self.values.node_adj_frame[labels[0]][i]-1
            temp = self.values.node_adj_frame[labels[2]][i]
            if ',' in str(temp):
                sedge_arr=temp.split(',')
                for i in range(0,len(sedge_arr)):
                    self.G.add_edge(snode,int(sedge_arr[i])-1)
                    
            elif math.isnan(temp) :
                print()
            else :
                self.G.add_edge(snode,temp-1)
        return
     
class Values:
    def __init__(self,BeforeFolder, AfterFolder, AdjFile,col_select,sclarisation_func):
        self.BeforeFolder= BeforeFolder
        self.AfterFolder = AfterFolder
        self.AdjFile=AdjFile
        self.col_select=col_select
        self.sclarisation_func=sclarisation_func
        self.node_list=[]
        self.attr_list =[]
        self.node_attri_dict=[]
        self.node_adj_frame = None
        self.no_nodes =None
        self.no_attri = None
        self.populate_after()

    def preprocess(self,Folder): # col_select =[2,3]
        df = pd.DataFrame()
        attribute_dict={}
        for filename in os.listdir(Folder):
            # print(filename.split(" ")[0])
            cntr=0
            self.node_list.append(filename.split(" ")[0])
            tempExcel = pd.read_excel(Folder+"/"+filename)
            if cntr==0:
                for i in self.col_select:
                    attribute_dict[tempExcel.iloc[i][0]]=[]
                self.attr_list=attribute_dict.keys()
                cntr+=1
        self.no_nodes=len(self.node_list)
        self.no_attri=len(self.attr_list)
        for filename in os.listdir(Folder):
            for j in self.col_select: 
                scalarvalue= self.sclarisation_func(float(tempExcel.iloc[j][1]),float(tempExcel.iloc[j][3]),float(tempExcel.iloc[j][4]))
                attribute_dict[tempExcel.iloc[j][0]].append(scalarvalue)
        print(attribute_dict)
        df["Nodes"] = self.node_list
        for attribute in self.attr_list:
            df[attribute] = attribute_dict[attribute]  
        return df

    def populate_after(self):
        #df = pd.read_excel(BeforeATEFile)
        df= self.preprocess(self.AfterFolder)
        df['sdgvec'] = df[self.attr_list].values.tolist()
        self.node_attri_dict = dict(zip(df["Nodes"], df.sdgvec))
        # df2['sdgvec'] = df2[attribute_list].values.tolist()
        self.node_adj_frame=pd.read_excel(self.AdjFile)


class Root:
    def __init__(self):
        self.ReturnObject=[]
    def StressModelling(self,Graph_obj,numRounds,EpsilonStress,SM_function ="gradient_descent"):
        NodesDict = {}
        for i in Graph_obj.values.node_list:
            NodesDict[i] = []
        MeanSDGs = []
        MeanStress = [] 
        Graph_obj.init_graph_attr1()
        print("Number Of Rounds :"+str(numRounds))
        # print("Punjabs SDG 5 after Policy Intervention:",G2.nodes[19]['sdgvec'])
        # PolicyIntervention(G,label,nodeIDs,Policies)
        for i in range(numRounds):
            # print(i)
            temp1 = Graph_obj.getMeanSDGGraph2("sdgvec")
            temp2 = Graph_obj.getGraphStress2("sdgvec")
            #print(" Mean SDG Graph is: ",temp1," Graph Stress is:",temp2)
            MeanSDGs.append(temp1)
            MeanStress.append(temp2)
            for n in Graph_obj.G.nodes(): 
                print(Graph_obj.G.nodes[n]["name"])
                NodesDict[Graph_obj.G.nodes[n]["name"]].append(Graph_obj.G.nodes[n]["sdgvec"])
            if temp2>=EpsilonStress:
            # PolicyIntervention(G,Policies,NodeIDs,numSDGs,label)
                func=StressReduction().getFunction(SM_function)
                print(func)
                func(Graph_obj.G,"sdgvec" ,"tempsdgvec",Graph_obj.values.no_attri)
            else:
                print(i,"stress less than epsilon")
                break
        print("Till her it cames\n")
        for n in Graph_obj.G.nodes(): 
            NodesDict[Graph_obj.G.nodes[n]["name"]].append(Graph_obj.G.nodes[n]["sdgvec"])
        print("Till here also it cames\n")
        return NodesDict


class StressReduction:
    def __init__(self) -> None:
        pass

    def Gradient_Descent(self,G,label1,label2,numSDG):
        for n in G.nodes():
            nodeStress = 0
            neigList = list(G.neighbors(n))
            a = np.zeros(numSDG)
            for nei in neigList:
                a = np. add(a,np.array(G.nodes[nei][label1]))
            if len(neigList)!=0:
                a = a/len(neigList)
                G.nodes[n][label2] = np.add(G.nodes[n][label2],np.add(a,-1*np.array(G.nodes[n][label1]))).tolist()
        for n in G.nodes():
            G.nodes[n][label1] = G.nodes[n][label2].copy()
        return 
    
    def getFunction(self,SM_function):
        if SM_function=="gradient_descent":
            return self.Gradient_Descent

# Test CODE
# Graph_obj1=GraphCreator().MakeGraph(BeforeInterventionFolder=r"C:\Users\sowmi\OneDrive\Desktop\studies\20 credit project\New folder\Package\StressModellingPackageTest\Before",AfterInterventionFolder=r"./After",adjList=r"./Adjacent list ac zones.xlsx",function="L2 Norm")
# Graph_obj2=GraphCreator().MakeGraph(BeforeInterventionFolder=r"C:\Users\sowmi\OneDrive\Desktop\studies\20 credit project\New folder\Package\StressModellingPackageTest\Before",AfterInterventionFolder=r"./After",adjList=r"./Adjacent list ac zones.xlsx",function ="ATE")
# result2=Root().StressModelling(Graph_obj1,numRounds=10,EpsilonStress=0)
# result3=Root().StressModelling(Graph_obj2,numRounds=10,EpsilonStress=0)
# print (result1)
# print("-------------------------------------------------------------------------")
# print (result2)
# print("-------------------------------------------------------------------------")
# print (result3)
# print("-------------------------------------------------------------------------")

# class ATECalculationMethods:


# class VizualizationMethods:


# def StressModelling():



# Version 2 (With Updated result object and stress modelling working on copy og graph object)
import pandas as pd
import copy
import math
# !pip install networkx[default]
# !pip install matplotlib==3.1.3
import networkx as nx
import numpy as np
np.random.seed(1000)
from pprint import pprint
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import os 



# class Graph:
#     G = nx.Graph()
#     nodeAttr = {}
#     def __init__(self,graph,attributes):
#         self.G = graph
#         self.nodeAttr = attributes
class Scalarization:
    def __init__(self):
        pass
    
    def L2_Norm(self,val1,val2,val3):
        return (val1**2+val2**2+val3**3)**(0.5)

    def ATE(self,val1,val2,val3):
        return (val1*1+val2*2+val3*3)/3
    
    def getFunction(self,selection="L2 Norm"):
        if selection=="L2 Norm":
            return self.L2_Norm
        elif selection == "ATE":
            return self.ATE
        return selection

#add more here

class GraphCreator:
    BeforeInterventionFile = ""
    AfterInterventionFile = "" 
    adjList = ""
    def getMeanSDGGraph2(self,label):
        meanSDG = 0
        for n in self.G.nodes():
            meanSDG += np.mean(np.array(self.G.nodes[n][label]))
        #print(meanSDG," ",num)
        return meanSDG / self.values.no_attri

    def getGraphStress2(self,label):
        for n in self.G.nodes():
            nodeStress = 0
            neigList = list(self.G.neighbors(n))
            for nei in neigList:
                a = np.array(self.G.nodes[n][label])
                b = np.array(self.G.nodes[nei][label])
                nodeStress += np.linalg.norm((a - b), ord=1)
            self.G.nodes[n]["nodesStress"] = nodeStress
            
        stress = 0
        for n in self.G.nodes():
            stress += self.G.nodes[n]["nodesStress"]
        return stress

    def __init__(self):
        # self.BeforeATEFile = BeforeATEFile
        # self.AfterATEFile = AfterATEFile
        # self.adjList = adjList
        pass
        # return self.MakeGraph()

    def MakeGraph(self,BeforeInterventionFolder,AfterInterventionFolder,adjList,col_select =[2,3],function ="L2 Norm"):
        self.BeforeInterventionFile = BeforeInterventionFolder
        self.AfterInterventionFile = AfterInterventionFolder
        self.adjList =adjList
        self.col_select = col_select
        self.function = function
        scalrization_func=Scalarization().getFunction(function)
        self.values=Values(BeforeInterventionFolder, AfterInterventionFolder,adjList,col_select,scalrization_func)
        self.G= nx.Graph()
        self.init_graph_attr1()
        return self

    def init_graph_attr1(self): 
        nodeAttr = {}
        self.init_graph1()
        for i in range(self.values.no_nodes):
            temp = {}
            # temp['OldDeltaVector'] = np.zeros(2)
            temp["DeltaVectornodesStress"] = 0 
            # temp['NewDeltaVector'] = np.zeros(2)
            temp["sdgvec"] = self.values.node_attri_dict[self.values.node_list[i]]
            temp["tempsdgvec"] = self.values.node_attri_dict[self.values.node_list[i]]
            temp["oldsdgvec"] = self.values.node_attri_dict[self.values.node_list[i]]
            temp["nodesStress"] = 0
            temp["meansdg"] = np.mean(self.values.node_attri_dict[self.values.node_list[i]])
            temp["name"] = self.values.node_list[i]
            nodeAttr[i] = temp
        print(nodeAttr)
        nx.set_node_attributes(self.G, nodeAttr)

    def init_graph1(self): #states is a dataframe
        self.G.add_nodes_from([i for i in range(0,self.values.no_nodes)])
        labels = {}
        labels = self.values.node_adj_frame.columns
        print(labels)
        print(self.values.node_adj_frame)
        for i in range(self.values.no_nodes):
            snode=  self.values.node_adj_frame[labels[0]][i]-1
            temp = self.values.node_adj_frame[labels[2]][i]
            if ',' in str(temp):
                sedge_arr=temp.split(',')
                for i in range(0,len(sedge_arr)):
                    self.G.add_edge(snode,int(sedge_arr[i])-1)
                    
            elif math.isnan(temp) :
                print()
            else :
                self.G.add_edge(snode,temp-1)
        return
     
class Values:
    def __init__(self,BeforeFolder, AfterFolder, AdjFile,col_select,sclarisation_func):
        self.BeforeFolder= BeforeFolder
        self.AfterFolder = AfterFolder
        self.AdjFile=AdjFile
        self.col_select=col_select
        self.sclarisation_func=sclarisation_func
        self.node_list=[]
        self.attr_list =[]
        self.node_attri_dict=[]
        self.node_adj_frame = None
        self.no_nodes =None
        self.no_attri = None
        self.populate_after()

    def preprocess(self,Folder): # col_select =[2,3]
        df = pd.DataFrame()
        attribute_dict={}
        for filename in os.listdir(Folder):
            # print(filename.split(" ")[0])
            cntr=0
            self.node_list.append(filename.split(" ")[0])
            tempExcel = pd.read_excel(Folder+"/"+filename)
            if cntr==0:
                for i in self.col_select:
                    attribute_dict[tempExcel.iloc[i][0]]=[]
                self.attr_list=attribute_dict.keys()
                cntr+=1
        self.no_nodes=len(self.node_list)
        self.no_attri=len(self.attr_list)
        for filename in os.listdir(Folder):
            for j in self.col_select: 
                scalarvalue= self.sclarisation_func(float(tempExcel.iloc[j][1]),float(tempExcel.iloc[j][3]),float(tempExcel.iloc[j][4]))
                attribute_dict[tempExcel.iloc[j][0]].append(scalarvalue)
        print(attribute_dict)
        df["Nodes"] = self.node_list
        for attribute in self.attr_list:
            df[attribute] = attribute_dict[attribute]  
        return df

    def populate_after(self):
        #df = pd.read_excel(BeforeATEFile)
        df= self.preprocess(self.AfterFolder)
        df['sdgvec'] = df[self.attr_list].values.tolist()
        self.node_attri_dict = dict(zip(df["Nodes"], df.sdgvec))
        # df2['sdgvec'] = df2[attribute_list].values.tolist()
        self.node_adj_frame=pd.read_excel(self.AdjFile)

def StressModelling(Graph_objOriginal,numRounds,EpsilonStress,SM_function ="gradient_descent"):
        Graph_obj = GraphCreator().MakeGraph(Graph_objOriginal.BeforeInterventionFile,
                                            Graph_objOriginal.AfterInterventionFile,
                                            Graph_objOriginal.adjList,
                                            Graph_objOriginal.col_select,
                                            Graph_objOriginal.function )
        NodesDict = {}
        for i in Graph_obj.values.node_list:
            NodesDict[i] = []
        MeanSDGs = []
        MeanStress = [] 
        Graph_obj.init_graph_attr1()
        print("Number Of Rounds :"+str(numRounds))
        # print("Punjabs SDG 5 after Policy Intervention:",G2.nodes[19]['sdgvec'])
        # PolicyIntervention(G,label,nodeIDs,Policies)
        for i in range(numRounds):
            # print(i)
            temp1 = Graph_obj.getMeanSDGGraph2("sdgvec")
            temp2 = Graph_obj.getGraphStress2("sdgvec")
            #print(" Mean SDG Graph is: ",temp1," Graph Stress is:",temp2)
            MeanSDGs.append(temp1)
            MeanStress.append(temp2)
            for n in Graph_obj.G.nodes(): 
                print(Graph_obj.G.nodes[n]["name"])
                NodesDict[Graph_obj.G.nodes[n]["name"]].append(Graph_obj.G.nodes[n]["sdgvec"])
            if temp2>=EpsilonStress:
            # PolicyIntervention(G,Policies,NodeIDs,numSDGs,label)
                func=StressReduction().getFunction(SM_function)
                # print(func)
                func(Graph_obj.G,"sdgvec" ,"tempsdgvec",Graph_obj.values.no_attri)
            else:
                print(i,"stress less than epsilon")
                break
        print("Till her it cames\n")
        for n in Graph_obj.G.nodes(): 
            NodesDict[Graph_obj.G.nodes[n]["name"]].append(Graph_obj.G.nodes[n]["sdgvec"])
        print("Till here also it cames\n")
        resultObject = ResultObject(NodesDict,MeanSDGs,MeanStress)
        return resultObject,Graph_obj

class ResultObject:
    NodesDict = None
    MeanSDGs = None
    MeanStress = None
    def __init__(self, NodeDict,MeanSDGs,MeanStress):
        self.NodesDict = NodeDict
        self.MeanSDGs = MeanSDGs
        self.MeanStress = MeanStress

    
    
# class Root:
#     def __init__(self):
#         self.ReturnObject=[]
#     def StressModelling(self,Graph_obj,numRounds,EpsilonStress,SM_function ="gradient_descent"):
#         NodesDict = {}
#         for i in Graph_obj.values.node_list:
#             NodesDict[i] = []
#         MeanSDGs = []
#         MeanStress = [] 
#         Graph_obj.init_graph_attr1()
#         print("Number Of Rounds :"+str(numRounds))
#         # print("Punjabs SDG 5 after Policy Intervention:",G2.nodes[19]['sdgvec'])
#         # PolicyIntervention(G,label,nodeIDs,Policies)
#         for i in range(numRounds):
#             # print(i)
#             temp1 = Graph_obj.getMeanSDGGraph2("sdgvec")
#             temp2 = Graph_obj.getGraphStress2("sdgvec")
#             #print(" Mean SDG Graph is: ",temp1," Graph Stress is:",temp2)
#             MeanSDGs.append(temp1)
#             MeanStress.append(temp2)
#             for n in Graph_obj.G.nodes(): 
#                 print(Graph_obj.G.nodes[n]["name"])
#                 NodesDict[Graph_obj.G.nodes[n]["name"]].append(Graph_obj.G.nodes[n]["sdgvec"])
#             if temp2>=EpsilonStress:
#             # PolicyIntervention(G,Policies,NodeIDs,numSDGs,label)
#                 func=StressReduction().getFunction(SM_function)
#                 print(func)
#                 func(Graph_obj.G,"sdgvec" ,"tempsdgvec",Graph_obj.values.no_attri)
#             else:
#                 print(i,"stress less than epsilon")
#                 break
#         print("Till her it cames\n")
#         for n in Graph_obj.G.nodes(): 
#             NodesDict[Graph_obj.G.nodes[n]["name"]].append(Graph_obj.G.nodes[n]["sdgvec"])
#         print("Till here also it cames\n")
#         return NodesDict


class StressReduction:
    def __init__(self) -> None:
        pass

    def Gradient_Descent(self,G,label1,label2,numSDG):
        for n in G.nodes():
            nodeStress = 0
            neigList = list(G.neighbors(n))
            a = np.zeros(numSDG)
            for nei in neigList:
                a = np. add(a,np.array(G.nodes[nei][label1]))
            if len(neigList)!=0:
                a = a/len(neigList)
                G.nodes[n][label2] = np.add(G.nodes[n][label2],np.add(a,-1*np.array(G.nodes[n][label1]))).tolist()
        for n in G.nodes():
            G.nodes[n][label1] = G.nodes[n][label2].copy()
        return 
    
    def getFunction(self,SM_function):
        if SM_function=="gradient_descent":
            return self.Gradient_Descent

def CreateGraph(BeforeInterventionFolder,AfterInterventionFolder,adjList,function):
    g = GraphCreator()
    return g.MakeGraph(BeforeInterventionFolder,AfterInterventionFolder,adjList,function)


# Test CODE
def ATEFunction1(a,b,c):
  return a+b+c
  
Graph_obj1=GraphCreator().MakeGraph(BeforeInterventionFolder=r"C:\Users\sowmi\OneDrive\Desktop\studies\20 credit project\New folder\Package\StressModellingPackageTest\Before",AfterInterventionFolder=r"./After",adjList=r"./Adjacent list ac zones.xlsx",function=ATEFunction1)
# Graph_obj2=GraphCreator().MakeGraph(BeforeInterventionFolder=r"C:\Users\sowmi\OneDrive\Desktop\studies\20 credit project\New folder\Package\StressModellingPackageTest\Before",AfterInterventionFolder=r"./After",adjList=r"./Adjacent list ac zones.xlsx",function ="ATE")
result1,graphUpdated=StressModelling(Graph_obj1,numRounds=10,EpsilonStress=0)
# print(type(graphOrgiginal))
# result3=Root().StressModelling(Graph_obj2,numRounds=10,EpsilonStress=0)
print (result1.NodesDict)
# print("-------------------------------------------------------------------------")
# print (result2)
# print("-------------------------------------------------------------------------")
# print (result3)
# print("-------------------------------------------------------------------------")

# class ATECalculationMethods:


# class VizualizationMethods:


# def StressModelling():




















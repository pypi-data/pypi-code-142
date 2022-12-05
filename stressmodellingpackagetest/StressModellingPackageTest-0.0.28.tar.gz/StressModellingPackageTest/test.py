import ..StressModellingPackageTest as SM

Graph_obj1= SM.GraphCreator().MakeGraph(BeforeInterventionFolder=r"./Before",AfterInterventionFolder=r"./After",adjList=r"./Adjacent list ac zones.xlsx",function="L2 Norm",PreComputed = 1)
# Graph_obj2=GraphCreator().MakeGraph(BeforeInterventionFolder=r"C:\Users\sowmi\OneDrive\Desktop\studies\20 credit project\New folder\Package\StressModellingPackageTest\Before",AfterInterventionFolder=r"./After",adjList=r"./Adjacent list ac zones.xlsx",function ="ATE")
result1,graphUpdated=SM.StressModelling(Graph_obj1,numRounds=10,EpsilonStress=0)
# print(type(graphOrgiginal))
# result3=Root().StressModelling(Graph_obj2,numRounds=10,EpsilonStress=0)
print (result1.NodesDict)
# print("-------------------------------------------------------------------------")
# print (result2)
# print("-------------------------------------------------------------------------")
# print (result3)
# print("-------------------------------------------------------------------------")

# class ATECalculationMethods:
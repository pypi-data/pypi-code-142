def prog1():
    def aStarAlgo(start_node, stop_node):

        open_set = set(start_node)
        closed_set = set()
        g = {}
        parents = {}

        g[start_node] = 0
        parents[start_node] = start_node

        while len(open_set) > 0:
            n = None
            for v in open_set:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v

            if n == stop_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight

                    else:
                        if g[m] > g[n] + weight:
                            g[m] = g[n] + weight
                            parents[m] = n

                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)

            if n == None:
                print('Path does not exist!')
                return None

            if n == stop_node:
                path = []

                while parents[n] != n:
                    path.append(n)
                    n = parents[n]

                path.append(start_node)

                path.reverse()

                print('Path found: {}'.format(path))
                return path

            open_set.remove(n)
            closed_set.add(n)

        print('Path does not exist!')
        return None

    def get_neighbors(v):
        if v in Graph_nodes:
            return Graph_nodes[v]
        else:
            return None

    def heuristic(n):
        H_dist = {
            'A': 10,
            'B': 8,
            'C': 5,
            'D': 7,
            'E': 3,
            'F': 6,
            'G': 5,
            'H': 3,
            'I': 1,
            'J': 0
        }

        return H_dist[n]

    # Describe your graph here
    Graph_nodes = {
        'A': [('B', 6), ('F', 3)],
        'B': [('C', 3), ('D', 2)],
        'C': [('D', 1), ('E', 5)],
        'D': [('C', 1), ('E', 8)],
        'E': [('I', 5), ('J', 5)],
        'F': [('G', 1), ('H', 7)],
        'G': [('I', 3)],
        'H': [('I', 2)],
        'I': [('E', 5), ('J', 3)],

    }
    aStarAlgo('A', 'J')

def prog2():
    class Graph:
        def __init__(self, graph, heuristicNodeList,
                     startNode):
            self.graph = graph
            self.H = heuristicNodeList
            self.start = startNode
            self.parent = {}
            self.status = {}
            self.solutionGraph = {}

        def applyAOStar(self):
            self.aoStar(self.start, False)

        def getNeighbors(self, v):
            return self.graph.get(v, '')

        def getStatus(self, v):
            return self.status.get(v, 0)

        def setStatus(self, v, val):
            self.status[v] = val

        def getHeuristicNodeValue(self, n):
            return self.H.get(n, 0)

        def setHeuristicNodeValue(self, n, value):
            self.H[n] = value

        def printSolution(self):
            print("FOR GRAPH SOLUTION, TRAVERSE THE GRAPH FROM THE START NODE:", self.start)
            print("------------------------------------------------------------")
            print(self.solutionGraph)
            print("------------------------------------------------------------")

        def computeMinimumCostChildNodes(self, v):
            minimumCost = 0
            costToChildNodeListDict = {}
            costToChildNodeListDict[minimumCost] = []
            flag = True
            for nodeInfoTupleList in self.getNeighbors(v):
                cost = 0
                nodeList = []
                for c, weight in nodeInfoTupleList:
                    cost = cost + self.getHeuristicNodeValue(c) + weight
                    nodeList.append(c)
                if flag == True:
                    minimumCost = cost
                    costToChildNodeListDict[minimumCost] = nodeList
                    flag = False
                else:
                    if minimumCost > cost:
                        minimumCost = cost
                        costToChildNodeListDict[minimumCost] = nodeList
            return minimumCost, costToChildNodeListDict[
                minimumCost]

        def aoStar(self, v, backTracking):
            print("HEURISTIC VALUES  :", self.H)
            print("SOLUTION GRAPH    :", self.solutionGraph)
            print("PROCESSING NODE   :", v)
            print("-----------------------------------------------------------------------------------------")

            if self.getStatus(v) >= 0:
                minimumCost, childNodeList = self.computeMinimumCostChildNodes(v)
                self.setHeuristicNodeValue(v, minimumCost)
                self.setStatus(v, len(childNodeList))
                solved = True
                for childNode in childNodeList:
                    self.parent[childNode] = v
                    if self.getStatus(childNode) != -1:
                        solved = solved & False
                if solved == True:
                    self.setStatus(v, -1)
                    self.solutionGraph[
                        v] = childNodeList
                if v != self.start:
                    self.aoStar(self.parent[v],
                                True)
                if backTracking == False:
                    for childNode in childNodeList:
                        self.setStatus(childNode, 0)
                        self.aoStar(childNode,
                                    False)

    h1 = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1, 'T': 3}
    graph1 = {
        'A': [[('B', 1), ('C', 1)], [('D', 1)]],
        'B': [[('G', 1)], [('H', 1)]],
        'C': [[('J', 1)]],
        'D': [[('E', 1), ('F', 1)]],
        'G': [[('I', 1)]]
    }
    G1 = Graph(graph1, h1, 'A')
    G1.applyAOStar()
    G1.printSolution()
    h2 = {'A': 1, 'B': 6, 'C': 12, 'D': 10, 'E': 4, 'F': 4, 'G': 5, 'H': 7}
    graph2 = {
        'A': [[('B', 1), ('C', 1)], [('D', 1)]],
        'B': [[('G', 1)], [('H', 1)]],
        'D': [[('E', 1), ('F', 1)]]
    }
    G2 = Graph(graph2, h2, 'A')
    G2.applyAOStar()
    G2.printSolution()

def prog3():

    # Dataset is required in this
    # import random
    import csv
    def g_0(n):
        return ("?",) * n

    def s_0(n):
        return ('0',) * n

    def more_general(h1, h2):
        more_general_parts = []
        for x, y in zip(h1, h2):
            mg = x == "?" or (x != "0" and (x == y or y == "0"))
            more_general_parts.append(mg)
        return all(more_general_parts)

    l1 = [1, 2, 3]
    l2 = [3, 4, 5]
    list(zip(l1, l2))

    def fulfills(example, hypothesis):
        return more_general(hypothesis, example)

    def min_generalizations(h, x):
        h_new = list(h)
        for i in range(len(h)):
            if not fulfills(x[i:i + 1], h[i:i + 1]):
                h_new[i] = '?' if h[i] != '0' else x[i]
        return [tuple(h_new)]

    min_generalizations(h=('0', '0', 'sunny'),
                        x=('rainy', 'windy', 'cloudy'))

    def min_specializations(h, domains, x):
        results = []
        for i in range(len(h)):
            if h[i] == "?":
                for val in domains[i]:
                    if x[i] != val:
                        h_new = h[:i] + (val,) + h[i + 1:]
                        results.append(h_new)
            elif h[i] != "0":
                h_new = h[:i] + ('0',) + h[i + 1:]
                results.append(h_new)
        return results

    min_specializations(h=('?', 'x',),
                        domains=[['a', 'b', 'c'], ['x', 'y']],
                        x=('b', 'x'))
    with open('wsce.csv') as csvFile:
        examples = [tuple(line) for line in csv.reader(csvFile)]
    examples

    def get_domains(examples):
        d = [set() for i in examples[0]]
        for x in examples:
            for i, xi in enumerate(x):
                d[i].add(xi)
        return [list(sorted(x)) for x in d]

    get_domains(examples)

    def candidate_elimination(examples):
        domains = get_domains(examples)[:-1]
        G = set([g_0(len(domains))])
        S = set([s_0(len(domains))])
        i = 0
        print("\n G[{0}]:".format(i), G)
        print("\n S[{0}]:".format(i), S)
        for xcx in examples:
            i = i + 1
            x, cx = xcx[:-1], xcx[-1]
            if cx == 'Y':
                G = {g for g in G if fulfills(x, g)}
                S = generalize_S(x, G, S)
            else:
                S = {s for s in S if not fulfills(x, s)}
                G = specialize_G(x, domains, G, S)
            print("\n G[{0}]:".format(i), G)
            print("\n S[{0}]:".format(i), S)
        return

    def generalize_S(x, G, S):
        S_prev = list(S)
        for s in S_prev:
            if s not in S:
                continue
            if not fulfills(x, s):
                S.remove(s)
                Splus = min_generalizations(s, x)
                S.update([h for h in Splus if any([more_general(g, h)
                                                   for g in G])])
                S.difference_update([h for h in S if
                                     any([more_general(h, h1)
                                          for h1 in S if h != h1])])
        return S

    def specialize_G(x, domains, G, S):
        G_prev = list(G)
        for g in G_prev:
            if g not in G:
                continue
            if fulfills(x, g):
                G.remove(g)
                Gminus = min_specializations(g, domains, x)
                G.update([h for h in Gminus if any([more_general(h, s) for s in S])])
                G.difference_update([h for h in G if any([more_general(g1, h) for g1 in G if h != g1])])
        return G

    candidate_elimination(examples)

def prog4():
    # This has 2 files, make a main.py and data_loader.py and then copy codes in respective files.

    # main.py
    import numpy as np
    import math
    from data_loader import read_data

    class Node:
        def __init__(self, attribute):
            self.attribute = attribute
            self.children = []
            self.answer = ""

        def str(self):
            return self.attribute

    def subtables(data, col, delete):
        dict = {}
        items = np.unique(data[:, col])
        count = np.zeros((items.shape[0], 1), dtype=np.int32)
        for x in range(items.shape[0]):
            for y in range(data.shape[0]):
                if data[y, col] == items[x]:
                    count[x] += 1
        for x in range(items.shape[0]):
            dict[items[x]] = np.empty((int(count[x]), data.shape[1]), dtype="|S32")
            pos = 0
            for y in range(data.shape[0]):
                if data[y, col] == items[x]:
                    dict[items[x]][pos] = data[y]
                    pos += 1
            if delete:
                dict[items[x]] = np.delete(dict[items[x]], col, 1)
        return items, dict

    def entropy(S):
        items = np.unique(S)
        if items.size == 1:
            return 0
        counts = np.zeros((items.shape[0], 1))
        sums = 0
        for x in range(items.shape[0]):
            counts[x] = sum(S == items[x]) / (S.size * 1.0)
        for count in counts:
            sums += -1 * count * math.log(count, 2)
        return sums

    def gain_ratio(data, col):
        items, dict = subtables(data, col, delete=False)
        total_size = data.shape[0]
        entropies = np.zeros((items.shape[0], 1))
        intrinsic = np.zeros((items.shape[0], 1))
        for x in range(items.shape[0]):
            ratio = dict[items[x]].shape[0] / (total_size * 1.0)
            entropies[x] = ratio * entropy(dict[items[x]][:, -1])
            intrinsic[x] = ratio * math.log(ratio, 2)
        total_entropy = entropy(data[:, -1])
        iv = -1 * sum(intrinsic)
        for x in range(entropies.shape[0]):
            total_entropy -= entropies[x]
        return total_entropy / iv

    def create_node(data, metadata):
        if (np.unique(data[:, -1])).shape[0] == 1:
            node = Node(" ")
            node.answer = np.unique(data[:, -1])[0]
            return node
        gains = np.zeros((data.shape[1] - 1, 1))
        for col in range(data.shape[1] - 1):
            gains[col] = gain_ratio(data, col)
        split = np.argmax(gains)
        node = Node(metadata[split])
        metadata = np.delete(metadata, split, 0)
        items, dict = subtables(data, split, delete=True)
        for x in range(items.shape[0]):
            child = create_node(dict[items[x]], metadata)
            node.children.append((items[x], child))
        return node

    def empty(size):
        s = ""
        for x in range(size):
            s += " "
        return s

    def print_tree(node, level):
        if node.answer != "":
            print(empty(level), node.answer)
            return
        print(empty(level), node.attribute)
        for value, n in node.children:
            print(empty(level + 1), value)
            print_tree(n, level + 2)

    metadata, traindata = read_data("tennis.csv")
    data = np.array(traindata)
    node = create_node(data, metadata)
    print_tree(node, 0)

    import csv

    def read_data(filename):
        with open(filename, 'r') as csvfile:
            datareader = csv.reader(csvfile, delimiter=',')
            headers = next(datareader)
            metadata = []
            traindata = []
            for name in headers:
                metadata.append(name)
            for row in datareader:
                traindata.append(row)
        return (metadata, traindata)

    # data_loader.py
    import csv
    def read_data(filename):
        with open(filename, 'r') as csvfile:
            datareader = csv.reader(csvfile, delimiter=',')
            headers = next(datareader)
            metadata = []
            traindata = []
            for name in headers:
                metadata.append(name)
            for row in datareader:
                traindata.append(row)
        return (metadata, traindata)


def prog5():
    import numpy as np
    X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
    y = np.array(([92], [86], [89]), dtype=float)
    X = X/np.amax(X,axis=0)
    y = y/100

    def sigmoid (x):
        return 1/(1 + np.exp(-x))

    def derivatives_sigmoid(x):
        return x * (1 - x)

    epoch=7000
    lr=0.1
    inputlayer_neurons = 2
    hiddenlayer_neurons = 3
    output_neurons = 1
    wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
    bh=np.random.uniform(size=(1,hiddenlayer_neurons))
    wout=np.random.uniform(size=(hiddenlayer_neurons,output_neurons))
    bout=np.random.uniform(size=(1,output_neurons))
    for i in range(epoch):
        hinp1=np.dot(X,wh)
        hinp=hinp1 + bh
        hlayer_act =sigmoid(hinp)
        outinp1=np.dot(hlayer_act,wout)
        outinp= outinp1+ bout
        output = sigmoid(outinp)
        EO = y-output
        outgrad = derivatives_sigmoid(output)
        d_output = EO* outgrad
        EH = d_output.dot(wout.T)
        hiddengrad = derivatives_sigmoid(hlayer_act)
        d_hiddenlayer = EH * hiddengrad
        wout += hlayer_act.T.dot(d_output) *lr
        bout += np.sum(d_output, axis=0,keepdims=True) *lr
        wh += X.T.dot(d_hiddenlayer) *lr
        bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) *lr
    print("Input: \n" + str(X))
    print("Actual Output: \n" + str(y))
    print("Predicted Output: \n" ,output)


def prog6():
    #This requires dataset

    import csv
    import random
    import math
    def loadcsv(filename):
        lines = csv.reader(open(filename, "r"))
        dataset = list(lines)
        for i in range(len(dataset)):
            dataset[i] = [float(x) for x in dataset[i]]
        return dataset

    def splitDataset(dataset, splitRatio):
        trainSize = int(len(dataset) * splitRatio)
        trainSet = []
        copy = list(dataset)
        while len(trainSet) < trainSize:
            index = random.randrange(len(copy))
            trainSet.append(copy.pop(index))
        return [trainSet, copy]

    def separateByClass(dataset):
        separated = {}
        for i in range(len(dataset)):
            vector = dataset[i]
            if (vector[-1] not in separated):
                separated[vector[-1]] = []
            separated[vector[-1]].append(vector)
        return separated

    def mean(numbers):
        return sum(numbers) / float(len(numbers))

    def stdev(numbers):
        avg = mean(numbers)
        variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
        return math.sqrt(variance)

    def summarize(dataset):
        summaries = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
        del summaries[-1]
        return summaries

    def summarizeByClass(dataset):
        separated = separateByClass(dataset)
        summaries = {}
        for classValue, instances in separated.items():
            summaries[classValue] = summarize(instances)
        return summaries

    def calculateProbability(x, mean, stdev):
        exponent = math.exp(-(math.pow(x - mean, 2) / (2 * math.pow(stdev, 2))))
        return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent

    def calculateClassProbabilities(summaries, inputVector):
        probabilities = {}
        for classValue, classSummaries in summaries.items():
            probabilities[classValue] = 1
            for i in range(len(classSummaries)):
                mean, stdev = classSummaries[i]
                x = inputVector[i]
                probabilities[classValue] *= calculateProbability(x, mean, stdev)
        return probabilities

    def predict(summaries, inputVector):
        probabilities = calculateClassProbabilities(summaries, inputVector)
        bestLabel, bestProb = None, -1
        for classValue, probability in probabilities.items():
            if bestLabel is None or probability > bestProb:
                bestProb = probability
                bestLabel = classValue
        return bestLabel

    def getPredictions(summaries, testSet):
        predictions = []
        for i in range(len(testSet)):
            result = predict(summaries, testSet[i])
            predictions.append(result)
        return predictions

    def getAccuracy(testSet, predictions):
        correct = 0
        for i in range(len(testSet)):
            if testSet[i][-1] == predictions[i]:
                correct += 1
        return (correct / float(len(testSet))) * 100.0

    def main():
        filename = 'pima-indians-diabetes.csv'
        splitRatio = 0.67
        dataset = loadcsv(filename)
        # print("\n The Data Set :\n",dataset)
        print("\n The length of the Data Set : ", len(dataset))
        print("\n The Data Set Splitting into Training and Testing \n")
        trainingSet, testSet = splitDataset(dataset, splitRatio)
        print('\n Number of Rows in Training Set:{0} rows'.format(len(trainingSet)))
        print('\n Number of Rows in Testing Set:{0} rows'.format(len(testSet)))
        print("\n First Five Rows of Training Set:\n")
        for i in range(0, 5):
            print(trainingSet[i], "\n")
        print("\n First Five Rows of Testing Set:\n")
        for i in range(0, 5):
            print(testSet[i], "\n")
        summaries = summarizeByClass(trainingSet)
        print("\n Model Summaries:\n", summaries)
        predictions = getPredictions(summaries, testSet)
        print("\nPredictions:\n", predictions)
        accuracy = getAccuracy(testSet, predictions)
        print('\n Accuracy: {0}%'.format(accuracy))

    main()

def prog7():

    import matplotlib.pyplot as plt
    from sklearn import datasets
    from sklearn.cluster import KMeans
    import pandas as pd
    import numpy as np
    iris = datasets.load_iris()
    X = pd.DataFrame(iris.data)
    X.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
    y = pd.DataFrame(iris.target)
    y.columns = ['Targets']
    model = KMeans(n_clusters=3)
    model.fit(X)
    plt.figure(figsize=(14, 14))
    colormap = np.array(['red', 'lime', 'black'])
    plt.subplot(2, 2, 1)
    plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[y.Targets], s=40)
    plt.title('Real Clusters')
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')
    plt.subplot(2, 2, 2)
    plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[model.labels_], s=40)
    plt.title('K-Means Clustering')
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')
    from sklearn import preprocessing
    scaler = preprocessing.StandardScaler()
    scaler.fit(X)
    xsa = scaler.transform(X)
    xs = pd.DataFrame(xsa, columns=X.columns)
    from sklearn.mixture import GaussianMixture
    gmm = GaussianMixture(n_components=3)
    gmm.fit(xs)
    gmm_y = gmm.predict(xs)
    plt.subplot(2, 2, 3)
    plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[gmm_y], s=40)
    plt.title('GMM Clustering')
    plt.xlabel('Petal Length')
    plt.ylabel('Petal Width')
    print(
        'Observation: The GMM using EM algorithm based clustering matched the true labels more closely than the Kmeans.')


def prog8():
    from sklearn.model_selection import train_test_split
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import datasets
    iris = datasets.load_iris()
    print("Iris Data set loaded...")
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.1)
    print("Dataset is split into training and testing...")
    print("Size of training data and its label", x_train.shape, y_train.shape)
    print("Size of testing data and its label", x_test.shape, y_test.shape)
    for i in range(len(iris.target_names)):
        print("Label", i, "-", str(iris.target_names[i]))
    classifier = KNeighborsClassifier(n_neighbors=1)
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    print("Results of Classification using K-nn with K=1 ")
    for r in range(0, len(x_test)):
        print(" Sample:", str(x_test[r]), " Actual-label:", str(y_test[r]), " Predicted-label:", str(y_pred[r]))
    print("Classification Accuracy :", classifier.score(x_test, y_test));
    from sklearn.metrics import classification_report, confusion_matrix
    print('Confusion Matrix')
    print(confusion_matrix(y_test, y_pred))
    print('Accuracy Metrics')
    print(classification_report(y_test, y_pred))

def prog91():
    #There are 2 programs in this, 91 requires dataset and is as per our lab manual
    #92 doesn't requires dataset and is given by Priyanka mam

    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    def kernel(point, xmat, k):
        m, n = np.shape(xmat)
        weights = np.mat(np.eye((m)))  # eye - identity matrix
        for j in range(m):
            diff = point - X[j]
            weights[j, j] = np.exp(diff * diff.T / (-2.0 * k ** 2))
        return weights

    def localWeight(point, xmat, ymat, k):
        wei = kernel(point, xmat, k)
        W = (X.T * (wei * X)).I * (X.T * (wei * ymat.T))
        return W

    def localWeightRegression(xmat, ymat, k):
        m, n = np.shape(xmat)
        ypred = np.zeros(m)
        for i in range(m):
            ypred[i] = xmat[i] * localWeight(xmat[i], xmat, ymat, k)
        return ypred

    def graphPlot(X, ypred):
        sortindex = X[:, 1].argsort(0)
        xsort = X[sortindex][:, 0]
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.scatter(bill, tip, color='green')
        ax.plot(xsort[:, 1], ypred[sortindex], color='red', linewidth=5)
        plt.xlabel('Total Bill')
        plt.ylabel('Tip')
        plt.show()

    data = pd.read_csv('data10_tips.csv')
    bill = np.array(data.total_bill)
    tip = np.array(data.tip)
    mbill = np.mat(bill)
    mtip = np.mat(tip)
    m = np.shape(mbill)[1]
    one = np.mat(np.ones(m))
    X = np.hstack((one.T, mbill.T))
    ypred = localWeightRegression(X, mtip, 3)
    graphPlot(X, ypred)

def prog92():
    import numpy as np
    import matplotlib.pyplot as plt

    def local_regression(x0, X, Y, tau):
        x0 = [1, x0]
        X = [[1, i] for i in X]
        X = np.asarray(X)
        xw = (X.T) * np.exp(np.sum((X - x0) ** 2, axis=1) / (-2 * tau))
        beta = np.linalg.pinv(xw @ X) @ xw @ Y @ x0
        return beta

    def draw(tau):
        prediction = [local_regression(x0, X, Y, tau) for x0 in domain]
        plt.plot(X, Y, 'o', color='black')
        plt.plot(domain, prediction, color='red')
        plt.show()

    X = np.linspace(-3, 3, num=1000)
    domain = X
    Y = np.log(np.abs(X ** 2 - 1) + .5)

    draw(10)
    draw(0.1)
    draw(0.01)
    draw(0.001)










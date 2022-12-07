import tellurium as te
import matplotlib.pyplot as plt

def reactionAntimony(dict, currentK):
    f = open("webapp/static/antimony1.txt", 'a')

    reactantSpecies = dict['Reactants']
    FixedReactants = dict['FixedReactants']
    newStr = ''
    for species in reactantSpecies:
        for fixedSpecies in FixedReactants:
            if species == fixedSpecies:
                species = '$' + species
                newStr = newStr + species + '+'
            else:
                newStr = newStr + species + '+'
    newStr = newStr[:-1] + '->'

    productSpecies = dict['Products']
    FixedProducts = dict['FixedProducts']
    for species in productSpecies:
        for fixedSpecies in FixedProducts:
            if species == fixedSpecies:
                species = '$' + fixedSpecies
                newStr = newStr + species + '+'
            else:
                newStr = newStr + species + '+'

    rxnVals = dict['RxnConstant']
    kVal = len(rxnVals)
    kList = []

    for i in range(kVal):
        numStr = str(i + currentK)
        kList.append('k' + numStr)
        numConstants = i

    currentK = currentK + kVal
    newStr = newStr[:-1] + ' ; ' + kList[0] + '*'

    for species in reactantSpecies:
        newStr = newStr + species + '*'
    newStr = newStr[:-1]

    # print this line to the antimony file
    f.write('\n')
    f.write(newStr)

    if dict['Reversibility'] == True:
        secStr = ''
        for species in productSpecies:
            for fixedSpecies in FixedReactants:
                if species == fixedSpecies:
                    species = '$' + fixedSpecies
                    secStr = secStr + species + '+'
                else:
                    secStr = secStr + species + '+'
        secStr = secStr[:-1] + '->'
        for species in reactantSpecies:
            for fixedSpecies in FixedReactants:
                if species == fixedSpecies:
                    species = '$' + species
                    secStr = secStr + species + '+'
                else:
                    secStr = secStr + species + '+'

        secStr = secStr[:-1] + ' ; ' + kList[1] + '*'

        for species in productSpecies:
            secStr = secStr + species + '*'
        secStr = secStr[:-1]

        # print secStr to antimony file within the if statement
        f.write('\n')
        f.write(secStr)
    f.close()
    return currentK, kList

def conditionsAntimony(dict,  kList):
    f = open('webapp/static/antimony2.txt','a')
    reactantIC = dict['ReactantIC']
    reactantSpecies = dict['Reactants']
    str1 = ''
    count = 0
    for species in reactantSpecies:
        str1 += species + '=' + reactantIC[count] + ';'
        count += 1
    str1 = str1[:-1]
    f.write('\n')
    f.write(str1)
    # print to IC file

    productIC = dict['ProductIC']
    productSpecies = dict['Products']
    str2 = ''
    count = 0
    for species in productSpecies:
        str2 += species + '=' + productIC[count] + ';'
        count += 1
    str2 = str2[:-1]
    # print to IC file
    f.write('\n')
    f.write(str2)

    rxnConstants = dict['RxnConstant']
    str3 = ''
    count = 0
    for var in kList:
        str3 += var + '=' + rxnConstants[count] + ';'
        count += 1
    str3 = str3[:-1]
    f.write('\n')
    f.write(str3)
    f.close()

    return str1, str2, str3

def resetFiles():
    with open('webapp/static/antimony1.txt', 'r+') as file:
        file.truncate(0)
        file.close()
    with open('webapp/static/antimony2.txt', 'r+') as file:
        file.truncate(0)
        file.close() 

"""
Takes in given values as strings or booleans from the website program and saves
them to a dictionary
Inputs:
    - reactants: (Str) comma separated string of a list of letters that represent reactants
    - fixed_reactants: (Str) comma separated string of the reactants that are fixed values
    - reactantIC: (Str) comma separated string of numbers that are the IC of the reactants
    - products: (Str) comma separated string of a list of letters that represent products
    - fixed_products: (Str) comma separated string of the products that are fixed values
    - productIC: (Str) comma separated string of numbers that are the IC of the products
    - reactionConstant: (Str) comma separates string of numbers that are the k values of reaction
    - reversibility: (boolean) true if the reaction is reversible
Outputs:
    - dict: a dictionary that contains the values as the inputs connected to a name
"""
def init(reactants, fixed_reactants, reactantIC, products, fixed_products, productIC, reactionConstant, reversibility):
    dict = {}

    dict['Reactants'] = reactants.split(',')

    dict['FixedReactants'] = fixed_reactants.split(',')

    dict['ReactantIC'] = reactantIC.split(',')

    dict['Products'] = products.split(',')

    dict['FixedProducts'] = fixed_products.split(',')

    dict['ProductIC'] = productIC.split(',')

    dict['RxnConstant'] = reactionConstant.split(',')

    dict['Reversibility'] = reversibility

    return dict

def runSim():
    file1 = open('webapp/static/antimony1.txt','a')
    file2 = open('webapp/static/antimony2.txt','r')

    for line in file2:
        file1.write(line)
        print(line)
    file1.close()
    file2.close()

    loadModel()

def loadModel():
    r = te.loadAntimonyModel('webapp/static/antimony1.txt')
    result = r.simulate()
    r.plot()
    plt.savefig("webapp/static/output.jpg")

def loadSBML(url):
    r = te.loadSBMLModel(url)
    result = r.simulate()
    r.plot()
    plt.savefig("webapp/static/output.jpg")
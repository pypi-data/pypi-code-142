def printer():
    file="""
    
        #sublist check:
        
        l1=[1,2,3,4,5]
        l2=[1,2,3]
        l=len(l2)
        count=0
        for i in l1:
            for j in l2:
                if i==j:
                    count+=1
        if count==l:
            print("Sublist found")
        else:
            print("Sublist not found")
        
        #dictionary values:
        
        marks=[{
            'name':"viswa","m1":33,'m2':99
        },{"name":"divi","m1":99,'m2':88}]
        for mark in marks:
            m1=mark.pop('m1');
            m2=mark.pop('m2')
            mark['avg']=(m1+m2)/2
        print(marks)
        
        #slicing tuple:
        
        a=(1,2,3,3,5)
        print(a[:])
        b=tuple("Welcome to MCA")
        print(b[::-1])
        
        #concept of array:
        
        import numpy as np
        mat1=np.array([[1,2,3],[1,2,3]])
        mat2=np.array([[1,2,3],[1,2,3]])
        print(np.multiply(mat1,mat2))
        print(np.divide(mat1,mat2))
        
        #powers pandas:
        
        import pandas as pd
        m={"values":[1,2,3,4,5,6,76,78,89,90]}
        df=pd.DataFrame(m)
        df['sq']=df["values"]**2
        print(df)
        
        #check whether a string is a pangram or not:
        
        text=input().lower()
        print(text)
        l=list(set(text))
        if " " in l:
            l.remove(" ")
        if len(l)==26:
            print("pangaram")
        else:
            print("not pangaram")
        
            ''' The quick  brown fox jumps over the lazy dog'''
        
        #K- fold Cross validation Algorithm:
        
        from numpy import array
        from sklearn.model_selection import KFold
        data = array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6,0.7])
        kfold = KFold(3)
        
        for train, test in kfold.split(data):
            print('train: %s, test: %s' % (data[train], data[test]))
        
        #Program to read each row from a given csv file and print a list of Strings:
        
        import csv
        col_names=['Name','Age'];
        data=[["Boopathy",'90'],["Ganesh",'100']]
        file="rec.csv"
        with open(file,'w') as csvfile:
            csvwriter=csv.writer(csvfile);
            csvwriter.writerow(col_names)
            csvwriter.writerows(data)
        
        with open('rec.csv','r') as csvfile:
            rows=csv.reader(csvfile)
            for row in rows:
                print(row)
        
        #K- means Algorithm:
        
        import matplotlib.pyplot as plt
        from sklearn.cluster import KMeans
        import sys
        
        x=[4,5,10,4,3,22,2,84]
        y=[21,19,24,16,25,24,22,21]
        plt.scatter(x,y)
        plt.show()
        d=list(zip(x,y))
        kmeans = KMeans(n_clusters=2)
        kmeans.fit(d)
        
        plt.scatter(x,y,c=kmeans.labels_)
        plt.show()
        plt.savefig(sys.stdout.buffer)
        sys.stdout.flush()
        
        #Naïve Bayes Algorithm:
        
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.naive_bayes import GaussianNB
        from sklearn.metrics import accuracy_score
        
        
        df = pd.read_csv("dataset.csv")
        x = df.drop("diabetes",axis=1)
        y = df["diabetes"]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
        model = GaussianNB()
        model.fit(x_train,y_train)
        y_pred=model.predict(x_test)
        accuracy=accuracy_score(y_test,y_pred)*100
        
        print(accuracy)
        
        #Logistic Regression using Python(Scikit –Learn):
        
        import matplotlib.pyplot as plt
        import pandas as pd
        from sklearn.linear_model import LogisticRegression
        
        data = pd.read_csv('irisdata.csv')
        x = data[['length', 'width']]
        y = data['Type']
        model = LogisticRegression(solver='liblinear', random_state=0)
        model.fit(x,y)
        z=model.predict(x)
        print(z)
        plt.plot(z)
        plt.show()
        
        #Stacked Generalization (Stacking) :
        
        import sklearn.datasets as sd
        import sklearn.model_selection as al
        import sklearn.ensemble as se
        import sklearn.linear_model as sl
        import sklearn.svm as sv
        import time
        X, Y = sd.load_diabetes(return_X_y=True)
        X_train, X_test, Y_train, Y_test = al.train_test_split(X,Y,random_state=42)
        stacked = se.StackingRegressor( estimators =[('SVR', sv.SVR()),('Liner',sl.LinearRegression())])
        st = time.time()
        stacked.fit(X_train, Y_train)
        et = time.time()
        print("Coefficient of determination: {}".format(stacked.score(X_test, Y_test)))
        print("Computation Time: {}".format(et - st))
        
        
        #Support Vector Machine :
        
        import matplotlib.pyplot as plt
        import pandas as pd
        import numpy as np
        from sklearn import svm
        
        
        data = pd.read_csv('irisdata.csv')
        x = data['length']
        y = data['width']
        tr_x = np.vstack((x, y)).T
        tr_y = data['Type']
        clf = svm.SVC(kernel='linear', C=1.0)
        clf.fit(tr_x,tr_y)
        w =clf.coef_[0]
        a = -w[0] /w[1]
        xx = np.linspace(0, 13)
        yy = a* xx -clf.intercept_[0] / w[1]
        plt.plot(xx,yy,'k-')
        plt.scatter(tr_x[:,0],tr_x[:,1],c=tr_y)
        plt.show()
        
        '''irisdata.csv:
        
        length,width,Type
        5.1,3.5,0
        4.9,3,0
        4.7,3.2,0
        4.6,3.1,0
        5,3.6,0
        5.4,3.9,0
        4.6,3.4,0
        5,3.4,0
        4.4,2.9,0
        4.9,3.1,0
        5.4,3.7,0
        4.8,3.4,0
        4.8,3,0
        4.3,3,0
        5.8,4,0
        5.7,4.4,0
        5.4,3.9,0
        5.1,3.5,0
        5.7,3.8,0
        5.1,3.8,0
        5.4,3.4,0
        5.1,3.7,0
        4.6,3.6,0
        5.1,3.3,0
        4.8,3.4,0
        5,3,0
        5,3.4,0
        5.2,3.5,0
        5.2,3.4,0
        4.7,3.2,0
        4.8,3.1,0
        5.4,3.4,0
        5.2,4.1,0
        5.5,4.2,0
        4.9,3.1,0
        5,3.2,0
        5.5,3.5,0
        4.9,3.1,0
        4.4,3,0
        5.1,3.4,0
        5,3.5,0
        4.5,2.3,0
        4.4,3.2,0
        5,3.5,0
        5.1,3.8,0
        4.8,3,0
        5.1,3.8,0
        4.6,3.2,0
        5.3,3.7,0
        5,3.3,0
        7,3.2,1
        6.4,3.2,1
        6.9,3.1,1
        5.5,2.3,1
        6.5,2.8,1
        5.7,2.8,1
        6.3,3.3,1
        4.9,2.4,1
        6.6,2.9,1
        5.2,2.7,1
        5,2,1
        5.9,3,1
        6,2.2,1
        6.1,2.9,1
        5.6,2.9,1
        6.7,3.1,1
        5.6,3,1
        5.8,2.7,1
        6.2,2.2,1
        5.6,2.5,1
        5.9,3.2,1
        6.1,2.8,1
        6.3,2.5,1
        6.1,2.8,1
        6.4,2.9,1
        6.6,3,1
        6.8,2.8,1
        6.7,3,1
        6,2.9,1
        5.7,2.6,1
        5.5,2.4,1
        5.5,2.4,1
        5.8,2.7,1
        6,2.7,1
        5.4,3,1
        6,3.4,1
        6.7,3.1,1
        6.3,2.3,1
        5.6,3,1
        5.5,2.5,1
        5.5,2.6,1
        6.1,3,1
        5.8,2.6,1
        5,2.3,1
        5.6,2.7,1
        5.7,3,1
        5.7,2.9,1
        6.2,2.9,1
        5.1,2.5,1
        5.7,2.8,1'''
            """
    print(file)


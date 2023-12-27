from sklearn.datasets import load_iris 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt 
iris_dataset=load_iris() 
X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], 
iris_dataset ["target"], random_state=0) 
kn = KNeighborsClassifier() 
kn.fit(X_train, y_train) 
prediction = kn.predict(X_test) 
print("ACCURACY:"+ str(kn.score(X_test, y_test))) 
plt.plot(X_test,y_test,'ro') 
plt.plot(X_test,prediction,'b+')

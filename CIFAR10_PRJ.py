import cifar10
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import ensemble
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

"""_________________________________________________________________________"""

cifar10.data_path = "C:\\Users\\prankhur\\OneDrive - Qualcomm\\Desktop\Python codes\\Cifar10"

cifar10.maybe_download_and_extract()


class_names = cifar10.load_class_names()

images_train, cls_train, labels_train = cifar10.load_training_data()
images_test, cls_test, labels_test = cifar10.load_test_data()

fig=plt.figure(figsize=(8,8))
for i in range(64):
    ax=fig.add_subplot(8,8,i+1)
    ax.imshow(images_train[i],cmap=plt.cm.bone)
plt.show()

"""__________________________________________________________________________"""


data_train = images_train.reshape(50000,3072)
data_test = images_test.reshape(10000,3072)    #Flattening out the images from row,col,RGB to one long array

pca = PCA()
pca.fit(data_train)

k=0
total=sum(pca.explained_variance_)
currentSum=0
while currentSum/total<0.99:
    currentSum+=pca.explained_variance_[k]
    k=k+1

pca_t = PCA(n_components=k,whiten=True) #Whiten is used to transform the entire data such that the variance is 1
x_transform = pca_t.fit_transform(data_train)

x_approx = pca_t.inverse_transform(x_transform)
x_approx_rs = x_approx.reshape(50000,32,32,3)

fig = plt.figure(figsize=(8,8))
for i in range(64):
    ax = fig.add_subplot(8,8,i+1)
    ax.imshow(x_approx_rs[i])
  
x_train_pca = x_transform
x_test_pca = pca_t.transform(data_test)

"""_____________________________________________________________________________"""


clf1=RandomForestClassifier(n_estimators=429, n_jobs=-1, max_depth=2000, max_leaf_nodes=2350) # n_jobs = -1 means use all CPUs
clf2=LogisticRegression(n_jobs=-1, multi_class="auto")
clf3=KNeighborsClassifier(n_jobs=-1)

clf1.fit(x_train_pca, cls_train)
clf2.fit(x_train_pca, cls_train)
clf3.fit(x_train_pca, cls_train)



y_pred2 = [class_names[i] for i in y_pred]
y_pred2 = pd.DataFrame(y_pred2)
y_pred2.to_csv('results_CIFAR4.csv',index_label=False,index=False,header=False)
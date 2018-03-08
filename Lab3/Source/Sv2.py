from sklearn import svm
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

cancerdataset = datasets.load_breast_cancer()
a = cancerdataset.data
b = cancerdataset.target
a_train,a_test,b_train,b_test=train_test_split(a,b,test_size=0.2)

#Linear Kernel
linear_svc = svm.SVC(kernel='linear')
b_predic = linear_svc.fit(a_train,b_train).predict(a_test)
print("Data and the target values for linear kernel score is:")
print(linear_svc.score(a,b))
print("Data and the target values for linear kernel accuracy score :")
print(metrics.accuracy_score(b_test,b_predic))

#Rbf kernel
rbf_svc = svm.SVC(kernel='rbf')
b_predic = rbf_svc.fit(a_train,b_train).predict(a_test)
print("Data and the target values for Rbf kernel score is:")
print(rbf_svc.score(a,b))
print("Data and the target values for rbf kernel accuracy score :")
print(metrics.accuracy_score(b_test,b_predic))
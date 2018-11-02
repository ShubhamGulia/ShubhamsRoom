from sklearn import tree
from sklearn import ensemble
#from sklearn import linear_model
# can be  (#import sklearn.tree)

# cannot sklearn does not automatically import its subpackages. If you only imported via: import sklearn, then it wont work. Import with import sklearn.cross_validation instead.
X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],[181,85,43]]

Y= ["Male","Female","Female","Female","Male","Male","Male","Female","Male","Female","Male"]


clf1= tree.DecisionTreeClassifier()

clf1=clf1.fit(X,Y)

prediction1 = clf1.predict([[190,70,43]])

print("Decision Tree Classifier Model ")
print(prediction1)
print("\n")


# Out of bag estimate is in ensemble subpackage of sklearn package

clf2= ensemble.GradientBoostingClassifier()

clf2=clf2.fit(X,Y)

prediction2 = clf2.predict([[190,70,43]])

print("Gradient Boosting Classifier Model ")
print(prediction2)
print("\n")

clf3 = ensemble.RandomForestClassifier()

clf3 = clf3.fit(X,Y)

prediction3 = clf3.predict([[190,70,43]])

print("Random Forest Classifier ")
print(prediction3)


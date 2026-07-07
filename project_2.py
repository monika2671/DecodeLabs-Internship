from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report
iris=load_iris()
scaler=StandardScaler()
scaled_data=scaler.fit_transform(iris.data)
print("First Scaled sample:",scaled_data[0])
x_train, x_test, y_train, y_test = train_test_split(scaled_data, iris.target, test_size=0.2, random_state=42)
print("Training set shape:",x_train.shape)
print("Testing set shape:",x_test.shape)
model= KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)
predictions=model.predict(x_test)
print("Predictions:",predictions)
print("Actual values:",y_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test,predictions))
print("Classification Report:")
print(classification_report(y_test,predictions))

"""print(iris.feature_names)
print(iris.target_names)
print(iris.data.shape)
print(iris.data[0])
print(iris.target[0])
print(iris.DESCR)
print(iris.data[0].shape)
system.out.printl(x)
int y:
y=20;
declaration
initialization
public static void main(String[]args)
public class variablesabasic
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Charger les données
file_path = './dragon_ball_z.csv'
data = pd.read_csv(file_path)

label_encoders = {}
for column in data.columns:
    if data[column].dtype == 'object':
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le


X = data[["Race", "Power Level", "Special Attack", "Melee Combat", "Ki Blast", "Speed"]]
y = data["Transformation"]

tree_clf = DecisionTreeClassifier(random_state=42)
tree_clf.fit(X, y)


plt.figure(figsize=(15, 10))
plot_tree(tree_clf, feature_names=X.columns, class_names=label_encoders["Transformation"].classes_, filled=True, rounded=True)
plt.show()

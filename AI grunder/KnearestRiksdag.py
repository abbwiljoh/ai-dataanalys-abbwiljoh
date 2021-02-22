import numpy as np
import pandas as pd
from sklearn import preprocessing, neighbors, model_selection

df = pd.read_csv('votering-201920.csv')
df.drop(['punkt'], 1, inplace=True)

df = df[['rost', 'parti', 'fodd', 'kon', 'intressent_id']]
inputLabels = ['kvinna', 'man']
encoder = preprocessing.LabelEncoder()
encoder.fit(inputLabels)
df['kon'] = encoder.transform(df['kon'])  # kvinna ---> 0 man ---> 1

inputLabels = ['C', 'KD', 'M', 'L', 'MP', 'V', 'S', 'SD', '-']
encoder.fit(inputLabels)
# - ---> 0 C ---> 1 KD ---> 2 L ---> 3 M ---> 4 MP ---> 5 S ---> 6 SD ---> 7 V ---> 8
df['parti'] = encoder.transform(df['parti'])

inputLabels = ['Ja', 'Nej', 'Frånvarande', 'Avstår']
# Avstår ---> 0 Frånvarande ---> 1 Ja ---> 2 Nej ---> 3
encoder.fit(inputLabels)
df['rost'] = encoder.transform(df['rost'])

df.replace('?', '-9999', inplace=True)

X = np.array(df.drop(['rost'], 1))
Y = np.array(df['rost'])

xTrain, xTest, yTrain, yTest = model_selection.train_test_split(X,
                                                                Y,
                                                                test_size=0.2)

xTrain = xTrain.reshape(len(xTrain), -1)
yTrain = yTrain.reshape(len(yTrain), -1)
clf = neighbors.KNeighborsClassifier()
clf.fit(xTrain, np.ravel(yTrain))
accuracy = clf.score(xTest, yTest)

#
# [parti, fodd, kon, intressent_id]
exampleMeasure = np.array([[1, 1964, 1, 853831481615],
                           [0, 1970, 1, 545353563812],
                           [6, 1989, 0, 496341906327]])
exampleMeasure = exampleMeasure.reshape(len(exampleMeasure), -1)
prediction = clf.predict(exampleMeasure)

decodedList = encoder.inverse_transform(prediction)

print('Decoded answer(s):', str(list(decodedList)))
print('Accuracy (%):', round(accuracy * 100, 1))

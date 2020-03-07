import numpy as np
import numpy
import pandas
from keras.engine.saving import model_from_json
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
from sklearn.metrics import auc
from sklearn.metrics import roc_curve
from scipy import interp
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn.metrics import accuracy_score
import normalizzazione as norm

def baseline_model():
  # create model
  model = Sequential()
  model.add(Dense(500, activation='tanh', input_dim=11))
  model.add(Dense(200, activation='relu'))
  model.add(Dense(100, activation='relu'))
  model.add(Dense(4, activation='softmax'))

  # Compile model
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
  return model

seed = 7
numpy.random.seed(seed)

n_classes = 4

dataframe = pandas.read_csv("dataset.csv", header=None,sep = ";")

dataset = dataframe.values

X = dataset[:,0:11]
Y = dataset[:,11]
#scaler = MinMaxScaler (feature_range = (-1,1))
#dummy_x = scaler.fit_transform(X)
dummy_x = norm.normalize(X)

encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)

print(dummy_x)

X_train, X_test, y_train, y_test = train_test_split(dummy_x,dummy_y, test_size = 0.2)

print('Calcolo...')


keras_model = baseline_model()
history = keras_model.fit(X_train, y_train, epochs = 30, batch_size = 80, verbose = 1,shuffle=False,validation_split=0.33)

y_score = keras_model.predict(X_test)
score = keras_model.evaluate(X_test, y_test, verbose=0)
score1 = keras_model.evaluate(X_train, y_train, verbose=0)
print("Accuracy Train: %.2f%%" % (score1[1]*100))
print("Accuracy Test: %.2f%%" % (score[1]*100))


predictions = keras_model.predict_classes(X_test)

countPositive = 0
countNegative = 0

for i in range(len(X_test)):
      if(predictions[i] == 0):
            if(y_test[i][0] == 1):
                  countPositive = countPositive + 1
            else:
                  countNegative = countNegative + 1
      if(predictions[i] == 1):
            if(y_test[i][1] == 1):
                  countPositive = countPositive + 1
            else:
                  countNegative = countNegative + 1
      if(predictions[i] == 2):
            if(y_test[i][2] == 1):
                  countPositive = countPositive + 1
            else:
                  countNegative = countNegative + 1
      if(predictions[i] == 3):
            if(y_test[i][3] == 1):
                  countPositive = countPositive + 1
            else:
                  countNegative = countNegative + 1
      print('(Prediction %d) => (expected %s)' % (predictions[i], y_test[i]))

print("Numero dati esaminati: %d" % len(X_test))
print("True Positive %d" % countPositive)
print("False Positive %d" % countNegative)


print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

lw = 2

fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(4):
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

# Compute macro-average ROC curve and ROC area

# First aggregate all false positive rates
all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))

# Then interpolate all ROC curves at this points
mean_tpr = np.zeros_like(all_fpr)
for i in range(n_classes):
    mean_tpr += interp(all_fpr, fpr[i], tpr[i])

# Finally average it and compute AUC
mean_tpr /= n_classes

fpr["macro"] = all_fpr
tpr["macro"] = mean_tpr
roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

# Plot all ROC curves
plt.figure(1)
plt.plot(fpr["micro"], tpr["micro"],
         label='micro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["micro"]),
         color='deeppink', linestyle=':', linewidth=4)

plt.plot(fpr["macro"], tpr["macro"],
         label='macro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["macro"]),
         color='navy', linestyle=':', linewidth=4)

colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])
for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=lw,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=lw)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Some extension of Receiver operating characteristic to multi-class')
plt.legend(loc="lower right")
plt.show()


# Zoom in view of the upper left corner.
plt.figure(2)
plt.xlim(0, 0.2)
plt.ylim(0.8, 1)
plt.plot(fpr["micro"], tpr["micro"],
         label='micro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["micro"]),
         color='deeppink', linestyle=':', linewidth=4)

plt.plot(fpr["macro"], tpr["macro"],
         label='macro-average ROC curve (area = {0:0.2f})'
               ''.format(roc_auc["macro"]),
         color='navy', linestyle=':', linewidth=4)

colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])
for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=lw,
             label='ROC curve of class {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=lw)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Some extension of Receiver operating characteristic to multi-class')
plt.legend(loc="lower right")
plt.show()

model_json = keras_model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

keras_model.save_weights("model.h5")
print("Saved model to disk")

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("model.h5")
print("Loaded model from disk")

loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
score = loaded_model.evaluate(X_train, y_train, verbose=0)
predictions = loaded_model.predict_classes(X_test)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
for i in range(len(X_test)):
    print('(Prediction %d)' % (predictions[i]))
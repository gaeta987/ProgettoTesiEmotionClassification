import pandas
from keras.engine.saving import model_from_json
import normalizzazione as norm

dataframe = pandas.read_csv("dataset.csv", header=None,sep = ";")

dataset = dataframe.values

X = dataset[:,0:11]
dummy_x = norm.normalize(X)

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("model.h5")
print("Loaded model from disk")

loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
predictions = loaded_model.predict_classes(dummy_x)

last = predictions[0]
if(last == 0):
    print('Felicità')
if(last == 1):
    print('Tristezza')
if(last == 2):
    print('Rabbia')
if(last == 3):
    print('Paura')

for i in range(len(dummy_x)):
    if (predictions[i] != last):
        last = predictions[i]
        if (last == 0):
            print('Felicità')
        if (last == 1):
            print('Tristezza')
        if (last == 2):
            print('Rabbia')
        if (last == 3):
            print('Paura')
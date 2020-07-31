from MalwareDetection import *
import os
import re
import string
import json
from matplotlib import pyplot as plt
import pandas as pd
import random
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
import numpy as np
from collections import Counter
import pickle
import sys


# Usage information if the training files have already been filtered, just do python3 train.py
# else python3 train.py filter <path to training data>

if len(sys.argv) == 3 and sys.argv[1] == 'filter' and os.path.exists(sys.argv[2]) and os.path.exists(sys.argv[2]+'/Static_Analysis_Data'):
	FILE_LIST_BENIGN = os.listdir('Static_Analysis_Data/Benign')
	FILE_LIST_BACKDOOR = os.listdir('Static_Analysis_Data/Malware/Backdoor')
	FILE_LIST_TROJAN = os.listdir('Static_Analysis_Data/Malware/Trojan')
	FILE_LIST_TROJANDOWNLOADER = os.listdir('Static_Analysis_Data/Malware/TrojanDownloader')
	FILE_LIST_TROJANDROPPER = os.listdir('Static_Analysis_Data/Malware/TrojanDropper')
	FILE_LIST_VIRUS = os.listdir('Static_Analysis_Data/Malware/Virus')
	FILE_LIST_WORM = os.listdir('Static_Analysis_Data/Malware/Worm')
	filter_data(FILE_LIST_VIRUS,'.',FILTERED_FILES_PATH,'virus')
	print("VIRUS DONE")
	filter_data(FILE_LIST_TROJANDROPPER,'.',FILTERED_FILES_PATH,'trojandropper')
	print("TROJAN DROPPER DONE")
	filter_data(FILE_LIST_WORM,'.',FILTERED_FILES_PATH,'worm')
	print("WORM DONE")
	filter_data(FILE_LIST_TROJAN,'.',FILTERED_FILES_PATH,'trojan')
	print("TROJAN DONE")
	filter_data(FILE_LIST_BENIGN,'.',FILTERED_FILES_PATH)
	print("BENIGN DONE")
	filter_data(FILE_LIST_BACKDOOR,'.',FILTERED_FILES_PATH,'backdoor')
	print("BACKDOOR DONE")
	filter_data(FILE_LIST_TROJANDOWNLOADER,'.',FILTERED_FILES_PATH,'trojandownloader')
	print("TROJANDOWNLOADER DONE")


FILTERED_FILES_PATH = 'filtered_data'
TRAIN_CSV = 'training_data.csv'
MODEL_NAME = 'trained_model.pickle'
filter_csv(FILTERED_FILES_PATH, TRAIN_CSV)

df = pd.read_csv(TRAIN_CSV)
features = df[['num_strings', 'len','avg_entropy','packer','max_en','min_en','num_addr','udp_dst']]
labels = df[['label']]
X_train, X_test, Y_train, Y_test = train_test_split(features, labels, test_size=0.1, shuffle=True)
dtc = DecisionTreeClassifier()
bag=BaggingClassifier(base_estimator=dtc, n_estimators=100, bootstrap=True)
bag.fit(X_train, np.ravel(Y_train)) 

Y_test = np.ravel(Y_test)
print("BAG SCORE:",bag.score(X_test,Y_test))
Y_pred = bag.predict(X_test)
Y_pred_binary = np.array([i=='benign' for i in Y_pred])
Y_test_binary = np.array([i=='benign' for i in np.ravel(Y_test)])
print("ACCURACY:",accuracy_score(Y_test_binary, Y_pred_binary))
precision, recall, fscore, support = precision_recall_fscore_support(Y_pred_binary, Y_test_binary)
print("PRECISION:",precision)
print("RECALL:",recall)
print("F-SCORE:",fscore)
print("SUPPORT:",support)

with open(MODEL_NAME,'wb') as model_file:
	pickle.dump(bag, model_file)

print("model saved in {}".format(MODEL_NAME))

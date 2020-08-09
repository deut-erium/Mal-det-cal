import sys
import os

if len(sys.argv) == 1:  #no arguments provided, just remove temp_features.csv, output.csv, and temp_test_filtered
	os.remove('temp_features.csv')
	os.remove('output.csv')
	for root, dirs, files in os.walk('temp_test_filtered'):
	for file in files:
		os.remove(os.path.join(root, file))

elif len(sys.argv) == 2 and sys.argv[1] == 'train':
	os.remove('training_data.csv')
	os.remove('trained_model.pickle')

elif len(sys.argv) == 2 and sys.argv[1] == 'all':
	os.remove('temp_features.csv')
	os.remove('output.csv')
	for root, dirs, files in os.walk('temp_test_filtered'):
	for file in files:
    	os.remove(os.path.join(root, file))
	os.remove('training_data.csv')
	os.remove('trained_model.pickle')

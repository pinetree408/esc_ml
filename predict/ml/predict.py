from sklearn import datasets, svm, metrics
import random
import os
import numpy


def predict(atom_category):
    # Initialize Data set path
    path = "../Graphene_6x6_doping/" + atom_category

    # Initialize default value
    data_set = []
    target_list = []

    # Parse Data
    for i in os.listdir(path):
        for j in os.listdir(path + '/' + i):
	    if j == 'DOS':
	        f = open(path+ '/' + i + '/' + j, 'r')
	        f_lines = f.readlines()
	        result = []
	        for line in f_lines[11:]:
                    data = line.split('\n')[0].split(' ')
		    temp = []
		    for k in data:
                        if k != '':
                            temp.append(k)
                    result.append(numpy.float64(temp[1]))
	        f.close()
	        data_set.append(result)
		f_sturct = open(path + '/' + i +'/STRUCT.fdf', 'r')
                target_list.append(i)

    n_samples = len(target_list)

    # spliter
    pre_target_list = list(target_list)
    data_dictionary = dict(zip(target_list, data_set))
    random.shuffle(target_list)
    data_set_shuffled = []
    for target in target_list:
        data_set_shuffled.append(data_dictionary.get(target))

    target_list_shuffled = []
    for target in target_list:
        index = pre_target_list.index(target)
        target_list_shuffled.append(numpy.int64(index))

    target_list_shuffled = numpy.array(target_list_shuffled)
    data_set_shuffled = numpy.array(data_set_shuffled)

    # Create a classifier: a support vector classifier
    classifier = svm.SVC(gamma=0.001)

    # We learn the digits on the first half of the digits
    classifier.fit(data_set_shuffled[:(n_samples/2)], target_list_shuffled[:(n_samples/2)])

    # Now predict the value of the digit on the second half:
    expected = target_list_shuffled[(n_samples/2):]
    predicted = classifier.predict(data_set_shuffled[(n_samples/2):])

    print("Classification report for classifier %s:\n%s\n"
        % (classifier, metrics.classification_report(expected, predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

    expected_data = []
    for item in expected:
        expected_data.append(data_set_shuffled[item])

    predicted_data = []
    for item in predicted:
        predicted_data.append(data_set_shuffled[item])

    for i in range(len(expected_data)):
        difference = [item for item in expected_data[i] if item not in predicted_data[i]]
        precent = len(difference) * 1.0 / len(expected_data[i]) * 100
    
    return [predicted_data[0], expected_data[0]]
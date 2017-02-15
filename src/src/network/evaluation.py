import csv
from sklearn.metrics import *


def read_data(list):
    with open('output/' + list + '_modClass.csv', 'r') as csvfile:
        reader1 = csv.reader(csvfile)
        mod_class = [row[1] for row in reader1]

    with open('output/' + list + '_expClass.csv', 'r') as csvfile:
        reader2 = csv.reader(csvfile)
        exp_class = [row[1] for row in reader2]

    del mod_class[0]
    del exp_class[0]
    return mod_class, exp_class


def confusion_matrix(mod_class, exp_class):
    # confusion matrix
    correct = 0.
    total = 0.

    for i in range(len(mod_class)):
        for j in range(i+1, len(mod_class)):
            total += 1.
            if mod_class[i] == mod_class[j] and exp_class[i] == exp_class[j]:
                correct += 1.
            if mod_class[i] != mod_class[j] and exp_class[i] != exp_class[j]:
                correct += 1.

    accuracy = correct/total
    return accuracy


def ami(mod_class, exp_class):
    return adjusted_mutual_info_score(exp_class, mod_class)


def nmi(mod_class, exp_class):
    return normalized_mutual_info_score(exp_class, mod_class)


if __name__ == '__main__':
    mod_class, exp_class = read_data('rv')
    accuracy = confusion_matrix(mod_class, exp_class)
    ami = ami(mod_class, exp_class)
    nmi = nmi(mod_class, exp_class)
    print('The accuracy computed from confusion matrix is ' + str(accuracy))
    print('NMI: ' + str(nmi))
    print('AMI: ' + str(ami))

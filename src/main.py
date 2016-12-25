from src.customcsv import parse_to_array
from src.task import random_select_sample, extract_sample
from src.classifier import KNN


dataset = parse_to_array('iris.data')
sample = random_select_sample(dataset, 80)
classifier = KNN(5) # make k odd and >= 5

extract_sample(sample, dataset)

classifier.run(sample, dataset)
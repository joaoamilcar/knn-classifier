from src.metrics import distance_euclid


class KNN:
    def __init__(self, k):
        self.k = k
        self.KXnear = []

    def run(self, sample, dataset):
        count_classified_correctly = 0

        for s in sample:
            self.KXnear = []
            Xnew = s[:(len(s) - 1)]  # unknown class

            for d in dataset:
                if len(self.KXnear) < self.k:
                    self.KXnear.append(d)
                else:
                    self.update_KXNear(Xnew, d)

            predominantClass = self.get_most_frequent_class(self.KXnear)

            if s[len(s) - 1] == predominantClass:
                print('success')
                print("sample            ", s)
                print("k neighbours      ", self.KXnear)
                print("predominant class ", predominantClass)
                print("-")
                count_classified_correctly += 1
                dataset.append(s)
            else:
                print('fail')
                print("sample            ", s)
                print("k neighbours      ", self.KXnear)
                print("predominant class ", predominantClass)
                print("-")
                continue

        print("")
        print("Classified     : ", len(sample))
        print("Correct        : ", count_classified_correctly)
        print("Sucess rate (%): ", (count_classified_correctly * 100) / len(sample))

    def get_most_frequent_class(self, neighbours):
        classes = set()
        arrayClasses = []
        counterClass = 0
        mostFrequentClass = ''

        for n in neighbours:
            className = n[len(neighbours) - 1]
            classes.add(className)
            arrayClasses.append(className)

        for c in classes:
            if arrayClasses.count(c) > counterClass:
                counterClass = arrayClasses.count(c)
                mostFrequentClass = c

        return mostFrequentClass

    def update_KXNear(self, Xnew, d):
        Xfar = self.find_further_neighbour(Xnew)

        if distance_euclid(Xnew, Xfar) > distance_euclid(Xnew, d):
            self.KXnear.remove(Xfar)
            self.KXnear.append(d)

    def find_further_neighbour(self, Xnew):
        farDistance = 0
        Xfar = []

        for n in self.KXnear:
            distance = distance_euclid(Xnew, n)

            if distance >= farDistance or farDistance == 0:
                farDistance = distance
                Xfar = n

        return Xfar
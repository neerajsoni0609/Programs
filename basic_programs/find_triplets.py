class Triplet:
    def __init__(self, elements) -> None:
        self.elements = elements

    def find_triplets(self):
        self.triplets = []
        n = len(self.elements)
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if self.elements[i] + self.elements[j] + self.elements[k] == 0:
                        self.triplets.append((self.elements[i], self.elements[j], self.elements[k]))

        return self.triplets
    

list1 = [-25, -10, -7, -3, 2, 4, 8, 10]
trip = Triplet(list1)
triplets = trip.find_triplets()
print(triplets)
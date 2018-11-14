class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    # max1=0
    def computeDifference(self):
        max1 = 0
        for i in range(len(self.__elements)):  # both way variablw works as self.elements or a
            for j in range(i + 1, len(a)):
                diff = abs(a[i] - a[j])  # finding the absolute difference
                if (self.maximumDifference < diff):
                    self.maximumDifference = diff
        return self.maximumDifference  # returning the sum


# def maximumDifference(self):
# return max1


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
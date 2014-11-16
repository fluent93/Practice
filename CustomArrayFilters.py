#list is the built_in class. So if I want to add member function, I have to declare the class.

class list:
# initialize the class 'list'
    def __init__(self, lst):
        self.lst = lst

# Just in case there are non-int elements, filter the list into the list of integer values
# and then write the function of even (elem % 2 == 0)
# I used 'List Comprehension' to make the list

    def even(self):
        l = [elem for elem in self.lst if type(elem) == int]
        return [elem2 for elem2 in l if elem2 % 2 == 0 ]

    def odd(self):
        l = [elem for elem in self.lst if type(elem) == int]
        return [elem2 for elem2 in l if elem2 % 2 == 1 ]
        
    def under(self, i):
        l = [elem for elem in self.lst if type(elem) == int]
        return [elem2 for elem2 in l if elem2 < i]

    def over(self, i):
        l = [elem for elem in self.lst if type(elem) == int]
        return [elem2 for elem2 in l if elem2 > i]

    def in_range(self, i, j):
        l = [elem for elem in self.lst if type(elem) == int]
        return [elem2 for elem2 in l if i <= elem2 <= j]
import sys

rl = lambda : sys.stdin.readline()


class TestCase:
    def __init__(self, read_temp):
        self.kind_of_book_count = int(read_temp.split(" ")[0])
        self.pouch_size = int(read_temp.split(" ")[1])

    def __str__(self):
        return "kind_of_book_count: %d, pouch_size: %d" % (self.kind_of_book_count, self.pouch_size)

class Book:
    def __init__(self, read_temp):
        self.size = int(read_temp.split(" ")[0])
        self.valuation = int(read_temp.split(" ")[1])
        self.count =  int(read_temp.split(" ")[2])

    def __str__(self):
        return "size: %d, valuation: %d, count: %d" % (self.size, self.valuation, self.count)


def process(test_case, books):
    print(test_case)
    for i in books:
        print(i)


def input():
    test_case_count = int(rl())

    for i in range(test_case_count):
        test_case = TestCase(rl())

        books = []
        for j in range(test_case.kind_of_book_count):
            book = Book(rl())
            books.append(book)

        process(test_case, books)

if __name__ == '__main__':
    input()
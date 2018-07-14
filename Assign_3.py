
"""

Loops in a program go over a particular set of actions repeatedly until a condition is met/not met. Below is a list with a set of numbers as given below. Print out all the even numbers in the sequence. Write the solution (in Python 3) into a function and have it called in your main block for the requested answer.

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]

"""

def find_even(numbers= None):
    numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
    numbers_seq = next(item for item in numbers if item["sequence"])
    numbers_split = numbers_seq["sequence"].split(',')
    find_even = ",".join(item for item in numbers_split if int(item)%2 == 0)
    print("output : The even numbers are : "+find_even)


if __name__ == "__main__":
    find_even()




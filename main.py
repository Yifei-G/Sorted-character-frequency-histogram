from os import strerror

mydict = {}
value = 1
fileName = input("please enter the file name(including the extension):")


def processChar(char):
    if char.isalpha():
        # as requested by the exercise, upper case and lower case are treated equally
        # forcing the char to be lowercase.
        lowerChar = char.lower()
        # try to find the key value (lowerChar) in mydict
        if lowerChar in mydict:
            mydict[lowerChar] += value
        else:
                # if the key is not in mydict yet, put into mydict and assign
                # value = 1
            mydict[lowerChar] = value
    else:
        print("excliding non-latin characters:", char, " is not a letter!")


# Reading the file from the directory
try:
    stream = open(fileName, "rt")
    char = stream.read(1)
    while char != "":
        processChar(char)
        char = stream.read(1)
    stream.close()
    # generate a sorted dict using sorted() function
    # using the key parameter indicating that the value of mydict is used for sorting.
    # set reverse to True, to sort in descending order
    # sorted() returns a list, to regenerate the dict, use dict() function
    sortedDict = dict(
        sorted(mydict.items(), key=lambda item: item[1], reverse=True))
    for char, frequency in sortedDict.items():
        print(char, "--->", frequency)
except IOError as e:
    print("The file can't be read:", strerror(e.errno))

# Writing the test.hist file to the directory
try:
    fileName = "test.hist"
    stream = open(fileName, "wt")
    for char, frequency in sortedDict.items():
        # Generating the string for writing into the file
        histogrm = char + "--->" + str(frequency) + "\n"
        stream.write(histogrm)
    stream.close()
    print("Wring completed!!! Check the result file in the directory!")
except IOError as e:
    print("Can't generate the output file!", strerror(e.errno))

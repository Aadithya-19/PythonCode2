def wordCount():

    cw = 0

    i = (input("Enter the file path you want to count: "))
    File_object = open(i, 'r')

    for a in File_object:
        w = a.split()
        cw = cw  + len(w)

    print(cw)

wordCount()
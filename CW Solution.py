
# I declare that my work contailns no examples of misconduct, such as plagiarism, or collusion
# Any code taken from other soureses is referenced within my code solution.
# Stident ID : 20211418(w1901420)
# Date : 4/17/2022


procount = 0  # global variable
promodulcount = 0  # global variable
excount = 0  # global variable
donotcount = 0  # global variable


# value entered as the the argument is the parameter
def outofrange(value):
    isoutofrange = False
    if value < 0 or value > 120 or value % 20 != 0:
        print("Value out of range !!")
        isoutofrange = True
        return isoutofrange


# function to calculate whether the total is exceeding 120
def total_check(p, d, f):
    is_total_correct = True
    if (p + d + f) != 120:
        print("Total incorrect")
        is_total_correct = False
    return is_total_correct


# function to only allow integer values in
def type_check(value):
    isint = True
    try:
        value = int(input("Enter your total pass credits : "))
    except ValueError:
        print("INT reqiured")

        isint = False
        print("Please enter a integer")
    return isint




# output prediction
# keep count of predictions
def progress_check(pass1, defer2, fail3):
    global insidecount
    if pass1 == 120:
        print("Progress")
        global procount
        procount = procount + 1
        return "Progress", pass1, defer2, fail3
    else:
        if pass1 == 100:
            print("Progress (module trailer)")
            global promodulcount
            promodulcount = promodulcount + 1
            return "Progress (module trailer)", pass1, defer2, fail3
        else:
            if fail3 > (pass1 + defer2):
                print("Exclude")
                global excount
                excount = excount + 1
                return "Exclude", pass1, defer2, fail3
            else:
                print("Do not progress (module retriever)")
                global donotcount
                donotcount = donotcount + 1
                return "Do not progress (module retriever)", pass1, defer2, fail3


def horizontal_histogram():
    print("__________________________________________________________")
    print("Horizontal histogram")
    print("Progress ", procount, "     :" + ('*' * procount))
    print("Trailer ", promodulcount, "      :" + ('*' * promodulcount))
    print("Retriever ", donotcount, "    :" + ('*' * donotcount))
    print("Excluded ", excount, "     :" + ('*' * excount))
    print()
    print(excount+donotcount+promodulcount+procount , "Outcomes in Total")
    print("__________________________________________________________")


# function to display their vertical histogram
def vertical_histogram():
    print("Progress    Trailer    Retriever    Exclude")
    # used a max function to determine the for loop repetiotion times
    for i in range(max(procount,donotcount,promodulcount,excount)):
        i += 1
        if procount >= i:
            print("  *", end="          ")
        else:
            print("             ", end="")
        if promodulcount >= i:
            print("  *", end="          ")
        else:
            print("             ", end="")
        if donotcount >= i:
            print(" *", end="          ")
        else:
            print("             ", end="")
        if excount >= i:
            print(" *", end="          ")
        else:
            print("             ", end="")
        print("")
    print(excount+donotcount+promodulcount+procount , "Outcomes in Total")



lt = []
# I did the part 3 using 2 lists where every time a user enters a complet three sets of credits, i crets a list with those three creditd and the progresion. Once the loop ends for that instance, i will insert this small list ti a larger list. 
# this inserts the small lists to the next element of the large list
def list_build(predic, p, d, f):
    ar = [predic, p, d, f]
    lt.insert(len(lt), ar)

#prints the smalle lists in the large list
def print_list_build():
    for x in range(len(lt)):
        print(lt[x][0], " - ", lt[x][1], ", ", lt[x][2], ", ", lt[x][3])

#Extracting smaller list from the large list and writing the smaller list to each line of the file
def fille_write():
    for x in range(len(lt)):
        with open("test.txt", "a") as f:
            f.write(str(lt[x][0]) + " - " + str(lt[x][1]) + ", " + str(lt[x][2]) + ", " + str(lt[x][3]) + "\n")

#Readinf the whole file at once and displaying the read result
def file_read():
    with open("test.txt", "r") as f:
        content = f.read()
        print(content)


# main
def main():
    # initialise choice as 'y' so the loop repeats for the first time
    choice = "y"
    while choice == "y":
        try:
            passc = int(input("Enter your total pass credits : "))
        except ValueError:
            print("Please enter a integer !!")
            continue
        rangecheck = outofrange(int(passc))
        if rangecheck:
            continue
        try:
            deferc = int(input("Enter your total defer credits : "))
        except ValueError:
            print("Please enter a integer !!")
            continue
        rangecheck = outofrange(deferc)
        if rangecheck:
            continue
        try:
            failc = int(input("Enter your total Fail credits : "))
        except ValueError:
            print("Please enter a integer !!")
            continue
        rangecheck = outofrange(failc)
        if rangecheck:
            continue
        tot_check = total_check(passc, deferc, failc)
        if not tot_check:
            continue
        out, p, d, f = progress_check(passc, deferc, failc)
        list_build(out, p, d, f)
        print("Would you like to enter another set of data ? ")
        choice = input("Enter 'y' to continue or 'txt' to output the data stored':\n 'h' to quite and view results in "
                       "Horizontal Histogram \n 'v' "
                       "to "
                       "quite and view results in vertical histogram : ")
        #validation for choice input
        while choice != "y" and choice != "v" and choice != "h" and choice != "txt":
            print("Invalid input!!! Please enter a valid input('h','v','y','txt') : ", end="")
            choice = input()
    if choice == "txt":
        file_read()

    if choice == "h":
        horizontal_histogram()
        print_list_build()
        fille_write()
    elif choice == 'v':
        vertical_histogram()
        print_list_build()
        fille_write()

#Calling the mailn function, the fisrt line tobe executed
if __name__ == '__main__':
    main()

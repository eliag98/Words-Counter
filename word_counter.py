
def empty_line():
    print("")

def count():
    global line_count
    global sentence_count
    global characters_count
    global words_count
    line_count = 0
    sentence_count = 0
    characters_count = 0
    words_count = 0
    for line in opened_file :
        if line.endswith("\n"):
            line_count += 1
        elif not line.endswith("\n") and line_count > 1:
            line_count += 1
        else:
            line_count = line_count
        for character in line:
            characters_count += 1
            if character == '.' or character == '!' or character == '?' or character == ':' or character == ',':
                sentence_count += 1
        if sentence_count >= 1:
            sline = line.split()
            for word in sline:
                words_count += 1
        else:
            words_count = 1

def reload():
    empty_line()
    app()

def app():
    print("Welcome to Words Counter")
    print("########################")
    empty_line()
    print("P.S. In order for this application to work correctly, the file should be in the same directory as the script.")
    print("P.S.2. The file should have a .txt format.")
    print("Thank you for understanding...")
    empty_line()
    print("Please select where do you want to count  from: ")
    print("------------------------------------------------")
    empty_line()
    print("For counting letters from a file: type ==> (1) ")
    answer = input("Response: ")
    global opened_file
    global line_count
    global sentence_count
    global characters_count
    global words_count
    if answer == "1" :
        try:
            file = input("Enter file name here: ")
            opened_file = open(file)

            count()
        except:
            print("Could not open file. Please try again and check that the file's name is correct.")
            reload()
    else:
        print("### Wrong Input Please choose 1/2 options. ###")
        reload()


    empty_line()
    print("Results:")
    print("######## ")
    print("1. There are " + str(line_count) + " lines in this file.")
    print("2. There are " + str(characters_count) + " characters in this file.")
    print("3. There are " + str(sentence_count) + " sentences in this file.")
    print("4. There are " + str(words_count) + " words in this file.")
    empty_line()
    print("##############################################################")
    print("Thank you for using our software. Press any key to continue...")
    p = input("##############################################################")

app()

### Created by Elia ###
### Email: eliework98@gmail.com ###

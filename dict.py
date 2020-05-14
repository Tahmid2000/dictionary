import json
import difflib

data = json.load(open(
    "/Users/tahmidimran/Visual Studio/Python Udemy Course/dictionary/data.json"))


def findWord(inp):
    if inp.lower() in data.keys():
        return printList(data[inp.lower()])
    else:
        mys = similarWord(inp.lower())
        if mys != None:
            return printList(data[mys])
        else:
            return str('Word not found.')


def similarWord(inp):
    closeMatch = difflib.get_close_matches(inp, data.keys(), 5, .7)
    for word in closeMatch:
        toinput = 'Did you mean ' + str(word) + '? (Yes or No)\n'
        yesNo = input(toinput)
        if yesNo.lower() == 'yes':
            return word
    return None


def printList(theList):
    output = ''
    for i in range(len(theList)):
        output += '\n' + str(i+1) + '. ' + theList[i]
    return output


def main():
    toFind = input('Input word (empty string to quit):\n')
    while toFind != '':
        print(findWord(toFind))
        toFind = input('Input word (empty string to quit):\n')


if __name__ == "__main__":
    main()

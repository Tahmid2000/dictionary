import json
import difflib
import mysql.connector
from ast import literal_eval

myDB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password123',
    database='test1'
)

cursor = myDB.cursor(buffered=True)
# these statements were used to create the test1 database and dictionary table
"""
cursor.execute("CREATE DATABASE test1")
cursor.execute("SHOW DATABASES")
 for db in cursor:
    print(db)

cursor.execute("CREATE TABLE words(word VARCHAR(255), defs VARCHAR(255))")
cursor.execute("SHOW TABLES")
 for tb in cursor:
    print(tb)
cursor.execute("CREATE TABLE words3(word VARCHAR(255), defs VARCHAR(65535))")
sqlFormula = "INSERT INTO words3(word,defs) VALUES(%s,%s)"
def2 = ('train', str(data['train']))
allDefs = []
def1 = ('', '')
for key in data.keys():
    def1 = (key, str(data[key]))
    allDefs.append(def1)

cursor.executemany(sqlFormula, allDefs)

 cursor.execute("SELECT * FROM words3")
 result = cursor.fetchall()
 result = cursor.fetchone()
 for row in result:
    print(row)
 myDB.commit()
"""


def findWord(inp):
    sqlForm = "SELECT defs FROM words3 WHERE word= %s"
    cursor.execute(sqlForm, (inp.lower(), ))
    result = cursor.fetchone()
    if result != None:
        result = list(result)[0]
        theArr = literal_eval(result)
        return printList(theArr)
    else:
        mys = similarWord(inp.lower())
        if mys != None:
            cursor.execute(sqlForm, (mys, ))
            result = cursor.fetchone()
            result = list(result)[0]
            theArr = literal_eval(result)
            return printList(theArr)
        else:
            return str('Word not found.')


def similarWord(inp):
    poss = []
    sqlForm = "SELECT word FROM words3 WHERE word LIKE %s"
    for i in range(1, len(inp)):
        cursor.execute(sqlForm, (inp.lower()[0:i] + '%', ))
        result = cursor.fetchall()
        poss.append(result)
    newPoss = [a_tuple[0] for a_tuple in poss[0]]

    closeMatch = difflib.get_close_matches(inp, newPoss, 10)
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

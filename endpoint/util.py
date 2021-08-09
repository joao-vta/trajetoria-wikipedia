import mysql.connector 
import json

def getIdFromName(name, cursor):
    cursor.execute("SELECT min(id) FROM wikipedia.paginas WHERE name = %s", (name.lower(),))
    row = cursor.fetchone()
    if row == None:
        print("no id")
        raise ValueError('Tried to find ID not in db')
    else:
        return(row[0])
        
def getNameFromId(id, cursor):
    cursor.execute("SELECT min(id),name FROM wikipedia.paginas WHERE id=%s", (id,))
    row = cursor.fetchone()
    if row == None:
        raise ValueError('tried to find Name not in db')
    else:
        return(row[1])

def selectMany(toExec, many, cursor): #selects for many values in db
    toExec += "("
    toExec += "%s," * len(many)
    toExec = toExec[:-1]
    toExec += ")"
    cursor.execute(toExec, [value[0] for value in many])
    
def makeJSON(message):
    return {
        "statusCode": 200,
        'headers': { 'Content-Type': 'application/json' },
        "body": json.dumps(message)
    }
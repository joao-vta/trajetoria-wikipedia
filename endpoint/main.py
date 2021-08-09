import mysql.connector 
import tree
import util
import json 

startID = 0

    
def makeConnection(oneNode, otherNode, cursor):
    try:
        cursor.fetchall()
    except:
        pass
    
    if   (oneNode.getAncestor().value   == startID):
        startNode = oneNode
        endNode   = otherNode
    elif (otherNode.getAncestor().value == startID):
        startNode = otherNode
        endNode   = oneNode
    else:
        print("Error: invalid connection")
        raise ValueError('Tried to print connection from node not in tree')
    
    result = startNode.getAncestorList() #gets startNode ancerstors from root to current
    while endNode != None:               #gets endNode acenstors from current to root
        result += [endNode.value]
        endNode = endNode.parent
    print([util.getNameFromId(val, cursor) for val in result])
    return ([util.getNameFromId(val, cursor) for val in result]) #result: start root to end root
        
def addToTreeIfNotOnOther(toAdd, toCompare, cursor):
    '''
    Adds element aplying bidirectional search
    Expects cursor to have executed query that has 
    elements to add on [1] and elements already on tree on [0]
    '''
    nextRow = cursor.fetchone()
    while nextRow != None:
        startNode, endNode = nextRow
        isInOther = toCompare.find(endNode)
        if isInOther == None:
            alreadyHere = (toAdd.find(endNode) != None)
            if not alreadyHere:
                toAdd.find(startNode).add(endNode)
        else:
            return makeConnection(toAdd.find(startNode), isInOther, cursor)
        nextRow = cursor.fetchone()

def find_path(event, context):
    global startID
    
    if 'startName' in event and 'endName' in event:
        startName = event['startName']
        endName = event['endName']
    elif 'body' in event and 'startName' in event['body'] and 'endName' in event['body']:
        mainBody = json.loads(event['body'])
        startName = mainBody['startName']
        endName = mainBody['endName']
    else:
        return util.makeJSON("ERROR no startname or endname")
    
    cnx = mysql.connector.connect(user='xxxx', password='xxxx',
                                host='xxxxxxxx.com',
                                database='wikipedia')
    cursor = cnx.cursor()

    try:
        startID = util.getIdFromName(startName, cursor)
        leftTree = tree.Node(startID, None)

        endID = util.getIdFromName(endName, cursor)
        rightTree = tree.Node(endID, None)
    except:
        return util.makeJSON("ERROR retriving ID from database")
    
    if startID == None or endID == None:
        return util.makeJSON("ERROR name not in dabatase")
        
    leftChildren = leftTree.getNDepthValues(0)
    util.selectMany("SELECT source_id, dest_id FROM wikipedia.links WHERE source_id IN ", leftChildren, cursor)
    result = addToTreeIfNotOnOther(leftTree, rightTree, cursor)
    if result != None:
        return util.makeJSON(result)

    rightChildren = rightTree.getNDepthValues(0)
    util.selectMany("SELECT dest_id, source_id FROM wikipedia.links WHERE dest_id IN ", rightChildren, cursor)
    result = addToTreeIfNotOnOther(rightTree, leftTree, cursor)
    if result != None:
        return util.makeJSON(result)

    leftChildren = leftTree.getNDepthValues(1)
    util.selectMany("SELECT source_id, dest_id FROM wikipedia.links WHERE source_id IN ", leftChildren, cursor)
    result = addToTreeIfNotOnOther(leftTree, rightTree, cursor)
    if result != None:
        return util.makeJSON(result)

    rightChildren = rightTree.getNDepthValues(1)
    util.selectMany("SELECT dest_id, source_id FROM wikipedia.links WHERE dest_id IN ", rightChildren, cursor)
    result = addToTreeIfNotOnOther(rightTree, leftTree, cursor)
    if result != None:
        return util.makeJSON(result)
    
    leftChildren = leftTree.getNDepthValues(2)
    util.selectMany("SELECT dest_id, source_id FROM wikipedia.links WHERE dest_id IN ", leftChildren, cursor)
    result = addToTreeIfNotOnOther(leftTree, rightTree, cursor)
    if result != None:
        return util.makeJSON(result)
    
    rightChildren = rightTree.getNDepthValues(2)
    util.selectMany("SELECT dest_id, source_id FROM wikipedia.links WHERE dest_id IN ", rightChildren, cursor)
    result = addToTreeIfNotOnOther(rightTree, leftTree, cursor)
    if result != None:
        return util.makeJSON(result)

    cursor.close()
    cnx.close()
    return util.makeJSON("ERROR path too big")

print(find_path({'startName':'pateta', 'endName':'tristeza'}, None))
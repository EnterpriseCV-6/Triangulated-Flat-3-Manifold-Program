import math

edgetable = []
tetrahedralist = []


class Edge:
    def __init__(self,vertex1 = 1,vertex2 = 2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.edgelength = 1
        self.edgecurvature = 0
        self.tetrahedraEdgeIsIn = []

##    def calculateEdgeCurvature(self):
        
        
class Tetrahedron:
    dihedralanglelist = []
    
    def __init__(self,vertex1 = 1, vertex2 = 2, vertex3 = 3, vertex4 = 4):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3
        self.vertex4 = vertex4
        self.edgesintetrahedron = []  #stored as lists ex, edge 1,2 stored as [1,2]

    def checkLegalTetra(self):
        print(self.vertex2)

    def calculateDihedralAngles(self):
        edgetable[self.vertex1][self.vertex2].edgelength

def createEdgeTable(numberOfVerticies = 15):
    numberOfVerticies = numberOfVerticies+1
    for row in range(numberOfVerticies):
        edgetable.append([])
        for column in range(numberOfVerticies):
            edgetable[row].append(0)
    
def fillEdgeTable(listOfTetrahedra,tableOfEdges):
    for i in range(len(listOfTetrahedra)):
        for j in range(len(listOfTetrahedra[i].edgesintetrahedron)):
            # If edge is not in the the tableOfEdges, add it
            if tableOfEdges[listOfTetrahedra[i].edgesintetrahedron[j][0]][listOfTetrahedra[i].edgesintetrahedron[j][1]] == 0:
                # Assigns edge its name
                tableOfEdges[listOfTetrahedra[i].edgesintetrahedron[j][0]][listOfTetrahedra[i].edgesintetrahedron[j][1]] = Edge(listOfTetrahedra[i].edgesintetrahedron[j][0],listOfTetrahedra[i].edgesintetrahedron[j][1])
                # Adds tetrahedran to list of tetrahedra edge is in
                tableOfEdges[listOfTetrahedra[i].edgesintetrahedron[j][0]][listOfTetrahedra[i].edgesintetrahedron[j][1]].tetrahedraEdgeIsIn.append([listOfTetrahedra[i].vertex1,listOfTetrahedra[i].vertex2,listOfTetrahedra[i].vertex3,listOfTetrahedra[i].vertex4])
            # adds edge to tetrahera list if edge already exists
            else:
                tableOfEdges[listOfTetrahedra[i].edgesintetrahedron[j][0]][listOfTetrahedra[i].edgesintetrahedron[j][1]].tetrahedraEdgeIsIn.append([listOfTetrahedra[i].vertex1,listOfTetrahedra[i].vertex2,listOfTetrahedra[i].vertex3,listOfTetrahedra[i].vertex4])


def showEdgeTable(tableOfEdges):
    count = 0
    for i in range(len(tableOfEdges)):
        for j in range(len(tableOfEdges[i])):
            if tableOfEdges[i][j] != 0:
                print(tableOfEdges[i][j].vertex1,tableOfEdges[i][j].vertex2,tableOfEdges[i][j].tetrahedraEdgeIsIn)
                count = count+1
    print(count)

def createTetrahedraList(primalList):
    for i in range(len(primalList)):
        tetrahedralist.append(Tetrahedron(primalList[i][0],primalList[i][1],primalList[i][2],primalList[i][3]))
        tetrahedralist[i].edgesintetrahedron.append([primalList[i][0],primalList[i][1]])
        tetrahedralist[i].edgesintetrahedron.append([primalList[i][0],primalList[i][2]])
        tetrahedralist[i].edgesintetrahedron.append([primalList[i][0],primalList[i][3]])
        tetrahedralist[i].edgesintetrahedron.append([primalList[i][1],primalList[i][2]])
        tetrahedralist[i].edgesintetrahedron.append([primalList[i][1],primalList[i][3]])
        tetrahedralist[i].edgesintetrahedron.append([primalList[i][2],primalList[i][3]])
        print(tetrahedralist[i].vertex1,tetrahedralist[i].vertex2,tetrahedralist[i].vertex3,tetrahedralist[i].vertex4)
        print(tetrahedralist[i].edgesintetrahedron)
    

def main():
    print("Hello World")
    readFile = open('manifoldExample.txt')
    data = readFile.read()        #Prepares file for read in
    data = data.split("facets :=") #Look up strip to remove white space
    data[1] = data[1].strip('[];')
    data[1] = data[1].split('],[')
    tetrahedron = []
    for i in range(0, len(data[1])):   #List comprehensions
        tetrahedron.append(data[1][i])
    for i in range(0, len(tetrahedron)):
        tetrahedron[i] = tetrahedron[i].split(',')
    readFile.close()
    tetrahedron = [[int(i) for i in tetrahedron[j]] for j in range(len(tetrahedron))] #turns tetrahedron from str to int
    print(tetrahedron)    #prints info for debugging
    print(len(tetrahedron))
    createTetrahedraList(tetrahedron)
    createEdgeTable()
    print("Edge Table")
    for i in range(16):
        print(edgetable[i])
    fillEdgeTable(tetrahedralist,edgetable)
    showEdgeTable(edgetable)

main()

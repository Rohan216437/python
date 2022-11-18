#HillClimbing
import math
increment = 0.1
startingPoint = [1, 1]
point1 = [1,5]
point2 = [6,4]
point3 = [5,2]
point4 = [2,1]
def distance(x1, y1, x2, y2):
    dist = math.pow(x2-x1, 2) + math.pow(y2-y1, 2)
    return dist
def sumOfDistances(x1, y1, px1, py1, px2, py2, px3, py3, px4, py4):
    d1 = distance(x1, y1, px1, py1)
    d2 = distance(x1, y1, px2, py2)
    d3 = distance(x1, y1, px3, py3)
    d4 = distance(x1, y1, px4, py4)
    return d1 + d2 + d3 + d4
def newDistance(x1, y1, point1, point2, point3, point4):
    d1 = [x1, y1]
    d1temp = sumOfDistances(x1, y1, point1[0],point1[1], point2[0],point2[1],
    point3[0],point3[1], point4[0],point4[1] )
    d1.append(d1temp)
    return d1
minDistance = sumOfDistances(startingPoint[0], startingPoint[1],point1[0],point1[1], point2[0],point2[1],point3[0],point3[1], point4[0],point4[1] )
flag = True
def newPoints(minimum, d1, d2, d3, d4):
    if d1[2] == minimum:
        return [d1[0], d1[1]]
    elif d2[2] == minimum:
        return [d2[0], d2[1]]
    elif d3[2] == minimum:
        return [d3[0], d3[1]]
    elif d4[2] == minimum:
        return [d4[0], d4[1]]
i = 1
while flag:
    d1 = newDistance(startingPoint[0]+increment, startingPoint[1], point1, point2,point3, point4)
    d2 = newDistance(startingPoint[0]-increment, startingPoint[1], point1, point2,point3, point4)
    d3 = newDistance(startingPoint[0], startingPoint[1]+increment, point1, point2,point3, point4)
    d4 = newDistance(startingPoint[0], startingPoint[1]-increment, point1, point2,point3, point4)
    print (i,' ', round(startingPoint[0], 2), round(startingPoint[1], 2))
    minimum = min(d1[2], d2[2], d3[2], d4[2])
    if minimum < minDistance:
        startingPoint = newPoints(minimum, d1, d2, d3, d4)
        minDistance = minimum
#print i,' ', round(startingPoint[0], 2), round(startingPoint[1], 2)
        i+=1
    else:
        flag = False

#********************************************88

#3aalpha beta search
tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]] 
root = 0 
pruned = 0 
def children(branch, depth, alpha, beta): 
    global tree 
    global root 
    global pruned 
    i = 0 
    for child in branch: 
        if type(child) is list: 
            (nalpha, nbeta) = children(child, depth + 1, alpha, beta) 
            if depth % 2 == 1: 
                beta = nalpha if nalpha < beta else beta 
            else: 
                alpha = nbeta if nbeta > alpha else alpha 
            branch[i] = alpha if depth % 2 == 0 else beta 
            i += 1 
        else: 
            if depth % 2 == 0 and alpha < child: 
                alpha = child 
            if depth % 2 == 1 and beta > child: 
                beta = child 
            if alpha >= beta: 
                pruned += 1 
                break 
    if depth == root: 
        tree = alpha if root == 0 else beta 
    return (alpha, beta) 
def alphabeta(in_tree=tree, start=root, upper=-15, lower=15): 
    global tree
    global pruned 
    global root 
    (alpha, beta) = children(tree, start, upper, lower) 
 
    if __name__ == "__main__": 
        print ("(alpha, beta): ", alpha, beta) 
        print ("Result: ", tree) 
        print ("Times pruned: ", pruned) 
    return (alpha, beta, tree, pruned) 
if __name__ == "__main__": 
    alphabeta(None)

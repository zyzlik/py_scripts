# -*- coding: utf-8 -*-
coords = [[0,1,3,3],[2,2,6,4],[1,0,3,5],[7,2,8,3],[10,6,11,8]]

#Ищем саму левую координату x
def findLeft(coords):
	leftX = coords[0][0]
	for coord in coords:
		if leftX >= coord[0]:
			leftX = coord[0]
	return leftX

#Ищем самую правую координату x
def findRight(coords):
	rightX = coords[0][2]
	for coord in coords:
		if rightX < coord[2]:
			rightX = coord[2]	
	return rightX
#Сканируем, какая площадь занята между указанной координатой и следующей
def scanY(X):
	Ycoord = []
	S = 0
	for coord in coords:
		if X >= coord[0] and X < coord[2]:
			Ycoord.append(range(coord[1], coord[3]+1))
	if len(Ycoord) == 1:
		S += Ycoord[0][-1] - Ycoord[0][0]
	elif len(Ycoord) > 1:
		tmp = []
		for lst in Ycoord:
			for coord in lst:
				if coord not in tmp:
					tmp.append(coord)
					tmp.sort()
		for i in range(len(tmp)-1):
			if (tmp[i+1] - tmp[i]) == 1:
				S += 1
			else:
				continue
	return S

def main(coords):
	S = 0
	for X in range(findLeft(coords), findRight(coords) + 1):
		S += scanY(X)
	return S
		



print main(coords)
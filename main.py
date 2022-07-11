#by @ivantom
import math # we are importing math function to find the sqrt

data={'poid':[],'taille':[],'age':[],'note':[]}

data["poid"] = [45,50,50,60,60,60,70,65,60,65]

data["taille"] = [1.50,1.60,1.65,1.75,1.70,1.70,1.60,1.60,1.55,1.70]

data["age"] = [13,13,13,15,14,14,14,13,15,14]

data["note"] = [14,16,15,9,10,7,8,13,17,11]

def prettierDisplay(data):	
	title = list(data.keys())
	for i in title:
		print('%8s\t'%(i),end='')
	print()
	for i in range(len(data[title[0]])):
		for j in title:
			print('%8f\t'%(data[j][i]),end='')
		print()

def mean(arr):
	s=0
	for i in arr:
		s+=	i
	return (s/len(arr))

def var(arr):
	s = 0
	m = mean(arr)
	for i in arr:
		s += (i-m)**2
	return (s/len(arr))
	
def std(arr):
	return math.sqrt(var(arr))

def cov(arr1,arr2):
	m1 = mean(arr1)
	m2 = mean(arr2)
	n = len(arr1)

	s = 0
	for i in range(len(arr1)):
		s += (arr1[i]-m1)*(arr2[i]-m2)

	return s/n


def cor(arr1,arr2):
	return cov(arr1,arr2)/(std(arr1)*std(arr2))

# Displaying the data
prettierDisplay(data)
	
# Question 1 find the mean the variance and the standard deviation


Q1 = {"poid":{},"taille":{},"age":{},"note":{}}
Q1["poid"]["mean"] = mean(data["poid"])
Q1["poid"]["std"]=std(data["poid"])
Q1["poid"]["var"]=var(data["poid"])

Q1["taille"]["mean"] = mean(data["taille"])
Q1["taille"]["std"]=std(data["taille"])
Q1["taille"]["var"]=var(data["taille"])

Q1["age"]["mean"] = mean(data["age"])
Q1["age"]["std"]=std(data["age"])
Q1["age"]["var"]=var(data["age"])

Q1["note"]["mean"] = mean(data["note"])
Q1["note"]["std"]=std(data["note"])
Q1["note"]["var"]=var(data["note"])

print("\nQuestion 1")

for i in Q1.keys():
	print(i)
	for j in Q1[i].keys():
		print('%8s : %7f'%(j,Q1[i][j]))

Mcr = data
title = list(data.keys())
for i in title:
	M = mean(data[i])
	S = std(data[i])
	for j in range(len(data[i])):
		# print(Mcr[i][j],M)
		Mcr[i][j] = (Mcr[i][j]-M)/S

print('\n')
print("Q2 center and reduce the matrix : \n")
# print(Mcr)

prettierDisplay(Mcr)

output = [[0]*4]*4

out = [[0]*4]*4

correlationMatrix = {}

for (row_index,i) in enumerate(data.keys()):
	correlationMatrix[i] = {}
	for (col_index,j) in enumerate(data.keys()):
		 correlationMatrix[i][j] = 0


for (row_index,i) in enumerate(data.keys()):
	for (col_index,j) in enumerate(data.keys()):

		out[row_index][col_index] = cor(data[i],data[j])
		correlationMatrix[i][j] = out[row_index][col_index]

print('\nQ3 Correlation Matrix : \n')
for k in correlationMatrix.keys():
	for i in correlationMatrix[k].keys():
		print('%f'%(round(correlationMatrix[k][i],4)),end='\t')
	print('\n')

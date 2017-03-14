#Dado un numero (i), escribir un programa que genera \n
#un diccionario que contenga (i,I*i).\n
#  (1:1,2:4,3:9,4:16)
from IPython.core.display import clear_output

u=1
nums=[]
nums2=[]
while u>=1:
    #clear_output()
    nums = []
    nums2 = []
    a = input('Numero= ')
    if a>0:
        for i in range(1,a+1,1):
            nums.append(i)
    print nums
    for x in range(0,len(nums),1):
        nums2.append(nums[x]**2)
    print nums2
    dic=dict(zip(nums,nums2))
    print dic
    u=input('Desea ingresar otro numero= (1=Si , 0=No)')

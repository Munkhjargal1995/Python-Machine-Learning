#a = [1,2,3,4,5,6,7] #0-6 index ni des dugaar
#a.append(13) #araasn element nemne
#a.insert(2,5) #2 dah index deer 5 iig oruulj bn
#a.remove(2)
#print(a)
#a.clear() # list iig tsewerlej bn
#print(a)
#==============================Range haruulah===========================
#doloohonog = ['Monday','Sunday','Wednesday','Thursday','Friday','Saturday','Sunday']
#print(doloohonog[1:4]) # 1deh indexees 3 index hurtel elementiig haruulj bn
#print(doloohonog[:3]) # ehnii 3 elementiig haruulj
#print(doloohonog[2:]) # 2 dah indexees aragshaa buh elementiig

#==============================List Copy=================================
#======================ingej copy hiihgui=======================
#print(doloohonog)
#week = doloohonog
#print(week)
#doloohonog[0] = "CSharp"
#print(doloohonog,week, sep="\n")

#===================Copy=======================
#print(doloohonog)
#week = doloohonog.copy()
#print(week)
#week[0] = 'Python'
#print(doloohonog,week,sep="\n")

#========================If and Loop===========================

#jims = ['Алим','Банана','Тарвас','Усан үзэм','Киви']
#if 'Банана' in jims: # Банана == Банана
#    print("Banana bna")
#else:
#    print("Banana baihgui")    
#for jimsnuud in jims:  for jimsnuud in range(1,jims,1)  
#    print(jimsnuud)
#========================== listuudiig holboh======================
#ist1 = ['a','b','c','d','e']
#list2 = [2,3,4,5,6,7,33]
#list3 = ['aa','ee','ii']
#list4 = list1+list2+list3
#print(list4)

#list1 = ['dog','cat','bird','elephant','lion']
#list2 = [3,15,27,1,8,9]
#for x in list2:
#    list1.append(x)
#print(list1)


#list1 = ['Bmw','Honda','Pruis','Land Cruiser']
#list_2 = [3,2,54,4543,65,346,5346,654,64]
#list_2.extend(list1)
#print(list_2)


#letters = ['a','b','c','d','e']
#letters[0] = 'A'
#print(letters)
#print(letters[::2])

#numbers = list(range(20+1)) 
#print(numbers)
#print(numbers[::2])

#numb = [1,2,3,4,5,6,11]
#hooson = []
#for x in numb:
#    hooson.append(x**2)   #kwadrat zeregt dewshuulj bn numb iin elementuudiig(hooson listiig utgaar duurgej bn)
#print(numb)
#print(hooson)

# deerhtei adil dawtalt ashiglan nemj bn
#hooson = [x**2 for x in numb]
#print(hooson)

#numb = [1,2,3,4,5,6,11]
#hooson = []
#for x in range(6,0,-1): 
#    numb.append(x**2)
#print(numb)
#numb[0] = "Mongol"
#print(numb)

tegsh = [2,4,1,3,6,7]
sum = 0
for x in tegsh:
    if x%2==0:
        sum=sum+x
print(sum)






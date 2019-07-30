'''
def fun(x,y):
	return x+y
fun1 = lambda x,y:x+y
print(fun(10,20))
print(fun1(10,20))
print(type(fun))
print(type(fun1))

def check(x):
	if x%2==0:
		return "even"
	else:
		return "odd"

def check(x):
	return "even" if x%2==0 else "odd"
c1 = lambda x:"even" if x%2==0 else "odd"

'''

'''
l=[1,2,3,4,5]
#["1-->odd","2-->even","3-->odd","4-->even","5-->odd"]
res=[]
for i in l:
	if i%2==0:
		res.append(f"{i}-->Even")
	else:
		res.append(f"{i}--> odd")
print(res)
'''

'''
l=[1,2,3,4,5]
res = [i+10 for i in l]

res=[f"{i}-->even" if i%2==0 else f"{i}-->odd" for i in l]
print(res)
'''
'''
l=[1,2,3,4,5]
res=(f"{i}-->even" if i%2==0 else f"{i}-->odd" for i in l)
print(res)
for j in res:
	print(j)
'''




'''
fun = lambda x:"even" if x%2==0 else "odd"
l=[1,2,3,4]

for i in l:
	print(fun(i))
'''

'''
fun = lambda x:"even" if x%2==0 else "odd"
l=[1,2,3,4]
res = map(fun,l)
print(list(res))
'''
'''
l=[1,2,3,4]
res = map(lambda x:"even" if x%2==0 else "odd",l)
print(list(res))
'''
'''
l=[1,2,3,4]
res = filter(lambda x:"even" if x%2==0 else "odd",l)
print(list(res))

'''
'''
l=[1,2,3,4]
res = map(lambda x:x%2==0,l)
print(list(res))
'''
'''
l=[1,2,3,4]
res = filter(lambda x:x%2==0,l)
print(list(res))
'''
'''
l=[10,-20,-30,4,5,-60]
print(list(filter(lambda x:x>0,l)))
'''
'''
def fun(x):
	return x
y=fun
y(10)
'''
# monkey patching..
d={"name":"sdfsd","age":20}
_ = d.get
print(_("name"))



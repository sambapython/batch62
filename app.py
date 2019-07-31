def fun(x,y):
	if not isinstance(x,(int,float)):
		x=str(x)
		y=str(y)

	if not isinstance(y,(int,float)):
		y=str(y)
		x=str(x)
	return x+y
'''
fun(10,20) -->30
fun(10,'str2')-->10str2
fun("str1",20)-->str120
fun('str1','str2')-->str1str2
'''
import logging
#logging.info("program started")
logging.basicConfig(level=logging.DEBUG,
	filename="log.txt",
	format="%(asctime)s=>%(levelname)s->%(name)s==>%(message)s")
print("welcome")
logging.info("program started")
a=input("enter a value:")
logging.info("a value entered")
b=input("Enter b value:")
logging.info("b value entered")
logging.debug(f"before conversion:a={a},b={b}")
try:
	a=float(a)
	logging.info("a value converted")
	b=float(b)
	logging.info("b value coinverted")
	logging.debug(f"after conversion:a={a},b={b}")
	res=a/b
	print("result=",res)
	logging.debug("Result=%s"%res)
except ValueError as err:
	logging.error(err)
	print("expecting digits only")
except ZeroDivisionError as err:
	logging.error(err)
	print("b !=0")
logging.info("program execytion completed..")
print("thanks")
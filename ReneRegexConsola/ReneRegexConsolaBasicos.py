import re



def getS(cant):
	se="\n"
	for i in range(cant):
		se+="\t"
	return se
s0=getS(0)
s1=getS(1)
s2=getS(2)
s3=getS(3)
s4=getS(4)
r=""
def pr(texto):
	global r
	r+=texto
def pr0(texto):
	global s0
	pr(s0+str(texto))
def pr1(texto):
	global s1
	pr(s1+str(texto))
def pr2(texto):
	global s2
	pr(s2+str(texto))
def pr3(texto):
	global s3
	pr(s3+str(texto))
def pr4(texto):
	global s4
	pr(s4+str(texto))
a=""
def setA(texto):
	global a
	a=texto
def append(texto):
	global a
	a+=texto


class MangerRegex:
	def __init__(self):
		self.patron=None
		self.claseCreadorDeArgumentos=None# class ([][]findall) y sus atributos almacenan los grupos procesados

mng=MangerRegex()
def setP(patron):
	mng.patron=patron
def setC(claseCreadorDeArgumentos):
	mng.claseCreadorDeArgumentos=claseCreadorDeArgumentos

def rec(metodo):
	for l in a.split('\n'):
		p=re.compile(mng.patron)
		f=re.findall(p,l)
		#print(f)
		if(len(f)>0):
			
			metodo(mng.claseCreadorDeArgumentos(f))

def r0(metodo):
	rec(lambda mn:pr0(metodo(mn)))
def r1(metodo):
	rec(lambda mn:pr1(metodo(mn)))
def r2(metodo):
	rec(lambda mn:pr2(metodo(mn)))
def r3(metodo):
	rec(lambda mn:pr3(metodo(mn)))
def r4(metodo):
	rec(lambda mn:pr4(metodo(mn)))


def mostrar():
	global r;
	print(r)
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
	global r
	r+=texto

def rec(metodo):
	for l in a.split('\n'):
		#print(l)
		#p=re.compile(r"((?:[[]]|[]]|[a-zA-ZñÑ_<>,?])+)(?:(?:[^\w]|_)*)([a-zA-ZñÑ_]+)(?:[;])")
		#private static String facultad = "";
		p=re.compile(r"(?:(?:[^\w]|_)*)([a-zA-ZñÑ_]+)(?:(?:[^\w]|_)*)([a-zA-ZñÑ_]+)(?:(?:[^\w]|_)*)((?:[[]]|[]]|[a-zA-ZñÑ_<>,?])+)(?:(?:[^\w]|_)*)([a-zA-ZñÑ_]+)(?:(?:[^\w]|_)*)[=]")
		#print("paso")
		#p=re.compile(r"(\w*)[=]")
		f=re.findall(p,l)
		#print(f)
		if(len(f)>0):
			#nombreV=f[0]
			print(f)
			tipoV=f[0][2]
			nombreV=f[0][3]
			nombreP=nombreV[0:1].lower()+nombreV[1:]
			nombreU=nombreV[0:1].upper()+nombreV[1:]
			metodo(tipoV,nombreV,nombreP,nombreU)

			#metodo("",nombreV,"","")
def r0(metodo):
	rec(lambda tipoV,nombreV,nombreP,nombreU:pr0(metodo(tipoV,nombreV,nombreP,nombreU)))
def r1(metodo):
	rec(lambda tipoV,nombreV,nombreP,nombreU:pr1(metodo(tipoV,nombreV,nombreP,nombreU)))
def r2(metodo):
	rec(lambda tipoV,nombreV,nombreP,nombreU:pr2(metodo(tipoV,nombreV,nombreP,nombreU)))
def r3(metodo):
	rec(lambda tipoV,nombreV,nombreP,nombreU:pr3(metodo(tipoV,nombreV,nombreP,nombreU)))
def r4(metodo):
	rec(lambda tipoV,nombreV,nombreP,nombreU:pr4(metodo(tipoV,nombreV,nombreP,nombreU)))

def ra(metodo):
	rec(lambda tipoV,nombreV,nombreP,nombreU:append(metodo(tipoV,nombreV,nombreP,nombreU)))

setA("""
    private static String nombre = "";
    private static String facultad = "";
    private static String carrera = "";

    private static String descripcion = "";
    private static int curso=1;
    private static int semestre=1;
		
""")


# pr1("public DirectoriosPrestablecidos(")

r3(lambda tipoV,nombreV,nombreP,nombreU:"%s %s,"%(tipoV,nombreV))
# pr3("){");
# r3(lambda tipoV,nombreV,nombreP,nombreU:"this.%s=%s;"%(nombreV,nombreV))
# # r3(lambda tipoV,nombreV,nombreP,nombreU:"this.%s=null;"%(nombreV))
# pr3("}");
# print("asd")
# ra(lambda tipoV,nombreV,nombreP,nombreU:nombreV+",")
# print("ccc")


print(r)
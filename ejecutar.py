from ReneRegexConsola.ReneRegexConsolaBasicos import *





setP(r"[,](\w+)")
class MngPatrones:
	def __init__(self,f):
		self.texto=f[0]
setC(MngPatrones)


setA("""
	,Direccion_Imagenes_Procesadas
                   ,Direccion_Imagenes_Originales
                   ,Nombre
                   ,Descripcion
                   ,CantidadDeImagenes
                   ,Fruto
	""");

#r0(lambda mng:",%s=%s"%(mng.texto,mng.texto))
#r0(lambda mng:"let %s=r.content.%s;"%(mng.texto,mng.texto))
# r0(lambda mng:str(type(mng))+"  "+str(mng))


ra()

mostrar()










# setP(r"['](?!['])(.*)[']")
# class MngPatrones:
# 	def __init__(self,f):
# 		self.texto=f[0]
# setC(MngPatrones)


# setA("""
# 	d['nombreImagen']=args.nombreImagen
#             d['nombreCarpetaPadre'] = args.nombreCarpetaPadre
#             d['indiceDeCarpeta'] = args.indiceDeCarpeta
#             d['indiceDeImagenEnCarpeta'] = args.indiceDeImagenEnCarpeta
#             d['indiceImagen'] = args.indiceImagen
#             d['porcientoDeImagenConRespectoAlTotal'] = args.porcientoDeImagenConRespectoAlTotal
#             d['porcientoDeImagenConRespectoAlaCarpeta'] = args.porcientoDeImagenConRespectoAlaCarpeta
#             d['porcientoDeCarpeta'] = args.porcientoDeCarpeta
#             d['cantidadTotalDeImagenes'] = args.cantidadTotalDeImagenes
#             d['cantidadTotalDeImagenesEnEstaCarpeta'] = args.cantidadTotalDeImagenesEnEstaCarpeta
#             d['indiceDeFaseDeImagen'] = args.indiceDeFaseDeImagen
#             d['cantidadTotalDeFasesDeImagen'] = args.cantidadTotalDeFasesDeImagen
#             d['progresoDeFasesDeImagen'] = args.progresoDeFasesDeImagen
# 	""");

# r0(lambda mng:"let %s=r.content.%s;"%(mng.texto,mng.texto))
# # r0(lambda mng:str(type(mng))+"  "+str(mng))


# mostrar()

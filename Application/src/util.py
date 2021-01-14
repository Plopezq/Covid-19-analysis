# coding=utf-8

# Usage:
# from util import *
# u = Util()
# print(u.getCCAA('segovia').nombre_ISO)
# print(u.getCCAA('ceuta').nombre_ISO)
# print(u.getCCAA('madrid').nombre_ISO)

class CCAA:
	# no distinction between CCAA and Autonomous Cities
	nombre = None
	nombre_ISO = None

	def __init__(self, nombre, nombre_ISO):
		self.nombre = nombre
		self.nombre_ISO = nombre_ISO

class Util:

	an = CCAA('andalucia', 'Andalucía')
	ar = CCAA('aragon', 'Aragón')
	ast = CCAA('asturias', 'Asturias') # 'as' is reserved
	cn = CCAA('canarias', 'Canarias')
	cb = CCAA('cantabria', 'Cantabria')
	cl = CCAA('castilla y leon', 'Castilla y León')
	cm = CCAA('castilla-la mancha', 'Castilla-La Mancha')
	ct = CCAA('catalunya', 'Cataluña')
	ex = CCAA('extremadura', 'Extremadura')
	ga = CCAA('galicia', 'Galicia')
	ib = CCAA('islas baleares', 'Islas Baleares')
	ri = CCAA('la rioja', 'La Rioja')
	md = CCAA('comunidad de madrid', 'Comunidad de Madrid')
	mc = CCAA('murcia', 'Región de Murcia')
	nc = CCAA('navarra', 'Navarra')
	pv = CCAA('pais vasco', 'País Vasco')
	vc = CCAA('comunidad valenciana', 'Comunidad Valenciana')

	ce = CCAA('ceuta', 'Ceuta')
	ml = CCAA('melilla', 'Melilla')

	tn = CCAA('total nacional', 'Total Nacional')

	ce = CCAA('ceuta', 'Ceuta')
	ml = CCAA('melilla', 'Melilla')

	dict = {
		'total nacional' : tn,
		'alava' : pv, 'araba/alava' : pv,
		'albacete' : cm,
		'alicante' : vc, 'alicante/alacant' :vc,
		'almeria' : an,
		'asturias' : ast,
		'avila' : cl,
		'badajoz' : ex,
		'barcelona' : ct,
		'burgos' : cl,
		'caceres' : ex,
		'cadiz' : an,
		'cantabria' : cb,
		'castellon' : vc, 'castellon/castello' : vc,
		'ciudad real' : cm,
		'cordoba' : an,
		'la coruña' : ga, 'corunya, a' : ga,
		'cuenca' : cm,
		'gerona' : ct, 'girona' : ct,
		'granada' : an,
		'guadalajara' : cm,
		'guipuzcoa' : pv, 'gipuzkoa' : pv,
		'huelva' : an,
		'huesca' : ar,
		'baleares' : ib, 'balears, illes' : ib,
		'jaen' : an,
		'leon' : cl,
		'lerida' : ct, 'lleida' : ct,
		'lugo' : ga,
		'madrid' : md,
		'malaga' : an,
		'murcia' : mc,
		'navarra' : nc,
		'orense' : ga, 'ourense' : ga,
		'palencia' : cl,
		'las palmas' : cn, 'palmas, las' : cn,
		'pontevedra' : ga,
		'la rioja' : ri, 'rioja, la' : ri,
		'salamanca' : cl,
		'segovia' : cl,
		'sevilla' : an,
		'soria' : cl,
		'tarragona' : ct,
		'santa cruz de tenerife' : cn,
		'teruel' : ar,
		'toledo' : cm,
		'valencia' : vc, 'valencia/valencia': vc,
		'valladolid' : cl,
		'vizcaya' : pv, 'bizkaia' : pv,
		'zamora' : cl,
		'zaragoza' : ar,
		# TODO ceuta and melilla
		'ceuta' : ce,
		'melilla': ml
	}

	def getCCAA(self, provincia):
		if provincia not in self.dict:
			return CCAA('ERROR ' + provincia, 'ERROR ' + provincia)
		else:
			return self.dict[provincia.lower()]

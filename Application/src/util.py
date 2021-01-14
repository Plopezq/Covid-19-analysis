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

	dict = {
		'alava' : pv, 'araba/alava' : pv,
		'albacete' : cm,
		'alicante' : vc,
		'almeria' : an,
		'asturias' : ast,
		'avila' : cl,
		'badajoz' : ex,
		'barcelona' : ct,
		'burgos' : cl,
		'cáceres' : ex,
		'cádiz' : an,
		'cantabria' : cb,
		'castellón' : vc,
		'ciudad real' : cm,
		'córdoba' : an,
		'la coruña' : ga,
		'cuenca' : cm,
		'gerona' : ct,
		'granada' : an,
		'guadalajara' : cm,
		'guipúzcoa' : pv,
		'huelva' : an,
		'huesca' : ar,
		'baleares' : ib,
		'jaén' : an,
		'león' : cl,
		'lérida' : ct,
		'lugo' : ga,
		'madrid' : md,
		'málaga' : an,
		'murcia' : mc,
		'navarra' : nc,
		'orense' : ga,
		'palencia' : cl,
		'las palmas' : cn,
		'pontevedra' : ga,
		'la rioja' : ri,
		'salamanca' : cl,
		'segovia' : cl,
		'sevilla' : an,
		'soria' : cl,
		'tarragona' : ct,
		'santa cruz de tenerife' : cn,
		'teruel' : ar,
		'toledo' : cm,
		'valencia' : vc,
		'valladolid' : cl,
		'vizcaya' : pv,
		'zamora' : cl,
		'zaragoza' : ar
		# TODO ceuta and melilla
	}
	
	def getCCAA(self, provincia):
		if provincia not in self.dict:
			return CCAA('ERROR', 'ERROR')
		else:
			return self.dict[provincia.lower()]

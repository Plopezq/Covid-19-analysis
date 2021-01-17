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

	lista_CCAA = [ an, ar, ast, cn, cb, cl, cm, ct, ex, ga, ib, ri, md, mc, nc, nc, pv, vc, ce, ml, tn ]

	dict = {
		'total nacional' : tn,
		'alava' : pv, 'araba/alava' : pv, 'vi' : pv,
		'albacete' : cm, 'ab' : cm,
		'alicante' : vc, 'alicante/alacant' : vc, 'a' : vc,
		'almeria' : an, 'al' : an,
		'asturias' : ast, 'o' : ast,
		'avila' : cl, 'av' : cl,
		'badajoz' : ex, 'ba' : ex,
		'barcelona' : ct, 'b' : ct,
		'burgos' : cl, 'bu' : cl,
		'caceres' : ex, 'cc' : ex,
		'cadiz' : an, 'ca' : an,
		'cantabria' : cb, 's' : cb,
		'castellon' : vc, 'castellon/castello' : vc, 'cs' : vc,
		'ciudad real' : cm, 'cr' : cm,
		'cordoba' : an, 'co' : an,
		'la coruña' : ga, 'corunya, a' : ga, 'c' : ga,
		'cuenca' : cm, 'cu' : cm,
		'gerona' : ct, 'girona' : ct, 'gi' : ct,
		'granada' : an, 'gr' : an,
		'guadalajara' : cm, 'gu' : cm,
		'guipuzcoa' : pv, 'gipuzkoa' : pv, 'ss' : pv,
		'huelva' : an, 'h' : an,
		'huesca' : ar, 'hu' : ar,
		'baleares' : ib, 'balears, illes' : ib, 'pm' : ib,
		'jaen' : an, 'j' : an,
		'leon' : cl, 'le' : cl,
		'lerida' : ct, 'lleida' : ct, 'l' : ct,
		'lugo' : ga, 'lu' : ga,
		'madrid' : md, 'm' : md,
		'malaga' : an, 'ma' : an,
		'murcia' : mc, 'mu' : mc,
		'navarra' : nc, 'na' : nc,
		'orense' : ga, 'ourense' : ga, 'or' : ga,
		'palencia' : cl, 'p' : cl,
		'las palmas' : cn, 'palmas, las' : cn, 'gc' : cn,
		'pontevedra' : ga, 'po' : ga,
		'la rioja' : ri, 'rioja, la' : ri, 'lo' : ri,
		'salamanca' : cl, 'sa' : cl,
		'segovia' : cl, 'sg' : cl,
		'sevilla' : an, 'se' : an,
		'soria' : cl, 'so' : cl,
		'tarragona' : ct, 't' : ct,
		'santa cruz de tenerife' : cn, 'tf' : cn,
		'teruel' : ar, 'te' : ar,
		'toledo' : cm, 'to' : cm,
		'valencia' : vc, 'valencia/valencia': vc, 'v' : vc,
		'valladolid' : cl, 'va' :cl,
		'vizcaya' : pv, 'bizkaia' : pv, 'bi' : pv,
		'zamora' : cl, 'za' : cl,
		'zaragoza' : ar, 'z' : ar,
		'ceuta' : ce, 'ce' : ce,
		'melilla': ml, 'ml' : ml,
	}

	def getCCAA(self, provincia):
		if provincia not in self.dict:
			return CCAA('ERROR ' + provincia, 'ERROR ' + provincia)
		else:
			return self.dict[provincia.lower()]

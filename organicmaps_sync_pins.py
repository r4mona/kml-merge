# Organicmaps sync pins

# abgeglichene pins in orte1 einfügen (ImportNode)
# orte1 speichern
# schauen ob es in organic maps funkioniert
# parameter fuer inputdatein (kml dataien)
				 #referenzpunkte
				 #radius

import math
from xml.dom import minidom

def abstand_referenzpunkt_pin(n, e):
	return math.sqrt((referenzpunkt_n - n) ** 2 + (referenzpunkt_o - e) **2)

def get_coordinates(placemark):
	coordin = placemark.getElementsByTagName('coordinates')
	c = coordin[0]
	temp_c = c.firstChild.data
	return temp_c

file = minidom.parse('orte.kml')
file_abgleichen = minidom.parse("orte1.kml")
umkreis_km = 0.075 
im_umkreis = []
im_umkreis_weitergeben = []
liste_placem_abgleichen = []
referenzpunkt_n = 2.3353633
referenzpunkt_o = 48.867903
placem = file.getElementsByTagName('Placemark')
placem_abgleichen = file_abgleichen.getElementsByTagName("Placemark")

for i in placem:
	temp_c = get_coordinates(i)
	temp_c = temp_c.split(",")
	pins_n = float(temp_c [0])
	pins_e = float(temp_c [1])
	abstand = abstand_referenzpunkt_pin(pins_n, pins_e)
	if abstand <= umkreis_km:
		im_umkreis.append(i)

for x in placem_abgleichen:
	temp_c_placm_abgleichen = get_coordinates(x)
	
	liste_placem_abgleichen.append(temp_c_placm_abgleichen)

for p in im_umkreis:
	temp_c_im_umkreis = get_coordinates(p)

	if temp_c_im_umkreis not in liste_placem_abgleichen:
		im_umkreis_weitergeben.append(p)

	print("weitergeben:", len(im_umkreis_weitergeben))
	print("imUmkreis:", len(im_umkreis))













#print(im_umkreis)
#print(len(im_umkreis))
#print(len(placem))




#	
#
#if abstand < 5:
#	im_umkreis.append(pin)





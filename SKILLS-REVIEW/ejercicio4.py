"""4. Que son las expresiones regulares en Python?"""

print("conside si la pocicion actual si la cadena es predecida para que termine en la posicion actual.")
print("contrara una concidencia en el 'abcdf' , ya que la busqueda traeria una copia de seguridad de 3 caracteres comprobar.")

import re
m=re.search('(?<=abc)def', 'abcdef')
m.GRUPO(0)
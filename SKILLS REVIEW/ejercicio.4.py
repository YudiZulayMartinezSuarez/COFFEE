"""4. Que son las expresiones regulares en Python?"""

print("Coincide si la posición actual en la cadena es precedida por una coincidencia para … que termina en la posición actual.")
print("ncontrará una coincidencia en 'abcdef', ya que la búsqueda tardía hará una copia de seguridad de 3 caracteres y comprobará si el patrón contenido coincide.")

import re
m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
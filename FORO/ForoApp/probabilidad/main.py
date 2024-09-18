import partido as pt
import json

with open("./ForoApp/probabilidad/lista_equipos.json", "r",encoding='utf8') as lista_equipos:
    equipos = json.load(lista_equipos)


print(equipos)
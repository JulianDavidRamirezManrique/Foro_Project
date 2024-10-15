import partido as pt
import json
import Equipo as eq
with open("./ForoApp/probabilidad/lista_equipos.json", "r",encoding='utf8') as lista_equipos:
    equipos = json.load(lista_equipos)


once_caldas=eq.Equipo(equipos[0]["club"],equipos[0]["PJ"],equipos[0]["GTriunfos"],equipos[0]["EEmpates"],equipos[0]["PDerrotas"],equipos[0]["GF"],equipos[0]["GC"],equipos[0]["PtsPuntos"])
america=eq.Equipo(equipos[1]["club"],equipos[1]["PJ"],equipos[1]["GTriunfos"],equipos[1]["EEmpates"],equipos[1]["PDerrotas"],equipos[1]["GF"],equipos[1]["GC"],equipos[1]["PtsPuntos"])
tolima=eq.Equipo(equipos[2]["club"],equipos[2]["PJ"],equipos[2]["GTriunfos"],equipos[2]["EEmpates"],equipos[2]["PDerrotas"],equipos[2]["GF"],equipos[2]["GC"],equipos[2]["PtsPuntos"])
fortaleza=eq.Equipo(equipos[3]["club"],equipos[3]["PJ"],equipos[3]["GTriunfos"],equipos[3]["EEmpates"],equipos[3]["PDerrotas"],equipos[3]["GF"],equipos[3]["GC"],equipos[3]["PtsPuntos"])
atl_nacional=eq.Equipo(equipos[4]["club"],equipos[4]["PJ"],equipos[4]["GTriunfos"],equipos[4]["EEmpates"],equipos[4]["PDerrotas"],equipos[4]["GF"],equipos[4]["GC"],equipos[4]["PtsPuntos"])
millonarios=eq.Equipo(equipos[5]["club"],equipos[5]["PJ"],equipos[5]["GTriunfos"],equipos[5]["EEmpates"],equipos[5]["PDerrotas"],equipos[5]["GF"],equipos[5]["GC"],equipos[5]["PtsPuntos"])
pasto=eq.Equipo(equipos[6]["club"],equipos[6]["PJ"],equipos[6]["GTriunfos"],equipos[6]["EEmpates"],equipos[6]["PDerrotas"],equipos[6]["GF"],equipos[6]["GC"],equipos[6]["PtsPuntos"])
santa_fe=eq.Equipo(equipos[7]["club"],equipos[7]["PJ"],equipos[7]["GTriunfos"],equipos[7]["EEmpates"],equipos[7]["PDerrotas"],equipos[7]["GF"],equipos[7]["GC"],equipos[7]["PtsPuntos"])
aguilas=eq.Equipo(equipos[8]["club"],equipos[8]["PJ"],equipos[8]["GTriunfos"],equipos[8]["EEmpates"],equipos[8]["PDerrotas"],equipos[8]["GF"],equipos[8]["GC"],equipos[8]["PtsPuntos"])
junior=eq.Equipo(equipos[9]["club"],equipos[9]["PJ"],equipos[9]["GTriunfos"],equipos[9]["EEmpates"],equipos[9]["PDerrotas"],equipos[9]["GF"],equipos[9]["GC"],equipos[9]["PtsPuntos"])
la_equidad=eq.Equipo(equipos[10]["club"],equipos[10]["PJ"],equipos[10]["GTriunfos"],equipos[10]["EEmpates"],equipos[10]["PDerrotas"],equipos[10]["GF"],equipos[10]["GC"],equipos[10]["PtsPuntos"])
dep_pereira=eq.Equipo(equipos[11]["club"],equipos[11]["PJ"],equipos[11]["GTriunfos"],equipos[11]["EEmpates"],equipos[11]["PDerrotas"],equipos[11]["GF"],equipos[11]["GC"],equipos[11]["PtsPuntos"])
bucaramanga=eq.Equipo(equipos[12]["club"],equipos[12]["PJ"],equipos[12]["GTriunfos"],equipos[12]["EEmpates"],equipos[12]["PDerrotas"],equipos[12]["GF"],equipos[12]["GC"],equipos[12]["PtsPuntos"])
alianza=eq.Equipo(equipos[13]["club"],equipos[13]["PJ"],equipos[13]["GTriunfos"],equipos[13]["EEmpates"],equipos[13]["PDerrotas"],equipos[13]["GF"],equipos[13]["GC"],equipos[13]["PtsPuntos"])
patriotas=eq.Equipo(equipos[14]["club"],equipos[14]["PJ"],equipos[14]["GTriunfos"],equipos[14]["EEmpates"],equipos[14]["PDerrotas"],equipos[14]["GF"],equipos[14]["GC"],equipos[14]["PtsPuntos"])
medellin=eq.Equipo(equipos[15]["club"],equipos[15]["PJ"],equipos[15]["GTriunfos"],equipos[15]["EEmpates"],equipos[15]["PDerrotas"],equipos[15]["GF"],equipos[15]["GC"],equipos[15]["PtsPuntos"])
dep_cali=eq.Equipo(equipos[16]["club"],equipos[16]["PJ"],equipos[16]["GTriunfos"],equipos[16]["EEmpates"],equipos[16]["PDerrotas"],equipos[16]["GF"],equipos[16]["GC"],equipos[16]["PtsPuntos"])
jaguares=eq.Equipo(equipos[17]["club"],equipos[17]["PJ"],equipos[17]["GTriunfos"],equipos[17]["EEmpates"],equipos[17]["PDerrotas"],equipos[17]["GF"],equipos[17]["GC"],equipos[17]["PtsPuntos"])
boyaca_chico=eq.Equipo(equipos[18]["club"],equipos[18]["PJ"],equipos[18]["GTriunfos"],equipos[18]["EEmpates"],equipos[18]["PDerrotas"],equipos[18]["GF"],equipos[18]["GC"],equipos[18]["PtsPuntos"])
envigado=eq.Equipo(equipos[19]["club"],equipos[19]["PJ"],equipos[19]["GTriunfos"],equipos[19]["EEmpates"],equipos[19]["PDerrotas"],equipos[19]["GF"],equipos[19]["GC"],equipos[19]["PtsPuntos"])

tabla = [once_caldas,america,tolima,fortaleza,atl_nacional,millonarios,pasto,santa_fe,aguilas,junior,la_equidad,dep_pereira,bucaramanga,alianza,patriotas,medellin,dep_cali,jaguares,boyaca_chico,envigado]

for equipos in tabla:
    if equipos.partidos_jugados != equipos.partidos_ganados+equipos.partidos_empatados+equipos.partidos_perdidos or equipos.puntos != equipos.partidos_ganados*3+equipos.partidos_empatados:    
        print("Los datos son incorrectos")
        print(equipos)
tabla_ordenada = sorted(tabla, key=lambda x: x.puntos, reverse=True)

for equipos in tabla_ordenada:
    print(equipos.club, equipos.posicion(tabla_ordenada), equipos.puntos)
  

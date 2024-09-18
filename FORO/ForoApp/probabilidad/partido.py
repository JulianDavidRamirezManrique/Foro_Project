import random as r

def partido(local, visitante,caso):
    
    if caso == 1:
        goles_local = r.randint(1,5)
        goles_visitante = r.randint(0,goles_local-1)
        local.goles_a_favor+=goles_local
        visitante.goles_en_contra+=goles_local
        visitante.goles_a_favor+=goles_visitante
        local.goles_en_contra+=goles_visitante
        local.partidos_ganados+=1
        visitante.partidos_perdidos+=1
        local.puntos+=3

    if caso == 2:
        goles_visitante = r.randint(1,5)
        goles_local = r.randint(0,goles_visitante-1)
        local.goles_a_favor+=goles_local
        visitante.goles_en_contra+=goles_local
        visitante.goles_a_favor+=goles_visitante
        local.goles_en_contra+=goles_visitante
        visitante.partidos_ganados+=1
        local.partidos_perdidos+=1
        visitante.puntos+=3

    if caso == 3:
        goles_local = r.randint(0,5)
        goles_visitante = goles_local
        local.goles_a_favor +=goles_local
        visitante.goles_en_contra +=goles_local
        visitante.goles_a_favor+=goles_visitante
        local.goles_en_contra+=goles_visitante
        local.partidos_empatados+=1
        visitante.partidos_empatados+=1
        local.puntos+=1
        visitante.puntos+=1
    
    

    
    return (f"{local.club} {goles_local} - {goles_visitante} {visitante.club}")
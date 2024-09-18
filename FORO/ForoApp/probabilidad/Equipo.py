class Equipo:
    def __init__(self, club, partidos_jugados, partidos_ganados, partidos_empatados, partidos_perdidos, goles_a_favor, goles_en_contra,puntos):
        self.club = club
        self.partidos_jugados = partidos_jugados
        self.partidos_ganados = partidos_ganados
        self.partidos_empatados = partidos_empatados
        self.partidos_perdidos = partidos_perdidos
        self.goles_a_favor = goles_a_favor
        self.goles_en_contra = goles_en_contra
        self.puntos = puntos
        

    def __str__(self):
        return f"{self.club} - {self.puntos}"
    
    def __repr__(self):
        return f"{self.club} - {self.puntos}"
    
    def posicion(self,tabla):
        return tabla.index(self) + 1
       
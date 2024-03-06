SELECT
    h.AñoMundial,
    h.PaisOrganizador,
    h.PaisCampeon,
    h.Goles,
    h.Goleador,
    h.NacionalidadGoleador,
    h.Arquero,
    h.NacionalidadArquero,
    h.Mascota,
    e.Estadio,
    e.Pais AS PaisEstadio
FROM HistoricoMundiales h
INNER JOIN EstadioMundial e ON h.AñoMundial = e.AñoMundial
ORDER BY h.AñoMundial;

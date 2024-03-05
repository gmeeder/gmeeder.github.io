CREATE TABLE INNER4 AS
SELECT 
    EstadioMundial.Campeon, 
    HistoricoMundiales.AñoMundial, 
    HistoricoMundiales.PaisOrganizador, 
    HistoricoMundiales.Goleador, 
    HistoricoMundiales.NacionalidadGoleador
FROM 
    EstadioMundial
INNER JOIN (
    SELECT 
        AñoMundial, 
        PaisOrganizador, 
        Goleador, 
        NacionalidadGoleador
    FROM 
        HistoricoMundiales
    GROUP BY 
        AñoMundial, 
        PaisOrganizador, 
        Goleador, 
        NacionalidadGoleador
) AS HistoricoMundiales
ON 
    EstadioMundial.AñoMundial = HistoricoMundiales.AñoMundial;

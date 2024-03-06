SELECT *
FROM HistoricoMundiales
LEFT JOIN EstadioMundial ON HistoricoMundiales.AñoMundial = EstadioMundial.AñoMundial;

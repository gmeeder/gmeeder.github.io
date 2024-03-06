SELECT *
FROM HistoricoMundiales
RIGHT JOIN EstadioMundial ON HistoricoMundiales.AñoMundial = EstadioMundial.AñoMundial;

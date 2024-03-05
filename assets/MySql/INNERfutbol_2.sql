CREATE TABLE INNERfutbol AS
SELECT EstadioMundial.*, HistoricoMundiales.*
FROM EstadioMundial
INNER JOIN HistoricoMundiales ON EstadioMundial.AñoMundial = HistoricoMundiales.AñoMundial;

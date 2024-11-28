--Script de listar eventos
DELIMITER //
CREATE PROCEDURE ListarEventosPorLocal(IN id_local INT)
BEGIN
    SELECT E.id_evento, E.nome, E.descricao, E.tipo, E.data_inicio, E.data_fim
    FROM Eventos E
    WHERE E.id_local = id_local;
END //
DELIMITER ;

CALL ListarEventosPorLocal(1); -- Listar eventos na Igreja Central

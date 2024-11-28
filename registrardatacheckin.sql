-- Script para registrar data e hora s no checkin
DELIMITER //

CREATE TRIGGER registrardatacheckin
AFTER INSERT ON Presencas
FOR EACH ROW
BEGIN
    -- Atualiza a presença com a data e hora do check-in
    IF NEW.check_in_online THEN
        UPDATE Presencas
        SET check_in_online = NOW()
        WHERE id_presenca = NEW.id_presenca;
    END IF;
END //

DELIMITER ;

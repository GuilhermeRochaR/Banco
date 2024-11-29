DELIMITER //

CREATE TRIGGER ImpedirEventoSemLocal
BEFORE INSERT ON eventos
FOR EACH ROW
BEGIN
    IF NEW.id_local IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'O evento deve ser associado a um local.';
    END IF;
END //

DELIMITER ;

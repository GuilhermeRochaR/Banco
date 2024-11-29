DELIMITER //

CREATE TRIGGER VerificarDataFimEvento
BEFORE INSERT ON eventos
FOR EACH ROW
BEGIN
    IF NEW.data_fim < NEW.data_inicio THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A data de término não pode ser anterior à data de início.';
    END IF;
END //

DELIMITER ;

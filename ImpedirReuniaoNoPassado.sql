DELIMITER //

CREATE TRIGGER ImpedirReuniaoNoPassado
BEFORE INSERT ON reunioes
FOR EACH ROW
BEGIN
    IF NEW.data_inicio < NOW() THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A data de início da reunião não pode ser no passado.';
    END IF;
END //

DELIMITER ;

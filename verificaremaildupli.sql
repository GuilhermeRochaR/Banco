--Script de verificar email duplicado
DELIMITER //

CREATE TRIGGER verificaremaildupli
BEFORE INSERT ON Membros
FOR EACH ROW
BEGIN
    -- Verifica se o e-mail já existe na tabela Membros
    IF EXISTS (SELECT 1 FROM Membros WHERE email = NEW.email) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'E-mail já está registrado!';
    END IF;
END //

DELIMITER ;

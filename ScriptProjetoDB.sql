DROP DATABASE IF EXISTS IGREJA;
CREATE DATABASE IF NOT EXISTS Igreja;
USE Igreja;

CREATE TABLE IF NOT EXISTS Membros (
    id_membro INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    telefone VARCHAR(20),
    endereco LONGTEXT,
    data_nascimento DATE,
    data_entrada DATE,
    senha VARCHAR(255);
    nivel_acesso ENUM('Administrador', 'Líder de Ministério', 'Membro Regular') DEFAULT 'Membro Regular'
);


CREATE TABLE IF NOT EXISTS membro_responsavel (
id_responsavel INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nome VARCHAR(100),
email VARCHAR(100) UNIQUE,
telefone VARCHAR(20),
endereco TEXT,
data_nascimento DATE,
data_entrada DATE,
senha VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS Ministerio (
id_ministerio INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nome VARCHAR(100),
descricao TEXT,
id_membro INT NOT NULL,
id_responsavel INT NOT NULL,
FOREIGN KEY (id_membro) REFERENCES Membros(id_membro),
FOREIGN KEY (id_responsavel) REFERENCES membro_responsavel(id_responsavel)
);


CREATE TABLE IF NOT EXISTS Locais (
    id_local INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco LONGTEXT,
    capacidade INT,
    descricao LONGTEXT
);

CREATE TABLE IF NOT EXISTS Eventos (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao LONGTEXT,
    tipo VARCHAR(100),
    data_inicio DATETIME NOT NULL,
    data_fim DATETIME,
    id_local INT,
    FOREIGN KEY (id_local) REFERENCES Locais(id_local)
);

CREATE TABLE IF NOT EXISTS Reunioes (
    id_reuniao INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao LONGTEXT,
    tipo VARCHAR(100),
    tipo_reuniao ENUM('Regular', 'Extraordinária') DEFAULT 'Regular',
    data_inicio DATETIME NOT NULL,
    data_fim DATETIME,
    id_ministerio INT,
    id_local INT,
    FOREIGN KEY (id_ministerio) REFERENCES Ministerios(id_ministerio),
    FOREIGN KEY (id_local) REFERENCES Locais(id_local)
);

CREATE TABLE IF NOT EXISTS Presencas (
    id_presenca INT AUTO_INCREMENT PRIMARY KEY,
    id_membro INT NOT NULL,
    id_evento INT,
    id_reuniao INT,
    check_in_online BOOLEAN,
    FOREIGN KEY (id_membro) REFERENCES Membros(id_membro),
    FOREIGN KEY (id_evento) REFERENCES Eventos(id_evento),
    FOREIGN KEY (id_reuniao) REFERENCES Reunioes(id_reuniao)
);

DELIMITER //
CREATE PROCEDURE RegistrarPresenca(IN id_membro INT, IN id_evento INT, IN id_reuniao INT, IN check_in BOOLEAN)
BEGIN
    INSERT INTO Presencas (id_membro, id_evento, id_reuniao, check_in_online) 
    VALUES (id_membro, id_evento, id_reuniao, check_in);
END //
DELIMITER ;

INSERT INTO Membros (nome, email, telefone, endereco, data_nascimento, data_entrada, nivel_acesso)
VALUES
('José Vicente', 'josevicente@email.com', '98912345678', 'Rua Grande, 123, Centro, São Luís, MA', '2000-01-15', CURDATE(), 'Administrador'),
('Yan Garrido', 'yangarrido@email.com', '98923456789', 'Avenida Litorânea, 456, Calhau, São Luís, MA', '2001-05-22', CURDATE(), 'Líder de Ministério'),
('Luis Guilherme', 'luisguilherme@email.com', '98934567890', 'Rua Portugal, 789, Praia Grande, São Luís, MA', '2002-08-10', CURDATE(), 'Membro Regular'),
('Luis Magno', 'luismagno@email.com', '98945678901', 'Rua São Pantaleão, 321, Madre Deus, São Luís, MA', '2003-11-30', CURDATE(), 'Membro Regular'),
('Marcos André', 'marcosandre@email.com', '98956789012', 'Avenida dos Holandeses, s/n, Olho d’Água, São Luís, MA', '2004-02-18', CURDATE(), 'Líder de Ministério'),
('João', 'joao@email.com', '98967890123', 'Rua das Hortas, 1001, Centro, São Luís, MA', '2000-09-10', CURDATE(), 'Membro Regular'),
('Juan', 'juan@email.com', '98978901234', 'Avenida Guajajaras, 10, São Cristóvão, São Luís, MA', '2001-03-25', CURDATE(), 'Membro Regular');

INSERT INTO Locais (nome, endereco, capacidade, descricao)
VALUES
('Igreja Central', 'Rua da Paz, 101, Centro, São Luís, MA', 200, 'Local de culto principal'),
('Igreja Filial', 'Avenida Brasil, 202, Cohab, São Luís, MA', 100, 'Local para encontros menores'),
('Auditório', 'Rua do Sol, 303, Centro, São Luís, MA', 150, 'Auditório para eventos e reuniões');

INSERT INTO Ministerios (nome, descricao, id_membro)
VALUES
('Ministério de Adoração', 'Responsável pela música e louvor da igreja', 1),
('Ministério Infantil', 'Ministério dedicado ao cuidado das crianças', 2),
('Ministério de Ensino', 'Responsável pelos estudos bíblicos e seminários', 3),
('Ministério de Oração', 'Grupo de oração pela igreja e pela comunidade', 4),
('Ministério de Louvor', 'Grupo responsável pelo louvor da igreja', 5),
('Ministério Jovem', 'Grupo de jovens para atividades e cultos especiais', 6);

INSERT INTO Eventos (nome, descricao, tipo, data_inicio, data_fim, id_local)
VALUES
('Culto de Adoração', 'Culto semanal para louvor e adoração', 'Culto', '2024-11-25 19:00:00', '2024-11-25 21:00:00', 1),
('Seminário de Liderança', 'Seminário sobre liderança cristã', 'Seminário', '2024-12-01 09:00:00', '2024-12-01 17:00:00', 2),
('Palestra sobre Família', 'Palestra com foco na educação familiar', 'Palestra', '2024-12-10 19:00:00', '2024-12-10 21:00:00', 1);

INSERT INTO Reunioes (nome, descricao, tipo, tipo_reuniao, data_inicio, data_fim, id_ministerio, id_local)
VALUES
('Reunião de Oração', 'Encontro semanal de oração', 'Reunião de oração', 'Regular', '2024-11-26 19:00:00', '2024-11-26 20:30:00', 1, 1),
('Reunião de Planejamento', 'Reunião de planejamento da equipe de eventos', 'Reunião de planejamento', 'Regular', '2024-11-29 09:00:00', '2024-11-29 12:00:00', 2, 2);

INSERT INTO Presencas (id_membro, id_evento, id_reuniao, check_in_online)
VALUES
(1, 1, NULL, false),
(2, 2, NULL, TRUE),
(3, 3, NULL, TRUE),
(4, 3, 1, FALSE),
(5, 1, NULL, TRUE),
(6, 2, 2, TRUE),
(7, 2, 1, TRUE);

SELECT * FROM Membros;
SELECT * FROM Locais;
SELECT * FROM Ministerios;
SELECT * FROM Eventos;
SELECT * FROM Reunioes;
SELECT * FROM Presencas;

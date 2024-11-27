CREATE DATABASE IF NOT EXISTS Igreja;
USE Igreja;

CREATE TABLE IF NOT EXISTS Membros (
id_membro INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nome VARCHAR(100),
email VARCHAR(100) UNIQUE,
telefone VARCHAR(20),
endereco TEXT,
data_nascimento DATE,
data_entrada DATE
);

CREATE TABLE IF NOT EXISTS Ministerio (
id_ministerio INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nome VARCHAR(100),
descrição TEXT,
id_membro INT NOT NULL,
FOREIGN KEY (id_membro) REFERENCES Membros(id_membro)
);

CREATE TABLE IF NOT EXISTS locais (
    id_local INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco TEXT,
    capacidade INT,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS eventos (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    tipo VARCHAR(100),
    data_inicio DATETIME NOT NULL,
    data_fim DATETIME,
    id_local INT,
    FOREIGN KEY (id_local) REFERENCES locais(id_local)
);

CREATE TABLE IF NOT EXISTS reunioes (
    id_reuniao INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    tipo VARCHAR(100),
    data_inicio DATETIME NOT NULL,
    data_fim DATETIME,
    id_ministerio INT,
    id_local INT,
    FOREIGN KEY (id_ministerio) REFERENCES ministerio(id_ministerio),
    FOREIGN KEY (id_local) REFERENCES locais(id_local)
);

-- Inserções na tabela de Membros
INSERT INTO Membros (nome, email, telefone, endereco, data_nascimento, data_entrada)
VALUES
('José Vicente', 'josevicente@email.com', '98912345678', 'Rua Grande, 123, Centro, São Luís, MA', '2000-01-15', CURDATE()),
('Yan Garrido', 'yangarrido@email.com', '98923456789', 'Avenida Litorânea, 456, Calhau, São Luís, MA,', '2001-05-22', CURDATE()),
('Luis Guilherme', 'luisguilherme@email.com', '98934567890', 'Rua Portugal, 789, Praia Grande, São Luís, MA', '2002-08-10', CURDATE()),
('Luis Magno', 'luismagno@email.com', '98945678901', 'Rua São Pantaleão, 321, Madre Deus, São Luís,MA', '2003-11-30', CURDATE()),
('Marcos André', 'marcosandre@email.com', '98956789012', 'Avenida dos Holandeses, s/n, Olho d’Água, São Luís, MA', '2004-02-18', CURDATE()),
('João', 'joao@email.com', '98967890123', 'Rua das Hortas, 1001, Centro, São Luís, MA', '2000-09-10', CURDATE()),
('Juan', 'juan@email.com', '98978901234', 'Avenida Guajajaras, 10, São Cristóvão, São Luís, MA', '2001-03-25', CURDATE());

-- Inserções na tabela de Locais
INSERT INTO Locais (nome, endereco, capacidade, descricao)
VALUES
('Igreja Central', 'Rua da Paz, 101, Centro, São Luís, MA', 200, 'Local de culto principal'),
('Igreja Filial', 'Avenida Brasil, 202, Cohab, São Luís, MA', 100, 'Local para encontros menores'),
('Auditório', 'Rua do Sol, 303, Centro, São Luís, MA', 150, 'Auditório para eventos e reuniões');



-- Inserções na tabela de Ministério (requer id_membro válido)
INSERT INTO Ministerio (nome, descrição, id_membro)
VALUES
('Ministério de Adoração', 'Responsável pela música e louvor da igreja', 1),  -- id_membro = 1
('Ministério Infantil', 'Ministério dedicado ao cuidado das crianças', 2),    -- id_membro = 2
('Ministério de Ensino', 'Responsável pelos estudos bíblicos e seminários', 3), -- id_membro = 3
('Ministério de Oração', 'Grupo de oração pela igreja e pela comunidade', 4),  -- id_membro = 4
('Ministério de Louvor', 'Grupo de oração pela igreja e pela comunidade', 5),  -- id_membro = 4
('Ministério de Louvor', 'Grupo de oração pela igreja e pela comunidade', 6);

-- Inserções na tabela de Eventos (requer id_local e id_tipo válidos)
INSERT INTO Eventos (nome, descricao,tipo, data_inicio, data_fim, id_local)
VALUES
('Culto de Adoração', 'Culto semanal para louvor e adoração','Culto', '2024-11-25 19:00:00', '2024-11-25 21:00:00', 1),
('Seminário de Liderança', 'Seminário sobre liderança cristã','Seminário', '2024-12-01 09:00:00', '2024-12-01 17:00:00', 2),
('Palestra sobre Família', 'Palestra com foco na educação familiar','Palestra', '2024-12-10 19:00:00', '2024-12-10 21:00:00', 1);

-- Inserções na tabela de Reuniões (requer id_ministerio, id_local e id_tipo válidos)
INSERT INTO Reunioes (nome, descricao,tipo, data_inicio, data_fim, id_ministerio, id_local)
VALUES
('Reunião de Oração', 'Encontro semanal de oração','Reunião de oração', '2024-11-26 19:00:00', '2024-11-26 20:30:00', 1, 1),
('Reunião de Planejamento', 'Reunião de planejamento da equipe de eventos','Reunião de planejamento', '2024-11-29 09:00:00', '2024-11-29 12:00:00', 2, 2);

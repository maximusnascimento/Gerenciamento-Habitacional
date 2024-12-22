CREATE TABLE ip.imoveis
(
    id_imovel INT IDENTITY(1,1) PRIMARY KEY,
    endereco NVARCHAR(255) NOT NULL,
    tipo NVARCHAR(50) NOT NULL,
    tamanho FLOAT NOT NULL,
    valor_aluguel DECIMAL(10, 2) NOT NULL
);

CREATE TABLE ip.proprietarios
(
    id_proprietario INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(255) NOT NULL,
    cpf_cnpj NVARCHAR(20) NOT NULL UNIQUE,
    contato NVARCHAR(255) NOT NULL
);

CREATE TABLE ip.inquilinos
(
    id_inquilino INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(255) NOT NULL,
    cpf NVARCHAR(14) NOT NULL UNIQUE,
    contato NVARCHAR(255) NOT NULL
);

CREATE TABLE ip.contratos
(
    id_contrato INT IDENTITY(1,1) PRIMARY KEY,
    id_imovel INT NOT NULL,
    id_inquilino INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_termino DATE NOT NULL,
    status NVARCHAR(50) NOT NULL,
    FOREIGN KEY (id_imovel) REFERENCES ip.imoveis(id_imovel),
    FOREIGN KEY (id_inquilino) REFERENCES ip.inquilinos(id_inquilino)
);

CREATE TABLE ip.pagamentos
(
    id_pagamento INT IDENTITY(1,1) PRIMARY KEY,
    id_contrato INT NOT NULL,
    data_pagamento DATE NOT NULL,
    valor_pago DECIMAL(10, 2) NOT NULL,
    status NVARCHAR(50) NOT NULL,
    FOREIGN KEY (id_contrato) REFERENCES ip.contratos(id_contrato)
);

CREATE TABLE ip.usuarios
(
    id_usuario INT IDENTITY(1,1) PRIMARY KEY,
    nome NVARCHAR(255) NOT NULL,
    email NVARCHAR(255) NOT NULL UNIQUE,
    senha NVARCHAR(255) NOT NULL
);



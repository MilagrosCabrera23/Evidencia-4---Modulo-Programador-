create database bd_esterilizador_uv;

  USE bd_esterilizador_uv; 
  
  CREATE TABLE Esterilizador_uv(
id_esterilizador int primary key, 
encendido bool not null, 
potencia int, 
ciclos_realizados int, 
modo varchar(10), 
estado_esterilizacion bool not null
);

 CREATE TABLE Historial_esterilizador(
id int primary key, 
id_esterilizador int, 
fecha_esterilizacion date, 
ciclos_realizados int, 
modo_esterilizacion varchar(10)
); 

INSERT INTO Esterilizador_uv (id_esterilizador, encendido, potencia, ciclos_realizados, modo, estado_esterilizacion) VALUES (1, TRUE, 10, 0, 'normal', FALSE);
INSERT INTO Esterilizador_uv (id_esterilizador, encendido, potencia, ciclos_realizados, modo, estado_esterilizacion) VALUES (2, FALSE, 20, 1, 'intenso', TRUE);
INSERT INTO Esterilizador_uv (id_esterilizador, encendido, potencia, ciclos_realizados, modo, estado_esterilizacion) VALUES (3, TRUE, 30, 2, 'normal', FALSE);
INSERT INTO Esterilizador_uv (id_esterilizador, encendido, potencia, ciclos_realizados, modo, estado_esterilizacion) VALUES (4, FALSE, 40, 3, 'intenso', TRUE);
INSERT INTO Esterilizador_uv (id_esterilizador, encendido, potencia, ciclos_realizados, modo, estado_esterilizacion) VALUES (5, TRUE, 50, 4, 'normal', FALSE);

INSERT INTO Historial_esterilizador (id, id_estelizador, fecha_esterilizacion, ciclos_realizados, modo_esterilizacion) VALUES (1, 1, '2021-01-01', 0, 'normal'); 
INSERT INTO Historial_esterilizador (id, id_estelizador, fecha_esterilizacion, ciclos_realizados, modo_esterilizacion) VALUES (2, 2, '2022-01-05', 1, 'intenso');
INSERT INTO Historial_esterilizador (id, id_estelizador, fecha_esterilizacion, ciclos_realizados, modo_esterilizacion) VALUES (3, 3, '2023-01-10', 2, 'normal');
INSERT INTO Historial_esterilizador (id, id_estelizador, fecha_esterilizacion, ciclos_realizados, modo_esterilizacion) VALUES (4, 4, '2024-01-15', 3, 'intenso');
INSERT INTO Historial_esterilizador (id, id_estelizador, fecha_esterilizacion, ciclos_realizados, modo_esterilizacion) VALUES (5, 5, '2019-01-20', 4, 'normal');

SELECT * FROM Esterilizador_uv; 
SELECT * FROM  Historial_esterilizador; 
SELECT * FROM Esterilizador_uv WHERE encendido = TRUE; 
SELECT * FROM  Historial_esterilizador where id_esterilizador = 1; 
SELECT * FROM Historial_esterilizador WHERE modo_esterilizacion = 'intenso'; 
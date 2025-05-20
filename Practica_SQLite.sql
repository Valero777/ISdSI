CREATE TABLE MATERIAS(
id INT DEFAULT NULL,
nombre VARCHAR(30) DEFAULT NULL,
grado INT DEFAULT NULL
);

INSERT INTO MATERIAS (id,nombre,grado) Values
(1,'Talleres',8),
(2,'Cienciasn Sociales',7),
(3,'CSdSI',6),
(4,'Con_Energia',8),
(5,'Pe_Mat',6),
(6,'Ing',9),
(7,'Soc_Emo',7),
(8,'ISdSI',8),
(9,'DSdSI',8),
(10,'Ly C',7);

UPDATE TABLE alumnos 
SET id=9
where id=1,
Delete from alumnos
(id,nombre,grado) Values
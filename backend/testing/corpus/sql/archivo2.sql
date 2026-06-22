
-- Uso de datos estáticos mediante una tabla temporal

CREATE TEMPORARY TABLE productos (
    id INT,
    nombre VARCHAR(50)
);

INSERT INTO productos (id, nombre) VALUES
(1, 'Teclado'),
(2, 'Ratón'),
(3, 'Monitor');

SELECT id, nombre FROM productos;

SELECT COUNT(*) AS total_productos FROM productos;


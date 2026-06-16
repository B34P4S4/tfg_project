-- patrón vulnerable típico almacenado
INSERT INTO logs (query) VALUES ('SELECT * FROM users WHERE id=' + input);
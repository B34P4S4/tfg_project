CREATE TABLE serialized_cache(
    id INT,
    payload TEXT
);

INSERT INTO serialized_cache
VALUES(
    1,
    @serialized_object
);
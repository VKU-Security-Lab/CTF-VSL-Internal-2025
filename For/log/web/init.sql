CREATE TABLE greetings (
    id SERIAL PRIMARY KEY,
    message VARCHAR(255)
);

INSERT INTO greetings (message) VALUES ('Hello, World!');

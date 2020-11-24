CREATE DATABASE datarepresentation;

USE datarepresentation;

CREATE TABLE movies(
    movieid INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(250),
    director VARCHAR(250),
    releaseyear INT,
    tomatoescore INT,
    PRIMARY KEY (movieid)
);
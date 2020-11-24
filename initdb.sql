CREATE DATABASE datarepresentation;

USE datarepresentation;

-- Create Movie Table
CREATE TABLE movies(
    movieid INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(250),
    director VARCHAR(250),
    releaseyear INT,
    tomatoescore INT,
    PRIMARY KEY (movieid)
);

-- Create Cast Table
CREATE TABLE moviecast(
    castid INT NOT NULL AUTO_INCREMENT,
    movieid INT,
    actor VARCHAR(250),
    rating INT,
    PRIMARY KEY (castid)
);
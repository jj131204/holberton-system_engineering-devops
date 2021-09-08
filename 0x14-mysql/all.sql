-- punto 0
        -- install mysql

-- punto 1

CREATE USER  IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

GRANT ALL PRIVILEGES ON * . * TO 'holberton_user'@'localhost';

-- punto2

CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- INSERT INTO tyrell_corp(


USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(
        id INT DEFAULT 1,
        name VARCHAR(256)
);

INSERT INTO nexus6 (name) VALUES ('Leon');


-- punto 3

CREATE USER  IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica';

GRANT REPLICATION SLAVE  ON   * . * TO 'replica_user'@'%';

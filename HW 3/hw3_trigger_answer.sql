DROP TRIGGER IF EXISTS develop_insert;
DROP TRIGGER IF EXISTS develop_update;
DROP TRIGGER IF EXISTS develop_delete;
DELIMITER $$

CREATE TRIGGER develop_insert
AFTER INSERT ON developer
FOR EACH ROW
BEGIN
INSERT INTO developer_log
VALUES("name", "", new.name);
INSERT INTO developer_log(attr, old_value, new_value)
VALUES("headquarters", "", new.headquarters);
END $$

CREATE TRIGGER develop_update
AFTER UPDATE ON developer
FOR EACH ROW
BEGIN
IF (new.name != old.name and new.headquarters != old.headquarters) THEN
INSERT INTO developer_log
VALUES("name", old.name,new.name);
INSERT INTO developer_log
VALUES("headquarters", old.headquarters, new.headquarters);
ELSE
IF (new.name != old.name) THEN
INSERT INTO developer_log
VALUES("name", old.name, new.name);
END IF;
IF (new.headquarters != old.headquarters) THEN
INSERT INTO developer_log
VALUES("headquarters", old.headquarters, new.headquarters);
END IF;
END IF;
END $$

CREATE TRIGGER develop_delete
AFTER DELETE ON developer
FOR EACH ROW
BEGIN
INSERT INTO developer_log
VALUES("name", old.name, "");
INSERT INTO developer_log
VALUES("headquarters", old.headquarters, "");
END $$

DELIMITER ;
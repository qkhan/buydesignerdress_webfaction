PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "items_country" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "country" varchar(250) NOT NULL);
INSERT INTO "items_country" VALUES(1,'Australia');
INSERT INTO "items_country" VALUES(2,'Pakistan');
INSERT INTO "items_country" VALUES(3,'Canada');
COMMIT;

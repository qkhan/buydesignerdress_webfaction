PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "items_prospect" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "prospect" varchar(250) NOT NULL);
INSERT INTO "items_prospect" VALUES(1,'Kids');
INSERT INTO "items_prospect" VALUES(2,'Ladies');
INSERT INTO "items_prospect" VALUES(3,'Men');
COMMIT;

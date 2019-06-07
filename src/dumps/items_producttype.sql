PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "items_producttype" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "productType" varchar(250) NOT NULL);
INSERT INTO "items_producttype" VALUES(1,'Accessories');
INSERT INTO "items_producttype" VALUES(2,'Shoes');
INSERT INTO "items_producttype" VALUES(3,'Clothing');
COMMIT;

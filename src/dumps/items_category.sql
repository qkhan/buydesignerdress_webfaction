PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "items_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "categoryName" varchar(250) NOT NULL, "lookAndTrend" bool NOT NULL, "featured" bool NOT NULL, "productType_id" integer NOT NULL REFERENCES "items_producttype" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "items_category" VALUES(13,'KAMEEZ SHALWAR',0,1,3);
INSERT INTO "items_category" VALUES(15,'UNSTITCHED',0,0,3);
INSERT INTO "items_category" VALUES(17,'FORMAL DRESS',1,0,3);
INSERT INTO "items_category" VALUES(19,'SHIRT',0,1,3);
INSERT INTO "items_category" VALUES(20,'FORMAL SHOES',1,0,2);
INSERT INTO "items_category" VALUES(21,'CASUAL FOOTWEAR',1,0,2);
INSERT INTO "items_category" VALUES(22,'FRAGRENCES',0,1,1);
CREATE INDEX "items_category_productType_id_1bb8124a" ON "items_category" ("productType_id");
COMMIT;

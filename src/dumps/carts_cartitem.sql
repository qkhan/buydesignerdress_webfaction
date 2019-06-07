PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "carts_cartitem" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "quantity" integer unsigned NOT NULL, "item_id" integer NOT NULL REFERENCES "items_item" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "carts_cartitem_item_id_6644202d" ON "carts_cartitem" ("item_id");
COMMIT;

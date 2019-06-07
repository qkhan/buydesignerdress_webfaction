PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "items_item" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "slug" varchar(50) NOT NULL UNIQUE, "sku" varchar(100) NULL, "title" varchar(120) NOT NULL, "price" decimal NOT NULL, "updated" datetime NOT NULL, "timestamp" datetime NOT NULL, "active" bool NOT NULL, "added_by_id" integer NULL REFERENCES "accounts_myuser" ("id") DEFERRABLE INITIALLY DEFERRED, "brandID_id" integer NULL REFERENCES "items_brand" ("id") DEFERRABLE INITIALLY DEFERRED, "categoryID_id" integer NOT NULL REFERENCES "items_category" ("id") DEFERRABLE INITIALLY DEFERRED, "countryID_id" integer NOT NULL REFERENCES "items_country" ("id") DEFERRABLE INITIALLY DEFERRED, "last_edited_by_id" integer NULL REFERENCES "accounts_myuser" ("id") DEFERRABLE INITIALLY DEFERRED, "prospectID_id" integer NULL REFERENCES "items_prospect" ("id") DEFERRABLE INITIALLY DEFERRED, "size" varchar(15) NOT NULL, "cartDesc" varchar(120) NULL, "featured" bool NOT NULL, "fitting" text NULL, "height_field" integer NOT NULL, "image1" varchar(100) NULL, "image2" varchar(100) NULL, "image3" varchar(100) NULL, "image4" varchar(100) NULL, "image5" varchar(100) NULL, "image6" varchar(100) NULL, "itemLimited" bool NOT NULL, "live" bool NOT NULL, "location" varchar(250) NULL, "longDesc" text NULL, "materialAndCare" text NULL, "shortDesc" varchar(250) NULL, "stock" decimal NOT NULL, "weight" decimal NOT NULL, "width_field" integer NOT NULL, "thumb_image" varchar(100) NULL, "color_id" integer NULL REFERENCES "items_color" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "items_item" VALUES(2,'blue-kameez-kurta','J-01070703','Blue Kameez Kurta',150,'2018-11-24 04:05:34.484763','2018-06-30 01:26:08.267643',1,1,4,13,1,NULL,3,'S,L','Blue Kurta',0,'<p>Slim Fit</p>',1110,'items/1/1_EPDy3VS.jpg','items/1/1_2wfvLn7.jpg','items/1/1_JZ5y1or.jpg','items/1/1_oXAGPui.jpg','items/1/1_2zEKoK2.jpg','items/1/1_oBCBC5p.jpg',1,1,NULL,'<p>More Information</p>

<p>Color: MID NIGHT BLUE</p>

<p>Collection: Eid ul Fiter &nbsp;2018</p>

<p>Fabric: CVC/Chief Value Cotton</p>

<p>Product category: Men Kameez shalwar</p>

<p>Fit Type: Regular</p>','<p>Pure Cotton</p>

<p>&nbsp;</p>','<p>Semi-Formal Kurta For Men Stylized With Printed Collar And Placket.</p>',0,11,864,'items/1/1_HmDavzm.jpg',7);
INSERT INTO "items_item" VALUES(3,'brown-kameez-kurta','J-01070611','Brown Kameez Kurta',145,'2018-07-06 00:12:01.007164','2018-06-30 01:31:32.958194',1,1,4,13,1,NULL,3,'S,XL','Dark Brown Shalwar Kameez',0,'<p>Slim Fit</p>',1110,'items/3/3_0ltqjuC.jpg','items/3/3_UWxtChV.jpg','items/3/3_YdQ7xug.jpg','items/3/3_VNnPh8o.jpg','items/3/3_tylweZv.jpg','items/3/3_KoRLQ4A.jpg',0,1,NULL,'<ul>
	<li><strong>Color:&nbsp;</strong>DARK BROWN</li>
	<li><strong>Collection:&nbsp;</strong>Eid ul Fiter Collection 2018</li>
	<li><strong>Fabric:&nbsp;</strong>CVC/Chief Value Cotton</li>
	<li><strong>Product category:&nbsp;</strong>Men Kameez shalwar</li>
	<li><strong>Fit Type:&nbsp;</strong>Smart</li>
</ul>','<p>Pure Cotton</p>','<p>Casual Suit For Men Designed With Cut &amp; Sew Details On Collar, Placket &amp; Cuff Used Contrast Applique</p>',4,12,864,'items/3/3_140Br3J.jpg',9);
INSERT INTO "items_item" VALUES(4,'blue-unstitched-suit','01071815-2MT-054','Blue Unstitched Suit',70,'2018-07-06 00:14:29.493287','2018-06-30 01:44:45.432698',1,1,4,15,1,NULL,3,'S,M,L,XL,XXL','Blue Cotton Un-Stitched Piece',1,'',1110,'items/4/4_ePZtXzZ.jpg','items/4/4_ZvD2AuL.jpg','items/4/4_S8bn6EG.jpg','items/4/4_PRWPRgJ.jpg','items/4/4_ggHTaDH.jpg','items/4/4_5PbTO1t.jpg',0,1,NULL,'<ul>
	<li>Size: 2.5 MTR</li>
	<li>Color: Blue</li>
	<li>Collection: Eid ul Fiter Collection 2018</li>
	<li>Fabric: Cotton</li>
	<li>Product category: Men Unstitched Fabric</li>
</ul>','',NULL,5,5,864,'items/4/4_qL16Qtn.jpg',7);
INSERT INTO "items_item" VALUES(5,'yellow-striped-shirt','BRM-458','YELLOW STRIPED SHIRT',100,'2018-06-30 01:59:47.172728','2018-06-30 01:59:47.172774',1,1,4,19,1,NULL,3,'S,M,L,XL,XXL','YELLOW STRIPED SHIRT',0,'<p>Slim Fit</p>',2400,'items/5/5_6TymA9Q.jpg','items/5/5_O70R8Sw.jpg','items/5/5_p7kScGg.jpg','items/5/5_hfVzuyZ.jpg','items/5/5_iEj0omY.jpg','items/5/5_FCDG9EK.jpg',0,1,NULL,'<p>This yellow stripe shirt features diamond weaved pattern on 100% cotton fabric . Featuring contrasting collar ribbon, classic shallow collar &amp; front pocket. Idea for business wear.</p>','<p>100% Cotton.</p>','<p>This yellow stripe shirt features diamond weaved pattern on 100% cotton fabric .&nbsp;</p>',5,3,1800,'items/5/5_rUe90Oe.jpg',13);
INSERT INTO "items_item" VALUES(6,'giorgio-armani-code-colonia','B01N9OJLD5','Giorgio Armani Code Colonia',158.7,'2018-06-30 02:25:00.235036','2018-06-30 02:20:15.715639',1,1,5,22,1,NULL,3,'NA','Giorgio Armani Code Colonia 4.2 oz For Men',0,'',1500,'items/7/7_cj0bqba.jpg','items/7/7_iHb3ETQ.jpg','items/6/6_PFq3KaO.jpg','items/7/7_sas5d6c.jpg','items/7/7_scO71IF.jpg','items/7/7_up7gmjB.jpg',0,1,NULL,'<p>In stock.</p>

<p>Get it as soon as&nbsp;Thursday, July 5&nbsp;-&nbsp;Tuesday, July 10&nbsp;when you choose&nbsp;Standard Delivery&nbsp;at checkout.</p>

<p>Ships from and sold by&nbsp;<a href="https://www.amazon.com.au/gp/help/seller/at-a-glance.html/ref=dp_merchant_link?ie=UTF8&amp;seller=A1N3JJ250RIZII">Price Rite Mart</a>.</p>

<ul>
</ul>

<ul>
	<li><strong>Product Dimensions:&nbsp;</strong>5.1 x 5.1 x 20.3 cm ; 454 g</li>
	<li><strong>Boxed-product Weight:</strong>&nbsp;422 g</li>
	<li><strong>Item Model Number:</strong>&nbsp;30-92420</li>
	<li><strong>ASIN:&nbsp;</strong>B01N9OJLD5</li>
	<li><strong>Date first available at Amazon.com.au:</strong>&nbsp;4 October 2017</li>
	<li><strong>Average Customer Review:</strong>&nbsp;<a href="https://www.amazon.com.au/review/create-review/ref=acr_dpproductdetail_solicit?ie=UTF8&amp;asin=B01N9OJLD5">Be the first to review this item</a></li>
</ul>','<p>Style Name:&nbsp;Giorgio Armani Code Colonia</p>

<ul>
	<li>An aromatic fougere fragrance for men</li>
	<li>Fresh, spicy, sweet, elegant and inviting</li>
	<li>Top notes of bergamot, mandarin and pink pepper</li>
</ul>','<p>Giorgio Armani For Men Giorgio Armani Code Colonia 4.2 oz</p>',3,10,422,'items/7/7_SwvtTke.jpg',7);
INSERT INTO "items_item" VALUES(7,'15-by-james','112211','15 by James',200,'2018-06-30 02:39:31.703997','2018-06-30 02:39:31.704029',1,1,6,20,1,NULL,3,'S,M,L,XL','15 by James',0,'',1200,'items/7/7_TPQmgAa.jpg','items/7/7_XrNXukR.jpg','items/7/7_bxXHr2T.jpg','items/7/7_8lGk5Gg.jpg','items/7/7_uxeUrAl.jpg','items/7/7_faipWmG.jpg',0,1,NULL,'<p>Shaken not stirred, the 15 by James is the perfect style to make a considerable impression. The sleek glossy patent-leather with grey linings is a refined touch&nbsp;to a formal outfit. Teamed with a classic tuxedo, they&#39;re guaranteed to add gravitas to your look.&nbsp;<br />
<br />
With a classic fit and elegant long vamp, our &#39;15&#39; last will add just the right amount of Italian flair to your look. Handcrafted with care in Portugal.</p>','<ul>
	<li>Leather</li>
</ul>','<p>Shaken not stirred, the 15 by James is the perfect style to make a considerable impression. The sleek glossy patent-leather with grey linings is a refined touch.</p>',10,12,1200,'items/7/7_KvzsN5n.jpg',10);
INSERT INTO "items_item" VALUES(8,'adidas-originals-by-alexander-wang','AQ1237','ADIDAS ORIGINALS BY ALEXANDER WANG',354,'2018-06-30 02:49:41.267103','2018-06-30 02:49:41.267134',1,1,7,21,1,NULL,3,'S,M,L,XL,XXL','ADIDAS ORIGINALS BY ALEXANDER WANG',0,'<p>Lining Composition:&nbsp;leather 100%</p>

<p>Outer Composition: leather 100%</p>

<p>Sole Composition:&nbsp;rubber 100%</p>

<p>Outer Composition:&nbsp;suede 100%</p>

<p>Outer Composition:&nbsp;nylon 100%</p>

<p>Lining Composition:&nbsp;nylon 100%</p>',640,'items/8/8_Ijpkeku.jpg','items/8/8_DEnKXGW.jpg','items/8/8_D4jAGxv.jpg','items/8/8_8SJYSAR.jpg','items/8/8_BEXW2Ec.jpg','items/8/8_FPemoaN.jpg',0,1,NULL,'<p>ADIDAS ORIGINALS BY ALEXANDER WANG</p>

<p>Revamp your streetwear style with iconic pieces from Adidas Originals by Alexander Wang.</p>

<p>The wang drop 3 unisex edit features in-out styles, all-over logo print and neutral colour palette.</p>

<p>Sleek clothing designs and statement footwear give the perfect sport luxe balance to this collection.</p>

<p>Discover our selection of&nbsp;<a href="https://www.farfetch.com/au/shopping/men/designer-adidas-by-raf-simons/shoes-2/items.aspx">Adidas by Raf Simons shoes&nbsp;</a>as well.</p>','<p>Designer Style ID:&nbsp;AQ1237</p>

<p>Colour:&nbsp;BLACK CHALK WHITE BOLD ORANGE</p>',NULL,15,10,480,'items/8/8_0sNbN3B.jpg',10);
INSERT INTO "items_item" VALUES(9,'maira-ahsan-embroidered-lawn-unstitched',NULL,'Maira Ahsan Embroidered Lawn Unstitched',110,'2018-07-02 06:58:46.510581','2018-06-30 02:58:35.232890',1,1,8,15,1,NULL,2,'NA','Maira Ahsan Embroidered Lawn Unstitched 3 Piece Suit',0,'<p>Size Chart</p>

<p>3 Piece Embroidered Unstitched Suits from Maira Ahsan Exclusive Designer Collection Vol</p>

<ul>
	<li><strong>Manufacturer:</strong>&nbsp;Maira Ahsan</li>
	<li><strong>Material:</strong>&nbsp;Lawn</li>
	<li><strong>Catalog:</strong>&nbsp;Maira Ahsan Exclusive Designer Collection Vol-3 2018</li>
</ul>',487,'items/9/9_AAB94bm.jpg','items/9/9_K0ondQU.jpg','items/9/9_4O1mgXq.jpg','items/9/9_ZNB7wkU.jpg','items/9/9_GOM7QUn.jpg','items/9/9_rgORNC6.jpg',0,1,NULL,'','<p><strong>3 Piece Embroidered Lawn Suit</strong></p>

<ul>
	<li>Shirt Front 1.25 Meter Embroidered</li>
	<li>Shirt Back 1.25 Meter Embroidered</li>
	<li>Sleeves 0.5 Meter Embroidered</li>
	<li>Trouser 2.5 Meter</li>
	<li>Digital Chiffon Dupatta 2.5 Meter</li>
</ul>','<p>Maira Ahsan Embroidered Lawn Unstitched 3 Piece Suit MA18-L3 1A - Eid Collection</p>',3,5,350,'items/9/9.jpg',2);
INSERT INTO "items_item" VALUES(10,'gulahmed-turquoise-springsummer-2017','CT # 200-136124','GulAhmed Turquoise Spring/Summer 2017',200,'2018-07-02 06:28:24.524601','2018-06-30 03:06:20.098161',1,1,9,19,1,NULL,2,'S,M,L','GulAhmed Turquoise Spring/Summer 2017',0,'',400,'items/11/11_IlwpqSh.jpg','items/11/11_Qs9tDrb.jpg','items/11/11_0YF1kwu.jpg','items/11/11_vyDpx21.jpg','items/11/11_4vvcwaP.jpg','items/11/11_6UrbgXq.jpg',0,0,NULL,'<p>GeneralBrandGulAhmed<br />
ReturnYes<br />
ExchangeYes<br />
SKUWOFGUL59ACCFFC99E5A<br />
VendorGULAHMED TEXTILES MILLS LIMITEDFeaturesWeight0.6500</p>','<p>Features:</p>

<p>Colour: Turquoise</p>

<p>Material: Printed Chantilly De Lace</p>

<p>Fabric Measurements: &nbsp;Embroidered</p>

<p>Chiffon Dupatta</p>

<ul>
	<li>2.5 meters</li>
</ul>

<p>Printed Shirt</p>

<ul>
	<li>2.5 meters</li>
</ul>

<p>Sleeves</p>

<ul>
	<li>0.65 meters</li>
</ul>

<p>Dyed Bottom</p>

<ul>
	<li>2.5 meters</li>
</ul>

<p>3 Piece Suit</p>

<p>Collection name: Premium Collection</p>','<p>GulAhmed Turquoise Spring/Summer 2017 Collection Printed Chantilly De Lace Suit - CT # 200-136124</p>',0,5,400,'items/11/11.jpg',7);
INSERT INTO "items_item" VALUES(11,'brown-female-kameez-shalwar','J-02038068','Brown Female Kameez Shalwar',230,'2018-07-06 00:14:01.732685','2018-06-30 03:21:00.427284',1,1,4,13,1,NULL,2,'M,L','J-02038068',1,'<p>Slim Fit</p>',1130,'items/11/11_c8VOtow.jpg','items/11/11_KKZCiKp.jpg','items/11/11_XjRNwJZ.jpg','items/11/11_FScBV7U.jpg','items/11/11_0AI3xkA.jpg','items/11/11_RKtXO3B.jpg',0,1,NULL,'<ul>
	<li>Color: Blue, Pink, Red</li>
	<li>Pieces: 3 Piece</li>
	<li>Collection&#39;&#39;: Eid ul Fiter Collection 2018</li>
	<li>Fabric: Viscose</li>
	<li>Product category: Ladies Pret</li>
</ul>','',NULL,22,22,880,'items/11/11_ZCfpv5l.jpg',9);
INSERT INTO "items_item" VALUES(12,'black-fantasy','150054','BLACK FANTASY',230,'2018-06-30 03:35:00.127319','2018-06-30 03:35:00.127484',1,1,10,17,1,NULL,2,'S,M,L','BLACK FANTASY',0,'',500,'items/12/12_CM9AYC3.jpeg','items/12/12_700oapz.jpeg','items/12/12_WH3iDtx.jpeg','items/12/12_sCKYOG6.jpeg','items/12/12_nowBBbW.jpeg','items/12/12_MJwsWkE.jpeg',0,1,NULL,'<p>Decorated with mesmerizing antique gold kora dabka and zardozi embellished neckline border and sleeves, our black embroidered angarkha will add glamour to your style.</p>

<p>*Actual colors of the outfit may vary from the colors being displayed on your device.</p>','<p>Dry clean only. Please read care label for detailed instructions.</p>',NULL,0,22,370,'items/12/12.jpeg',6);
INSERT INTO "items_item" VALUES(13,'bridal-sandal','0213-2-1733','BRIDAL SANDAL',400,'2018-11-17 02:35:00.083104','2018-06-30 03:44:49.804717',1,1,11,20,1,NULL,2,'S,M,L','Bridal Sandals – Bridal Shoes',0,'<p>Heel: 4&rdquo;</p>',800,'items/13/13_ehakuZG.jpg','items/13/13_f5HN5ab.jpg','items/13/13_ZD6C8nH.jpg','items/13/13_02cH9LF.jpg','items/13/13_bsd3iZq.jpg','items/13/13_gNfTPLG.jpg',0,1,NULL,'<p><strong>Bridal Sandals &ndash; Bridal Shoes</strong></p>

<p><strong>Bridal Sandals (Bridal Shoes)<u>: Ladies shoes in Pakistan:</u></strong>&nbsp;Shoes can be categorized as an item of fashion, styling, comfort, and safety. &nbsp;The design of a good shoe pair, slippers or sandals may differ as per culture, function, setting, and occasion. Fashion plays its part in terms of heels, straps and general styling. Shoes have evolved significantly and the conventional materials used now have many additions which include but not limited to as plastic and rubber, our&nbsp;<strong>ladies shoes in Pakistan</strong>&nbsp;can gratify this statement. We at&nbsp;<strong>English Boot House</strong>&nbsp;have something in all ranges and something that goes well with any attire. We are a one-stop shoe and leather accessories shop for you and your family.</p>

<p>Our commencement was back in 1947 and being the predecessors of the shoe market has given us a leverage to entertain and maintain a wide variety of customers over time and provide the finest&nbsp;<strong>Pakistani shoes</strong>&nbsp;and&nbsp;<strong>Karachi shoes</strong>. Our strong foundation and familiarity with the field help us bring out the best of the best for our loyal and potential customers. Ladies have a strong inclination towards the right footwear and their shoes and our offerings include<strong>&nbsp;Ladies shoes in Pakistan, Ladies slippers in Pakistan, Ladies sandals in Pakistan</strong>&nbsp;and&nbsp;<strong>bridal shoes in Pakistan</strong>. We are proud of our heritage and if you&rsquo;re looking for the finest&nbsp;<strong>Karachi shoes&nbsp;</strong>and&nbsp;<strong>Pakistani shoes</strong>; look no further.</p>

<p><strong>Ladies Shoes in Pakistan</strong></p>

<p><strong>Bridal Sandal (bridal shoes):</strong>&nbsp;Marriages hold a lot of magnitudes religiously, culturally and on an individual level.&nbsp; We offer comfortable, fancy and trendy shoes for your big day. Our motto is to prioritize on quality and comfort, so you can wear the shoes for a considerable amount of time. Our shoes are elegant, classy and economical so they look good and feel great. Just a few clicks and your shoes would be at your doorstep. So if you are about to walk the aisle or have to attend any event or occasion these shoes are meant for you.</p>','<p>Fancy rain shine bedded</p>','<p>Material/Type:&nbsp;Fancy rain shine bedded</p>

<p>Heel: 4&rdquo;</p>',0,22,600,'items/13/13.jpg',NULL);
INSERT INTO "items_item" VALUES(14,'summers-and-flowers','11222','Summers and flowers',300,'2018-06-30 03:52:04.609619','2018-06-30 03:52:04.609687',1,1,12,21,1,NULL,2,'S,M,L,XL','Summers and flowers - Pink Shoes',0,'<p>Shoe Size</p>

<p>Euro 36 (23cm), Euro 37 (23.5 cm), Euro 38 (24 cm), Euro 39 (24.5 cm), Euro 40 (25 cm), Euro 41 (26 cm), Euro 42 (26.5 cm), Euro 43 (27 cm)</p>',600,'items/14/14_3t8DyIq.jpg','items/14/14_Sbm3L7I.jpg','items/14/14_iGUYttx.jpg','items/14/14_aqKXHJO.jpg','items/14/14_emKIwmp.jpg','items/14/14_9wB8x7A.jpg',0,0,NULL,'<p>Summers and flowers. The best thing about summers is these bright blossoms. JuttiChoo has imprinted these summers blossoms on their Punjabi Juttis.&nbsp;These bright and bloomy floral designs will nourish your summer soul.&nbsp;And with the vibrant-versatile design, these pretty summer blooms will go with every single piece in your summer wardrobe. Stock on this irresistible floral collection. After all, Flowers are second most beautiful creation after women!</p>

<p>&nbsp;</p>','',NULL,0,22,600,'items/14/14.jpg',2);
INSERT INTO "items_item" VALUES(15,'chanel-eau-de-parfum','00011122254','Chanel - Eau de Parfum',245,'2018-11-24 03:42:58.792887','2018-06-30 03:57:16.363190',1,1,13,22,1,NULL,2,'M,L,XL','Chanel - Eau de Parfum',0,'',240,'items/15/15_iyLVhLB.jpg','items/15/15_0675dnQ.jpg','items/15/15_Fwu4wP2.jpg','items/15/15_K46qigE.jpg','items/15/15_mwPhwWn.jpg','items/15/15_ou270LE.jpg',0,0,NULL,'<p>Bleu de Chanel is a sophisticated and contemporary fragrance from Chanel that hit the market in 2010. Chanel introduces its enhanced version, Bleu de Chanel Eau de Parfum, in summer of 2014. The fragrance is dedicated to freedom&mdash;endless, deep and boundless.<br />
<br />
The woody-aromatic composition created by Jacques Polge follows the original path but goes down into a sensual and oriental amber territory. Wood maintains the freshness of the original in this variant, enriched with depth and velvet amber woods.<br />
<br />
The fragrance is available as 50 and 100 ml Eau de Parfum.</p>','',NULL,0,32,210,'items/16/16.jpg',7);
INSERT INTO "items_item" VALUES(16,'dynasty-boski-wash-n-wear-unstitched-shalwar-kameez-graphite-summer-collection','231561','Dynasty Boski Wash N Wear Unstitched Shalwar Kameez Graphite - Summer Collection',50,'2018-12-23 01:40:11.152378','2018-11-24 04:13:16.398580',1,1,14,15,1,NULL,3,'S,M,L','Black Plain Cotton Kurta For Men',0,'<p>4.5 Meter. 50/50 Wash n Wear Fabric</p>',927,'items/18/18_pjUj11q.jpg','items/18/18_ftHa1fB.jpg','items/18/18_YWqkvWs.jpg','items/18/18_iFglH5L.jpg','items/18/18_hYuoND7.jpg','items/18/18_OSj8GAf.jpg',0,1,NULL,'','<ul>
	<li>Wash N Wear</li>
</ul>','<ul>
	<li>Shalwar Kameez Boski Unstitched Suits from Dynasty Fabrics Summer Collection</li>
</ul>',1,1,666,'items/18/18_By29Alj.jpg',10);
INSERT INTO "items_item" VALUES(17,'new-product','17278','New PRODUCT',1999,'2018-12-15 05:14:32.806558','2018-12-15 05:14:32.806593',1,2,2,19,2,NULL,2,'M,L,XL','22',1,'<p>Testing4</p>',954,'items/17/17_3XOpgI6.jpg','items/17/17_5iYywcI.jpg','items/17/17_elyTEbW.jpg','items/17/17_SfZXhuT.jpg','items/17/17_V5w66xl.jpg','items/17/17_G7opdbT.jpg',1,0,'22','<p>sHkSHK</p>','<p>Testing2</p>','<p>Testing</p>',111,22,620,'items/17/17.jpg',3);
INSERT INTO "items_item" VALUES(18,'classic-jamawar-sherwani','120920920','Classic Jamawar Sherwani',90,'2018-12-23 04:39:08.090483','2018-12-23 04:30:24.021793',1,2,2,17,1,NULL,3,'S','Classic Jamawar Off-white Classic Fit Sherwani',0,'',80,'items/19/19_CANaPUO.jpg','items/19/19_lAtLwKw.jpg','items/19/19_dOb2N9x.jpg','items/19/19_4knf3qc.jpg','items/19/19_O2olRJB.jpg','items/19/19_kYWgNuh.jpg',0,0,NULL,'','','<p>Testing</p>',0,0,80,'items/19/19_6DS03bd.jpg',3);
INSERT INTO "items_item" VALUES(19,'formal-dress-image-1','1234-1111','Formal Dress Image 1',90,'2018-12-23 05:38:03.249331','2018-12-23 05:38:03.249361',1,2,16,17,1,NULL,3,'S,M,L',NULL,0,'',275,'items/19/19_EjxWS9H.jpeg','items/19/19_XuHQ9Py.jpeg','items/19/19_ovQy1OV.jpeg','items/19/19_nZN1U33.jpeg','items/19/19_ARF7flX.jpeg','items/19/19_YB9zpkw.jpeg',0,0,NULL,'','',NULL,0,0,183,'items/19/19.jpeg',10);
INSERT INTO "items_item" VALUES(20,'formal-dress-2','22111222','Formal Dress 2',90,'2018-12-23 05:43:12.184528','2018-12-23 05:43:12.184558',1,2,16,17,1,NULL,3,'S,M,L','Formal Dress Amir Adnan',0,'',275,'items/20/20_dSNWiGn.jpeg','items/20/20_365FjZP.jpeg','items/20/20_fdBbcoF.jpeg','items/20/20_0X9Yqd9.jpeg','items/20/20_HCl2NQ1.jpeg','items/20/20_bpLkXdv.jpeg',0,0,NULL,'','',NULL,0,9.97,183,'items/20/20.jpeg',10);
INSERT INTO "items_item" VALUES(21,'kids1',NULL,'Kids1',100,'2018-12-23 05:48:36.097867','2018-12-23 05:48:36.097898',1,2,4,19,1,NULL,1,'S,M,L',NULL,0,'',271,'items/21/21_s2auJUa.jpeg','items/21/21_E3xQPKG.jpeg','items/21/21_CsNnIv7.jpeg','items/21/21_Pp4lPwc.jpeg','items/21/21_8aKnLrJ.jpeg','items/21/21_8iRBmUC.jpeg',0,0,NULL,'','',NULL,0,0,186,'items/21/21.jpeg',NULL);
INSERT INTO "items_item" VALUES(22,'kids-shirt-2',NULL,'Kids shirt 2',90,'2019-01-12 01:51:21.305179','2018-12-23 05:50:13.778105',1,2,4,19,1,NULL,1,'S,M,L','Kids shirt 2',0,'',251,'items/22/22_aqUlXe2.jpeg','items/22/22_SdkPJt3.jpeg','items/22/22_ZJUgB3g.jpeg','items/22/22_3AseBgi.jpeg','items/22/22_9PBCoEP.jpeg','items/22/22_uzqNQDj.jpeg',0,0,NULL,'','','<p>This is new test</p>',0,0,201,'items/22/22.jpeg',NULL);
INSERT INTO "items_item" VALUES(23,'kids-3',NULL,'Kids 3',80,'2018-12-23 05:52:16.735910','2018-12-23 05:52:16.735943',1,2,3,19,1,NULL,1,'S,M,L','Kids 3',0,'',251,'items/23/23_ZFidz2a.jpeg','items/23/23_DOJ6Bgf.jpeg','items/23/23_LfADgBV.jpeg','items/23/23_8RCis9R.jpeg','items/23/23_l5iGMBG.jpeg','items/23/23_CPaKF4N.jpeg',0,0,NULL,'','',NULL,0,0,201,'items/23/23.jpeg',3);
CREATE INDEX "items_item_added_by_id_9e1522d1" ON "items_item" ("added_by_id");
CREATE INDEX "items_item_brandID_id_db9fc3c6" ON "items_item" ("brandID_id");
CREATE INDEX "items_item_categoryID_id_98750692" ON "items_item" ("categoryID_id");
CREATE INDEX "items_item_countryID_id_a68d3ae7" ON "items_item" ("countryID_id");
CREATE INDEX "items_item_last_edited_by_id_3a60c716" ON "items_item" ("last_edited_by_id");
CREATE INDEX "items_item_prospectID_id_096f2833" ON "items_item" ("prospectID_id");
CREATE INDEX "items_item_color_id_81918baf" ON "items_item" ("color_id");
COMMIT;

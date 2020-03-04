CREATE TABLE Saloane (
  numar_salon int,
  tip varchar(10) not null,
  nr_locuri int,
  PRIMARY KEY (numar_salon)
);

CREATE TABLE Asistenti (
  id_asistent int,
  nume varchar(30) not null,
  prenume varchar(30) not null,
  email varchar(50) not null unique,
  nr_telefon varchar(10) not null unique,
  data_angajare date,
  numar_salon int,
  PRIMARY KEY (id_asistent),
  FOREIGN KEY (numar_salon) references Saloane(numar_salon)
  ON DELETE CASCADE
);

CREATE TABLE  Sectii  (
   id_sectie varchar(20),
   denumire varchar(100) not null,
   etaj int,
  PRIMARY KEY (id_sectie)
);

CREATE TABLE Medici (
   id_medic int,
   Nume varchar(30) not null,
   Prenume varchar(30) not null,
   email varchar(50) not null unique,
   nr_telefon varchar(10) not null unique,
   Varsta int,
   id_sectie varchar(20),
   PRIMARY KEY (id_medic),
   FOREIGN KEY (id_sectie) references Sectii(id_sectie)
   ON DELETE CASCADE
   
);

CREATE TABLE Tratamente (
  id_tratament varchar(10),
  denumire varchar(100) not null,
  cantitate int,
  PRIMARY KEY (id_tratament)
);
CREATE TABLE Diagnostice (
  id_diagnostic varchar(10),
  denumire varchar(200) not null,
  id_tratament varchar(10),
  PRIMARY KEY (id_diagnostic),
  FOREIGN KEY (id_tratament) references Tratamente(id_tratament)
  ON DELETE SET NULL
);
CREATE TABLE Pacienti (
  id_pacient int,
  Nume varchar(30) not null,
  Prenume varchar(30) not null,
  Varsta int,
  Gen varchar(10),
  Nr_telefon varchar(10) not null unique,
  Adresa varchar(40),
  id_medic int,
  id_diagnostic varchar(10),
  numar_salon int,
  PRIMARY KEY (id_pacient),
  FOREIGN KEY (id_medic) references Medici(id_medic),
  FOREIGN KEY (id_diagnostic) references Diagnostice(id_diagnostic),
  FOREIGN KEY (numar_salon) references Saloane(numar_salon)
  ON DELETE SET NULL
);

insert into sectii values ('CH-GEN','Chirurgie Generala',1);
insert into sectii values ('CH-CRD','Chirurgie Cardiovasculara',1);
insert into sectii values ('CARD','Cardiologie',2);
insert into sectii values ('CH-PLAST','Chirurgie Plastica',3);
insert into sectii values ('DERMAT','Dermatologie',3);
insert into sectii values ('NEURO-CH','Neurochirurgie',4);
insert into sectii values ('NEURO','Neurologie',4);
insert into sectii values ('ONC','Oncologie',5);
insert into sectii values ('GINEC','Ginecologie',6);
insert into sectii values ('OFT','Oftarmologie',7);
insert into sectii values ('ORL','Otorinolaringologie',7);
insert into sectii values ('PED','Pediatrie',8);

insert into medici values (1,'Badea', 'Nicolae','badeanicolae@gmail.com','0742765401',42,'CH-GEN');
insert into medici values (2,'Darie', 'Emanuel','darie_emanuel@gmail.com','0743974652',37,'CH-GEN');
insert into medici values (3,'Florea', 'Maria Ioana','floreamaria@gmail.com','0725397153',35,'CH-CRD');
insert into medici values (4,'Ivanov', 'Andrei','ivanovandrei@gmail.com','0752836594',44,'CH-PLAST');
insert into medici values (5,'Lascu', 'Mihaela','lascumihaela@yahoo.com','0747396205',39,'DERMAT');
insert into medici values (6,'Calin', 'Diana','calindiana@gmail.com','0725095487',34,'DERMAT');
insert into medici values (7,'Stanescu', 'Andrei Ioan','stanescuioan@yahoo.com','0747351648',49,'NEURO-CH');
insert into medici values (8,'Vintila', 'Mihai','mihaivintila@yahoo.com','0747392870',36,'NEURO-CH');
insert into medici values (9,'Stefanescu', 'Florian','florianstefanescu@icloud.com','0743078632',29,'NEURO');
insert into medici values (10,'Silaghi', 'Marius Alexandru','silaghi@gmail.com','07287015388',49,'NEURO');
insert into medici values (11,'Radu', 'Serghei','raduderghei@gmail.com','0744378290',51,'NEURO');
insert into medici values (12,'Popa', 'Dragos','popadragos@yahoo.com','0745551643',48,'ONC');
insert into medici values (13,'Olteanu', 'Mihai','loteanumihai@gmail.com','0725889122',43,'ONC');
insert into medici values (14,'Trandafir', 'Anamaria','trandafir@gmail.com','0746679103',31,'GINEC');
insert into medici values (15,'Pana', 'Elena','elenapana@yahoo.com','0741601882',45,'GINEC');
insert into medici values (16,'Nicoara', 'Andrei','andreinicoara@yahoo.com','0764117829',38,'OFT');
insert into medici values (17,'Enache', 'Sorin','enachesorin@yahoo.com','0725591022',44,'OFT');
insert into medici values (18,'Achim', 'Catalina','achimcatalina@gmail.com','0753447810',37,'ORL');
insert into medici values (19,'Constantinescu', 'Victor','constantinescuvictor@gmail.com','0746658204',52,'ORL');
insert into medici values (20,'Popescu', 'Delia','popescudelia@yahoo.com','0721590226',48,'ORL');
insert into medici values (21,'Leonida', 'Tudor','leonidatudor@yahoo.com','0744789700',35,'ORL');
insert into medici values (22,'Neamtu', 'Andrada','andradaneamtu@gmail.com','0758995102',37,'CARD');
insert into medici values (23,'Mihaila', 'Alin','alinmihaila@gmail.com','0744569182',33,'PED');
insert into medici values (24,'Stanciu', 'Mihaela','stanciumihaela@yahoo.com','0753248901',54,'PED');

insert into saloane values (1,'femei',4);
insert into saloane values (2,'femei',5);
insert into saloane values (3,'barbati',4);
insert into saloane values (4,'barbati',6);
insert into saloane values (11,'femei',6);
insert into saloane values (12,'femei',4);
insert into saloane values (13,'barbati',5);
insert into saloane values (14,'barbati',4);
insert into saloane values (20,'femei',4);
insert into saloane values (21,'femei',6);
insert into saloane values (22,'barbati',4);
insert into saloane values (23,'barbati',8);
insert into saloane values (30,'femei',4);
insert into saloane values (31,'femei',5);
insert into saloane values (32,'barbati',4);
insert into saloane values (33,'barbati',4);

insert into asistenti values (2,'Cristescu','Carina','carinacristescu@gmial.com','0726291880','03-APR-2005',1);
insert into asistenti values (3,'Ivan','Daria','dariaivan@gmial.com','0758199012','26-MAY-2010',2);
insert into asistenti values (3,'Avram','Marius','mariusavram@gmial.com','0754238750','21-JUN-2010',2);
insert into asistenti values (4,'Mihaila','Alina','alinamihaila@gmial.com','0758540917','15-AUG-2007',4);
insert into asistenti values (5,'Barbu','Darius','dariusbarbu@gmial.com','0758199325','04-APR-2013',11);
insert into asistenti values (6,'Stancescu','Maria','mariastancescu@yahoo.com','0759649017','23-MAY-2024',12);
insert into asistenti values (7,'Tica','Ioan','ioantica@gmial.com','0753287640','10-FEB-2010',13);
insert into asistenti values (8,'Adam','Ilinca','adamilinca@gmial.com','0754198752','02-MAY-2008',14);
insert into asistenti values (9,'Petrascu','Andrada','petrascuandra@gmial.com','0758780192','23-SEP-2015',20);
insert into asistenti values (10,'Ilie','Diana','dianailie@gmial.com','0728710936','21-NOV-2006',21);
insert into asistenti values (11,'Popescu','Matei','mateipopescu@gmial.com','0768102854','04-DEC-2010',22);
commit;

INSERT INTO pacienti VALUES (1, 'Ionescu','Mihai',62,'masculin','0726671928','Bulevardul Mihail Kogalniceanu',12,NULL,NULL);
INSERT INTO pacienti VALUES (2, 'Dumitru','Ana',35,'feminin','0758170922','Splaiul independentei nr 14',22,'MenVir',1);
INSERT INTO pacienti VALUES (3, 'Costea','Andrei',35,'masculin','0758710927','Strada Academiei 14',12,'Rac',3);
INSERT INTO pacienti VALUES (4, 'Mihailescu','Stefan',35,'masculin','0728177609','Strada Plantelor 21',12,'InfOc',4);
INSERT INTO pacienti VALUES (5, 'Catrina','Daniel',42,'masculin','0758197265','Splaiul independentei nr 14',13,'MenVir',1);
INSERT INTO pacienti VALUES (6, 'Floroiu','Raluca',35,'feminin','0726510998','Bulevardul Elisabeta nr 5',9,'TbCirc',3);
INSERT INTO pacienti VALUES (7, 'Dinoiu','Mircea',27,'masculin','0764518902','Strada Mihai Eminescu nr 10',3,'TbEch',32);
INSERT INTO pacienti VALUES (8, 'Simionescu','Georgiana',45,'feminin','0757199082','Strada Cosbuc nr 16',6,'TbEch',11);

insert into tratamente values ('vitD','Vitamina D',10);
insert into tratamente values ('vitA','Vitamina A',15);
insert into tratamente values ('vitC','Vitamina C',5);
insert into tratamente values ('mag','Magneziu',10);
insert into tratamente values ('Ca','Calciu',20);
insert into tratamente values ('Lec','Lecitina',6);
insert into tratamente values ('Para','Paracetamol',7);
insert into tratamente values ('Algo','Algocalmin',9);

insert into diagnostice values('MenVir','Meningita virala','mag');
insert into diagnostice values('InfOc','Infectie oculara','vitA');
insert into diagnostice values('TbEch','Tulburari de echilibru','vitD');
insert into diagnostice values('TbCirc','Tulburari circulatorii','Ca');
insert into diagnostice values('Rac','Raceala','Para');























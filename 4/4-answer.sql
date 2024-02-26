CREATE TABLE  Advertiser (
	id INT NOT NULL,
	name  VARCHAR (25) NOT NULL,
	clicks INT DEFAULT '0',
	views INT DEFAULT '0',
	PRIMARY KEY (id)
	);
	

CREATE TABLE Ad (
	id INT NOT NULL,
	title VARCHAR (100) NOT NULL,
	img_url VARCHAR NOT NULL,
	link VARCHAR NOT NULL,
	clicks INT DEFAULT '0',
	views INT DEFAULT '0',
	advertiser_id INT,
	CONSTRAINT FK_Advertiser
	FOREIGN KEY(advertiser_id) 
	REFERENCES Advertiser(id),
	PRIMARY KEY (id)
	);
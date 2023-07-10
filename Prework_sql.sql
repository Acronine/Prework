CREATE DATABASE prework;
USE prework;
CREATE TABLE magic_cards (
 card_id INT AUTO_INCREMENT, 
 PRIMARY KEY (card_id));
ALTER TABLE magic_cards
ADD name VARCHAR(255);
ALTER TABLE magic_cards
ADD price FLOAT;
INSERT INTO magic_cards (name, price)
Values ('Bind', 2.71),
		('Titanias Song', 1.30),
        ('Vexing Shusher', 4.92),
        ('Greater Good', 4.43),
        ('Metamorphosis', 5.00),
        ('Natures Chosen', 5.84);
SELECT * FROM magic_cards;
        


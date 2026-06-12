
create database project;

use project;

create table user
(sno int, username varchar(20) primary key, password varchar(20));

create table movies
(mid int primary key, mname varchar(300), rating char(3), duration char(60), description text);

create table date_manager
(mdate date);

create table time_manager
(time time);

create table ticket_manager
(username varchar(20),mname varchar(40),mdate date,time time,tname varchar(10),seats varchar(50));

insert into time_manager values
('12:00:00');

insert into movies values
(1,
'Avengers Endgame',
'8.4',
'3h 01m',
'The fourth installment in the Avengers saga is the culmination of 22 interconnected Marvel films and the climax of a journey. The worlds heroes finally understand just how fragile reality is, and the sacrifices that must be made to uphold it, in a story of friendship, teamwork and setting aside differences to overcome an impossible obstacle.'),
(2,
'Inception',
'8.8',
'2h 28m',
'Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter peoples dreams and steal their secrets from their subconscious. His skill has made him a hot commodity in the world of corporate espionage but has also cost him everything he loves. Cobb gets a chance at redemption when he is offered a seemingly impossible task: Plant an idea in someones mind. If he succeeds, it will be the perfect crime, but a dangerous enemy anticipates Cobbs every move.'),
(3,
'Jurassic Park',
'8.2',
'2h 07m',
'In Steven Spielbergs massive blockbuster, paleontologists Alan Grant (Sam Neill) and Ellie Sattler (Laura Dern) and mathematician Ian Malcolm (Jeff Goldblum) are among a select group chosen to tour an island theme park populated by dinosaurs created from prehistoric DNA. While the parks mastermind, billionaire John Hammond (Richard Attenborough), assures everyone that the facility is safe, they find out otherwise when various ferocious predators break free and go on the hunt.'),
(4,
'Now You See Me 2',
'6.4',
'2h 09m',
'After fleeing from a stage show, the illusionists (Jesse Eisenberg, Woody Harrelson) known as the Four Horsemen find themselves in more trouble in Macau, China. Devious tech wizard Walter Mabry (Daniel Radcliffe) forces the infamous magicians to steal a powerful chip that can control all of the worlds computers. Meanwhile, vengeful FBI agent Dylan Rhodes (Mark Ruffalo) hatches his own plot against Thaddeus Bradley (Morgan Freeman), the man he blames for the death of his father.'),
(5,
'Oppenheimer',
'8.3',
'3hr 00m',
'During World War II, Lt. Leslie Groves Jr. appoints physicist Robert Oppenheimer to work on the top-secret Manhattan Project. He and a team of scientists spend years developing and designing the atomic bomb. Their work comes to fruition on July 16, 1945, as they witness the first nuclear explosion, forever changing the course of history.'),
(6,
'Dune: Part Two',
'8.5',
'2h 46m',
'Dune Part Two will explore the mythic journey of Paul Atreides as he unites with Chani and the Fremen while on a warpath of revenge against the conspirators who destroyed his family. Facing a choice between the love of his life and the fate of the known universe he endeavors to prevent a terrible future only he can foresee.'),
(7,
'Interstellar',
'8.7',
'2h 49m',
'When Earth becomes uninhabitable in the future a farmer and ex-NASA pilot Joseph Cooper is tasked to pilot a spacecraft along with a team of researchers to find a new planet for humans.'),
(8,
'Mission: Impossible-The Final Reckoning',
'7.4',
'2h 49m',
'Our lives are the sum of our choices. Tom Cruise is Ethan Hunt in Mission Impossible  The Final Reckoning.'),
(9,
'The Batman',
'7.8',
'2h 56m',
'When a sadistic serial killer begins murdering key political figures in Gotham the Batman is forced to investigate the city hidden corruption and question his involvement.'),
(10,
'Skyfall',
'7.8',
'2h 23m',
'James Bonds loyalty to M is tested when her past comes back to haunt her. When MI6 comes under attack 007 must track down and destroy the threat no matter how personal the cost.');









USE startersq;
-- Create the table (guessing column names from your data)
CREATE TABLE players (
    id       INT PRIMARY KEY,
    name     VARCHAR(50),
    age      INT,
    jersey   INT,
    team     VARCHAR(10),
    score    INT
);

-- Insert all your rows
INSERT INTO players VALUES (1, 'Alice',   20, 8,  'KTM', 40);
INSERT INTO players VALUES (2, 'Bob',     21, 9,  'BKT', 30);
INSERT INTO players VALUES (3, 'Cam',     30, 10, 'PKR', 80);
INSERT INTO players VALUES (4, 'ROb',     16, 11, 'MNG', 99);
INSERT INTO players VALUES (5, 'Ronaldo', 19, 48, 'BRG', 75);
SELECT * FROM students;


-- All data
SELECT * FROM players;

-- Specific columns
SELECT name, team, score FROM players;

-- With a condition
SELECT * FROM players WHERE score > 50;
SELECT * FROM players WHERE age < 20;
SELECT * FROM players WHERE team = 'KTM';

-- Multiple conditions
SELECT * FROM players WHERE age > 18 AND score > 50;
SELECT * FROM players WHERE team = 'KTM' OR team = 'BKT';

-- Pattern matching
SELECT * FROM players WHERE name LIKE 'R%';   -- starts with R
SELECT * FROM players WHERE name LIKE '%ob%'; -- contains 'ob'

-- Sort results
SELECT * FROM players ORDER BY score DESC;   -- highest score first
SELECT * FROM players ORDER BY age ASC;      -- youngest first

-- Limit results
SELECT * FROM players ORDER BY score DESC LIMIT 3; -- top 3

-- Distinct values
SELECT DISTINCT team FROM players;

-- Delete
Delete FROM players WHERE id=3;
Delete FROM players WHERE  score <75;

-- UPdate

UPDATE players SET score =90 where id=1;
UPDATE players SET name = "Rob" where id =4;
UPDATE players SET name = "Pravat", score= 100, jersey= 10 where id=5;


-- Agregate functions
SELECT
 COUNT(*)  AS total_players,
 SUM(score) AS total_score,
 AVG(score) AS Average_Score,
 MAX(score) AS Highest_Score,
MIN(score) AS lowest_Score
FROM players;

SELECT * FROM players;
SELECT 
MAX(age) AS oldest_player,
COUNT(age) as total_age,
AVG(age) as average_age_players,
MIN(age) as youngest_player
FROM players;
SELECT * FROM players;

SELECT team, COUNT(*) AS total_players
FROM Players
GROUP BY team;

--- - JOIN

-- CREATE TABLE Teams (
-- team VARCHAR(50),
-- players int,
-- Captain Varchar(50),
-- League VARCHAR(10)
-- );

-- INSERT INTO Teams VALUES( "KTM", 5,"Red", "A");
-- INSERT INTO Teams VALUES( "BKT", 5,"Blue", "A");
-- INSERT INTO Teams VALUES( "LLT", 5,"White", "B");

-- SELECT players.name, players.score, Teams.Captain, Teams.League
-- FROM players
-- INNER JOIN Teams ON players.team = Teams.team; 







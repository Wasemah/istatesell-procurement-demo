-- iStateSell database Schema Demo 
-- Simplified version for porfolio demonstration 

CREATE TABLE projects ( 
       id  INTEGER PRIMARY KEY, 
      name TEXT NOT NULL, 
      budget  REAL,
      requirements TEXT,
      created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );

       

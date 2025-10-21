-- iStateSell Database Schema Demo
-- Simplified version for portfolio demonstration

CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    budget REAL,
    requirements TEXT,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE vendors (
    id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL,
    specialty TEXT,
    contact_email TEXT
);

CREATE TABLE quotations (
    id INTEGER PRIMARY KEY,
    project_id INTEGER,
    vendor_id INTEGER,
    quote_amount REAL,
    quote_details TEXT,
    FOREIGN KEY (project_id) REFERENCES projects (id),
    FOREIGN KEY (vendor_id) REFERENCES vendors (id)
);

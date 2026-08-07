CREATE TABLE properties (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE tenants (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone_number VARCHAR(50),
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE leases (
    id SERIAL PRIMARY KEY,
    property_id INTEGER NOT NULL,
    tenant_id INTEGER NOT NULL,
    monthly_rent NUMERIC(10,2),
    start_date DATE,
    end_date DATE
);

CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    lease_id INTEGER NOT NULL,
    amount NUMERIC(10,2),
    payment_date DATE
);
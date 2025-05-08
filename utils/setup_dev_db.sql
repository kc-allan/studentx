-- Prepares the SQL server for development

CREATE DATABASE IF NOT EXISTS studentx_db;

-- Create user if not exists
CREATE USER IF NOT EXISTS 'studentx_dev'@'localhost' IDENTIFIED BY 'password';

-- Grant appropriate privileges
GRANT SELECT ON performance_schema.* TO 'studentx_dev'@'localhost';
GRANT ALL PRIVILEGES ON studentx_db.* TO 'studentx_dev'@'localhost';
FLUSH PRIVILEGES;

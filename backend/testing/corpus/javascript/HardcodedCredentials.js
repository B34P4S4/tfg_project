// hardcoded credentials
const mysql = require('mysql2');

const db = mysql.createConnection({
    host: 'localhost',
    user: 'admin',
    password: 'SuperSecret123',
    database: 'app'
});
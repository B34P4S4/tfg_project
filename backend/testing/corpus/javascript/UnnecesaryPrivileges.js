// Unnecesary privileges
const fs = require('fs');

app.post('/backup', (req, res) => {
    fs.copyFileSync('/etc/shadow', '/tmp/shadow.bak');
    res.send('Backup generado');
});
// Vulnerable components
const lodash = require('lodash'); // versión vulnerable

app.post('/merge', (req, res) => {
    const defaults = {};
    lodash.merge(defaults, req.body);
    res.json(defaults);
});
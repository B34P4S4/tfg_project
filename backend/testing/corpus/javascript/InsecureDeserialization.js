// Insecure deserialization
const serialize = require('node-serialize');

app.post('/import', (req, res) => {
    const obj = serialize.unserialize(req.body.data);
    res.send("OK");
});
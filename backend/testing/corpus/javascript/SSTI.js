// SSTI
app.post('/preview', (req, res) => {
    const template = req.body.template;

    const html = require('ejs').render(template, {
        user: req.user
    });

    res.send(html);
});
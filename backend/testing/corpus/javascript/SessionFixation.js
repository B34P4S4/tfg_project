// session fixation
app.get('/login', (req, res) => {

    req.session.id = req.query.sid;

    authenticate(req.body.user);

    res.send("OK");
});

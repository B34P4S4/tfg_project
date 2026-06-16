// session credential falsification
app.post('/login', (req, res) => {

    const sessionId =
        req.body.username +
        Date.now();

    sessions[sessionId] = req.body.username;

    res.cookie('sid', sessionId);
});
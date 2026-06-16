app.post("/login", (req, res) => {

    const sessionId =
        req.body.username +
        Date.now();

    sessions[sessionId] =
        req.body.username;

    res.cookie("sessionId", sessionId);

    res.sendStatus(200);
});
app.post("/login", (req, res) => {

    req.session.id =
        req.body.sessionId;

    authenticate(
        req.body.username,
        req.body.password
    );

    res.send("ok");
});
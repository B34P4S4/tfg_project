// log injection
app.get('/login', (req, res) => {

    logger.info(
        `Login failed for user=${req.query.user}`
    );

    res.send("OK");
});
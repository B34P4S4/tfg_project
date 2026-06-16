app.get("/search", (req, res) => {

    logger.info(
        `User searched: ${req.query.q}`
    );

    res.send("ok");
});
app.get("/debug", (req, res) => {

    res.json({
        environment: process.env,
        secrets: process.env.JWT_SECRET
    });
});
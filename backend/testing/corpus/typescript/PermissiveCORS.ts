app.use((req, res, next) => {

    res.header(
        "Access-Control-Allow-Origin",
        req.headers.origin as string
    );

    res.header(
        "Access-Control-Allow-Credentials",
        "true"
    );

    next();
});
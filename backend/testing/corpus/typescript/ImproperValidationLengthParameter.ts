app.post("/process", (req, res) => {

    const length = Number(req.body.length);

    const payload =
        req.body.data.substring(0, length);

    processData(payload);

    res.send("ok");
});
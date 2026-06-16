const buffer = Buffer.alloc(32);

app.post("/upload", (req, res) => {

    buffer.write(req.body.content);

    res.send("saved");
});
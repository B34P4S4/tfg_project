// Buffer Overflow
const buffer = Buffer.alloc(16);

app.post('/upload', (req, res) => {
    buffer.write(req.body.content);
    res.send("OK");
});
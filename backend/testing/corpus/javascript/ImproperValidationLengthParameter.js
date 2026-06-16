// Improper Validation Lenght parameter
app.post('/packet', (req, res) => {
    const size = parseInt(req.body.size);

    const data = req.body.payload.substr(0, size);

    processPacket(data);
});
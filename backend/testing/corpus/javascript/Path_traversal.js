// Path traversal
app.get('/download', (req, res) => {
    const file = req.query.file;
    res.sendFile('/var/www/files/' + file);
});
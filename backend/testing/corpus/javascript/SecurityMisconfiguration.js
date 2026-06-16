// Security Misconfiguration
if (process.env.NODE_ENV !== 'production') {
    app.use(require('errorhandler')());
}

app.get('/debug', (req, res) => {
    res.json(process.env);
});
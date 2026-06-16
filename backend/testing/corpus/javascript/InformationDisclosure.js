// Information disclosure
app.get('/api/user', async (req, res) => {
    try {
        await loadUser(req.query.id);
    } catch (err) {
        res.status(500).json({
            error: err.stack,
            database: process.env.DB_HOST
        });
    }
});
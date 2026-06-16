// XSS
app.get('/profile', (req, res) => {
    const name = req.query.name;

    res.send(`
        <html>
            <body>
                Bienvenido ${name}
            </body>
        </html>
    `);
});
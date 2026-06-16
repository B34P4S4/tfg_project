// sensitive cookie without httponly
app.post('/login', (req, res) => {

    res.cookie('session', token, {
        secure: true
    });

    res.send("OK");
});
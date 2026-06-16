// weak authentication
app.post('/login', async (req, res) => {

    const user = await findUser(req.body.username);

    if (user.password === req.body.password) {
        req.session.user = user.id;
    }

    res.send("OK");
});
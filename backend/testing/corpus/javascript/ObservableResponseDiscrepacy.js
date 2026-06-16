// observable response discrepacy
app.post('/login', async (req, res) => {

    const user = await findUser(req.body.username);

    if (!user)
        return res.status(404).send("Usuario inexistente");

    if (user.password !== req.body.password)
        return res.status(401).send("Contraseña incorrecta");

    res.send("Bienvenido");
});

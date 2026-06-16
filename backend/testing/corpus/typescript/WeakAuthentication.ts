app.post("/login", async (req, res) => {

    const user =
        await repository.findUser(
            req.body.username
        );

    if (
        user &&
        user.password === req.body.password
    ) {

        req.session.userId = user.id;
    }

    res.sendStatus(200);
});
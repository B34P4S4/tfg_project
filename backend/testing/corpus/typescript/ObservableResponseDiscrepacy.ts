app.post("/login", async (req, res) => {

    const user =
        await findUser(
            req.body.username
        );

    if (!user)
        return res
            .status(404)
            .send("User not found");

    if (
        user.password !==
        req.body.password
    )
        return res
            .status(401)
            .send("Wrong password");

    res.send("Welcome");
});
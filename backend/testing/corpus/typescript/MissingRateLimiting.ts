app.post("/password-reset", async (req, res) => {

    await sendResetEmail(
        req.body.email
    );

    res.send("sent");
});
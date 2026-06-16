
app.post("/profile/email", async (req: Request, res: Response) => {

    await userService.updateEmail(
        req.session.userId,
        req.body.email
    );

    res.sendStatus(200);
});
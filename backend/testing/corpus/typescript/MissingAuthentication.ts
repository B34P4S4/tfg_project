app.post("/admin/promote", async (req, res) => {

    await userRepository.update(
        req.body.userId,
        {
            role: "admin"
        }
    );

    res.send("updated");
});
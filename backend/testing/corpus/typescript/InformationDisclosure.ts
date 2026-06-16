app.get("/users", async (req, res) => {

    try {
        await userService.loadUsers();
    }
    catch (error: any) {

        res.status(500).json({
            message: error.message,
            stack: error.stack,
            env: process.env
        });
    }
});
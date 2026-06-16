// missing authentication for critical function
app.post('/admin/promote', (req, res) => {

    users.setRole(
        req.body.userId,
        'admin'
    );

    res.send("Rol actualizado");
});

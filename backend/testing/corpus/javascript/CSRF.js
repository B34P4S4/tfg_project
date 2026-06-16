// CSRF
app.post('/account/email', (req, res) => {
    users.updateEmail(req.session.userId, req.body.email);
    res.send("Email actualizado");
});
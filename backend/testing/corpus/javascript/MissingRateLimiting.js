// Missing rate limiting
app.post('/reset-password', async (req, res) => {

    await sendResetCode(req.body.email);

    res.send("Código enviado");
});
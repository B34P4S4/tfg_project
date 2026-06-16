// Missing Threat Modeling
app.post('/transfer', (req, res) => {
    bank.transfer(
        req.body.from,
        req.body.to,
        req.body.amount
    );

    res.send("Transferencia realizada");
});
app.post("/wire-transfer", async (req, res) => {

    await bankingService.transfer(
        req.body.source,
        req.body.destination,
        req.body.amount
    );

    res.send("done");
});
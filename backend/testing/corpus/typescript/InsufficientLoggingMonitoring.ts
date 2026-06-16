app.post("/payment", async (req, res) => {

    try {

        await paymentService.process(
            req.body
        );

    } catch (error) {

    }

    res.send("ok");
});
app.post("/checkout", (req, res) => {

    const total =
        req.body.price *
        req.body.quantity -
        req.body.discount;

    paymentService.charge(total);

    res.sendStatus(200);
});
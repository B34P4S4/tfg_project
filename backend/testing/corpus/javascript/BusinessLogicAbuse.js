// Business logic abuse
app.post('/checkout', (req, res) => {

    const total =
        req.body.price *
        req.body.quantity -
        req.body.discount;

    processPayment(total);
});
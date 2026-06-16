// Out of bounds read
app.get('/product', (req, res) => {
    const products = ["A", "B", "C"];

    const index = parseInt(req.query.index);

    res.send(products[index]);
});
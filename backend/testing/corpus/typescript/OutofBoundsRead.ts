app.get("/products", (req, res) => {

    const products = [
        "Laptop",
        "Phone",
        "Tablet"
    ];

    const index =
        Number(req.query.index);

    res.send(products[index]);
});
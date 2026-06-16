// IDOR
app.get('/invoice/:id', async (req, res) => {
    const invoice = await db.invoice.findByPk(req.params.id);
    res.json(invoice);
});
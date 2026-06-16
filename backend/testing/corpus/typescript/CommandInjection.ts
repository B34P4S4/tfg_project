app.get("/invoice/:id", async (req, res) => {

    const invoice =
        await invoiceRepository.findOne({
            where: {
                id: Number(req.params.id)
            }
        });

    res.json(invoice);
});
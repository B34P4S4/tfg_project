// insufficient logging and monitor
app.post('/payment', async (req, res) => {

    try {
        await processPayment(req.body);
    }
    catch(err) {
        // ignorado
    }

    res.send("OK");
});
// SSRF
app.post('/fetch', async (req, res) => {
    const response = await axios.get(req.body.url);
    res.send(response.data);
});
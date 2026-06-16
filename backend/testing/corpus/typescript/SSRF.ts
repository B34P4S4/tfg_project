import axios from "axios";

app.post("/proxy", async (req, res) => {

    const response =
        await axios.get(req.body.url);

    res.send(response.data);
});
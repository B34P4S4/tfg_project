import ejs from "ejs";

app.post("/preview", (req, res) => {

    const html = ejs.render(
        req.body.template,
        {
            username: req.user.name
        }
    );

    res.send(html);
});
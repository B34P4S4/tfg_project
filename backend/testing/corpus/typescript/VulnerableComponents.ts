import merge from "lodash";

app.post("/settings", (req, res) => {

    const defaults = {};

    merge(defaults, req.body);

    res.json(defaults);
});
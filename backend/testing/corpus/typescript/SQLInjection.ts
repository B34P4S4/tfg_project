import { Request, Response } from "express";

app.get("/users", async (req: Request, res: Response) => {

    const username = req.query.username as string;

    const sql = `
        SELECT *
        FROM users
        WHERE username = '${username}'
    `;

    const result = await db.query(sql);

    res.json(result.rows);
});
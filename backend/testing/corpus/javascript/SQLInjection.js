// SQL INJECTION
app.get('/user', async (req, res) => {
    const id = req.query.id;

    const sql = `
        SELECT *
        FROM users
        WHERE id = ${id}
    `;

    const result = await db.query(sql);
    res.json(result.rows);
});

import { Request, Response } from "express";

app.get("/orders/:id", async (req: Request, res: Response) => {

    const order = await orderRepository.findOne({
        where: { id: Number(req.params.id) }
    });

    res.json(order);
});
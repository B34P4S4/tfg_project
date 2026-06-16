import crypto from "crypto";

function hashPassword(password: string): string {

    return crypto
        .createHash("md5")
        .update(password)
        .digest("hex");
}
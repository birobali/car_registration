CREATE TABLE IF NOT EXISTS jarmu (
    uuid UUID primary key DEFAULT gen_random_uuid(),
    rendszam VARCHAR(20),
    tulajdonos VARCHAR(200),
    forgalmi_ervenyes VARCHAR(10),
    adatok text[200]
);

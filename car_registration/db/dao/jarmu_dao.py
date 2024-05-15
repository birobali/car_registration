import uuid
from typing import List

from fastapi import Depends
from psycopg.rows import class_row
from psycopg_pool import AsyncConnectionPool

from car_registration.db.dependencies import get_db_pool
from car_registration.db.models.jarmu_model import JarmuModel


class JarmuDAO:
    def __init__(
        self,
        db_pool: AsyncConnectionPool = Depends(get_db_pool),
    ):
        self.db_pool = db_pool

    async def create_jarmu_model(
        self,
        uuid: uuid.UUID,
        rendszam: str,
        tulajdonos: str,
        forgalmi_ervenyes: str,
        adatok: List[str],
    ) -> None:
        async with self.db_pool.connection() as connection:
            async with connection.cursor(binary=True) as cur:
                await cur.execute(
                    "INSERT INTO jarmu (uuid, rendszam, tulajdonos, forgalmi_ervenyes, adatok, szoveg) "
                    "VALUES (%(uuid)s, %(rendszam)s, %(tulajdonos)s, %(forgalmi_ervenyes)s, %(adatok)s, %(szoveg)s);",
                    params={
                        "uuid": uuid,
                        "rendszam": rendszam,
                        "tulajdonos": tulajdonos,
                        "forgalmi_ervenyes": forgalmi_ervenyes,
                        "adatok": adatok,
                        "szoveg": f"{rendszam} {tulajdonos} {str(adatok)}".lower(),
                    },
                )

    async def get_all_jarmu(self) -> List[JarmuModel]:
        async with self.db_pool.connection() as connection:
            async with connection.cursor(
                binary=True,
                row_factory=class_row(JarmuModel),
            ) as cur:
                res = await cur.execute(
                    "SELECT * FROM jarmu;",
                )
                return await res.fetchall()

    async def get_jarmu_by_filter(self, query: str) -> List[JarmuModel]:
        async with self.db_pool.connection() as connection:
            async with connection.cursor(
                binary=True,
                row_factory=class_row(JarmuModel),
            ) as cur:
                res = await cur.execute(
                    "SELECT * FROM jarmu WHERE szoveg LIKE %(query)s;",
                    params={
                        "query": f"%{query.lower()}%",
                    },
                )
                return await res.fetchall()

    async def get_jarmu(self, uuid: str) -> JarmuModel:
        async with self.db_pool.connection() as connection:
            async with connection.cursor(
                binary=True,
                row_factory=class_row(JarmuModel),
            ) as cur:
                res = await cur.execute(
                    "SELECT * FROM jarmu WHERE uuid = %(uuid)s;",
                    params={
                        "uuid": uuid,
                    },
                )
                return await res.fetchone()

    async def get_jarmu_count(self) -> int:
        async with self.db_pool.connection() as connection:
            async with connection.cursor(binary=True) as cur:
                res = await cur.execute(
                    "SELECT COUNT(1) FROM jarmu;",
                )
                result = await res.fetchone()
                return result[0]

from sqlite3 import Connection
from typing import List, Tuple


class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_activity(self, activities_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO activities
                    (id, trip_id, title, occurs_at)
                VALUES
                    (?, ?, ?, ?)
            ''',
            (
                activities_info["id"],
                activities_info["trip_id"],
                activities_info["title"],
                activities_info["occurs_at"]
            )
        )
        self.__conn.commit()

    def find_activities_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT
                   *
                FROM activities
                WHERE
                    trip_id = ?
            ''', (trip_id,)
        )
        participants = cursor.fetchall()
        return participants

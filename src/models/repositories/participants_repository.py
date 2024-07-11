from sqlite3 import Connection
from typing import List, Tuple


class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_participant(self, participant_infos: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO participantes
                    (id, trip_id, emails_to_invite_id, name)
                VALUES
                    (?, ?, ?, ?)
            ''',
            (participant_infos["id"],
             participant_infos["trip_id"],
             participant_infos["emails_to_invite_id"],
             participant_infos["name"])
        )
        self.__conn.commit()

    def find_participants_from_trio(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT
                    p.Id, p.name, p.is_confirmed, e.email
                FROM participants as p
                JOIN emails_to_invite as e ON e.id = p.emails_to_invite.id
                WHERE
                    p.trip_id = ?
            ''', (trip_id,)
        )
        participants = cursor.fetchall()
        return participants

    def update_participant_status(self, participant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                UPDATE 
                    participants
                SET
                    is_confirmed = 1
                WHERE
                    id = ?
            ''', (participant_id,)
        )
        self.__conn.commit()

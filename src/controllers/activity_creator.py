import uuid

class ActivityCreator:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def create(self, body, trip_id) -> dict:
        try:
            activity_id = str(uuid.uuid4())
            activities_infos = {
                "trip_id": trip_id,
                "id": activity_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"]
            }
            self.__activities_repository.registry_activity(activities_infos)
            return {
                "body":
                    {
                     "link_id": activity_id
                     },
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

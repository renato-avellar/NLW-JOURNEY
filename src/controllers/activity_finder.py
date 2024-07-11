class ActivityFinder:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def find_activities_from_trip(self, trip_id: str) -> dict:
        try:
            activities = self.__activities_repository.find_activities_from_trip(trip_id)

            activities_info = []
            for activity in activities:
                activities_info.append({
                    "id": activity[0],
                    "title": activity[2],
                    "occurs_at": activity[3],
                })
            return {
                "body": {"activities": activities_info},
                "status_code": 200
            }
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

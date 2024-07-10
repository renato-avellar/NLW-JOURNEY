from flask import jsonify, Blueprint, request
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirm import TripConfirm
from src.controllers.link_creator import LinkCreator
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import  LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

trip_routes_bp = Blueprint("trip_routes", __name__)
trip_repository = TripCreator

@trip_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repository, emails_repository)

    response = controller.create(request.json)

    return jsonify(response["body"], response["status_code"])

@trip_routes_bp.route("/trips/<trip_id>", methods=["GET"])
def find_trip(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)

    response = controller.find_trip_details(trip_id)
    return jsonify(response["body"], response["status_code"])


@trip_routes_bp.route("/trips/<trip_id>/confirm", methods=["GET"])
def confirm_trip(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirm(trips_repository)

    response = controller.confirm(trip_id)
    return jsonify(None)


@trip_routes_bp.route("/links/<trip_id>", methods=["POST"])
def create_trip_link(trip_id):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)

    response = controller.create(request.json, trip_id)

    return jsonify(response["link_id"], response["status_code"])
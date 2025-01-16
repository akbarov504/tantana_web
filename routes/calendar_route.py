from app import root
from models import models
from flask_login import login_required
from flask import render_template, redirect, url_for

@root.route("/change-status/<calendar_id>/<profile_id>", methods=["GET", "POST"])
@login_required
def change_status_page(calendar_id, profile_id) -> render_template:
    calendar = models.Calendar.query.filter_by(id=calendar_id, is_deleted=False).first()
    calendar.is_free = not calendar.is_free
    models.db.session.commit()
    return redirect(url_for("profile_get_page", id=profile_id))

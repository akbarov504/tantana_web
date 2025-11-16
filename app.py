from flask import Flask
from models.models import db, migrate, login_manager
from models.models import User, ProfileCategory, Profile, ProfileImage, ProfileSave, Slider, Banner, Calendar, Chat, Message, Respublika, Viloyat, Tuman

root = Flask(__name__)
root.config['UPLOAD_FOLDER'] = "static/uploads"
root.config["SECRET_KEY"] = "342afc9ac23241fa1372f913"
root.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://akbarov:akbarov@127.0.0.1:5432/tantana"
root.config["WTF_CSRF_ENABLED"] = False
root.config["WTF_CSRF_SECRET_KEY"] = "fgkgsd23gkfsdk32fds4r3t43t43"

db.init_app(root)
migrate.init_app(root, db)
login_manager.init_app(root)

with root.app_context():
    db.create_all()

if __name__ == "__main__":
    from routes.main_route import *
    from routes.auth_route import *
    from routes.admin_route import *
    from routes.profile_route import *
    from routes.calendar_route import *
    from routes.notification_route import *
    root.run(debug=False, port=80, host='0.0.0.0')

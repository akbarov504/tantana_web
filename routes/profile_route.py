import os
from app import root
from models import models
from datetime import datetime
from calendar import monthrange
from forms.profile_form import ProfileForm, ProfileImageForm
from werkzeug.utils import secure_filename
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required

@root.route("/profile/list/<id>", methods=["GET", "POST"])
def profile_list_page(id) -> render_template:
    profile_l = models.Profile.query.filter_by(category_id=id, is_deleted=False).all()
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    return render_template("profile.html", profile_list=profile_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

@root.route("/profile/list/res/<_respublika>", methods=["GET", "POST"])
def profile_list_respublika_page(_respublika) -> render_template:
    profile_l = models.Profile.query.filter_by(respublika=_respublika, is_deleted=False).all()
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    return render_template("profile.html", profile_list=profile_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

@root.route("/profile/list/vil/<_viloyat>", methods=["GET", "POST"])
def profile_list_viloyat_page(_viloyat) -> render_template:
    profile_l = models.Profile.query.filter_by(viloyat=_viloyat, is_deleted=False).all()
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    return render_template("profile.html", profile_list=profile_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

@root.route("/profile/list/tu/<_tuman>", methods=["GET", "POST"])
def profile_list_tuman_page(_tuman) -> render_template:
    profile_l = models.Profile.query.filter_by(tuman=_tuman, is_deleted=False).all()
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    return render_template("profile.html", profile_list=profile_l, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

@root.route("/profile/get/<id>", methods=["GET", "POST"])
def profile_get_page(id) -> render_template:
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).all()
    profile = models.Profile.query.filter_by(id=id, is_deleted=False).first()
    calendars = models.Calendar.query.filter_by(profile_id=profile.id, is_deleted=False).order_by(models.Calendar.day).all()
    profile_i = models.ProfileImage.query.filter_by(profile_id=profile.id, is_deleted=False).order_by(models.ProfileImage.order).all()

    profile_count = profile_i[0].id
    for pro in profile_i:
        if pro.id < profile_count:
            profile_count = pro.id
            
    now = datetime.now()
    month_name = now.strftime("%B")

    form = ProfileImageForm()
    if form.validate_on_submit():
        image = form.image.data
        img1 = form.img1.data
        img2 = form.img2.data
        img3 = form.img3.data
        img4 = form.img4.data
        img5 = form.img5.data
        img6 = form.img6.data
        img7 = form.img7.data
        img8 = form.img8.data
        img9 = form.img9.data
        img10 = form.img10.data
        description = form.description.data
        if image:
            filename = secure_filename(image.filename)
            profile.image = "/uploads/" + filename
            models.db.session.commit()
            image.save(os.path.join(root.config["UPLOAD_FOLDER"], filename))
        
        if img1:
            filename1 = secure_filename(img1.filename)
            profile_img1 = models.ProfileImage.query.filter_by(profile_id=profile.id, order=1, is_deleted=False).first()
            profile_img1.image = "/uploads/" + filename1
            models.db.session.commit()
            img1.save(os.path.join(root.config["UPLOAD_FOLDER"], filename1))

        if img2:
            filename2 = secure_filename(img2.filename)
            profile_img2 = models.ProfileImage.query.filter_by(profile_id=profile.id, order=2, is_deleted=False).first()
            profile_img2.image = "/uploads/" + filename2
            models.db.session.commit()
            img2.save(os.path.join(root.config["UPLOAD_FOLDER"], filename2))

        if img3:
            filename3 = secure_filename(img3.filename)
            profile_img3 = models.ProfileImage.query.filter_by(profile_id=profile.id, order=3, is_deleted=False).first()
            profile_img3.image = "/uploads/" + filename3
            models.db.session.commit()
            img3.save(os.path.join(root.config["UPLOAD_FOLDER"], filename3))

        if img4:
            filename4 = secure_filename(img4.filename)
            profile_img4 = models.ProfileImage.query.filter_by(profile_id=profile.id, order=4, is_deleted=False).first()
            profile_img4.image = "/uploads/" + filename4
            models.db.session.commit()
            img4.save(os.path.join(root.config["UPLOAD_FOLDER"], filename4))

        if img5:
            filename5 = secure_filename(img5.filename)
            profile_img5 = models.ProfileImage.query.filter_by(profile_id=profile.id, order=5, is_deleted=False).first()
            profile_img5.image = "/uploads/" + filename5
            models.db.session.commit()
            img5.save(os.path.join(root.config["UPLOAD_FOLDER"], filename5))

        if img6:
            filename6 = secure_filename(img6.filename)
            profile_img6 = models.ProfileImage.query.filter_by(profile_id=profile.id, order=6, is_deleted=False).first()
            profile_img6.image = "/uploads/" + filename6
            models.db.session.commit()
            img6.save(os.path.join(root.config["UPLOAD_FOLDER"], filename6))

        if img7:
            filename7 = secure_filename(img7.filename)
            profile_img7 = models.ProfileImage.query.filter_by(profile_id=profile.id, order=7, is_deleted=False).first()
            profile_img7.image = "/uploads/" + filename7
            models.db.session.commit()
            img7.save(os.path.join(root.config["UPLOAD_FOLDER"], filename7))

        if img8:
            filename8 = secure_filename(img8.filename)
            profile_img8 = models.ProfileImage.query.filter_by(profile_id=profile.id, order=8, is_deleted=False).first()
            profile_img8.image = "/uploads/" + filename8
            models.db.session.commit()
            img8.save(os.path.join(root.config["UPLOAD_FOLDER"], filename8))

        if img9:
            filename9 = secure_filename(img9.filename)
            profile_img9 = models.ProfileImage.query.filter_by(profile_id=profile.id, order=9, is_deleted=False).first()
            profile_img9.image = "/uploads/" + filename9
            models.db.session.commit()
            img9.save(os.path.join(root.config["UPLOAD_FOLDER"], filename9))

        if img10:
            filename10 = secure_filename(img10.filename)
            profile_img10 = models.ProfileImage.query.filter_by(profile_id=profile.id, order=10, is_deleted=False).first()
            profile_img10.image = "/uploads/" + filename10
            models.db.session.commit()
            img10.save(os.path.join(root.config["UPLOAD_FOLDER"], filename10))
        
        if description:
            profile.description = description
            models.db.session.commit()

        return redirect(url_for("profile_get_page", id=profile.id))
    form.description.data = profile.description
    return render_template("profile-get.html", form=form, profile=profile, profile_images=profile_i, p_count=profile_count, calendar_list=calendars, month_name=month_name, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

@root.route("/profile/create", methods=["GET", "POST"])
@login_required
def profile_create_page() -> render_template:
    respublika_l = models.Respublika.query.filter_by(is_deleted=False).order_by(models.Respublika.id).all()
    viloyat_l = models.Viloyat.query.filter_by(is_deleted=False).order_by(models.Viloyat.id).all()
    tuman_l = models.Tuman.query.filter_by(is_deleted=False).order_by(models.Tuman.id).all()
    category_l = models.ProfileCategory.query.filter_by(is_deleted=False).order_by(models.ProfileCategory.order).all()
    category_names = []
    for category in category_l:
        category_names.append(category.title)
    respublika_names = []
    for respublika in respublika_l:
        respublika_names.append(respublika.text)
    viloyat_names = []
    for viloyat in viloyat_l:
        viloyat_names.append(viloyat.text)
    tuman_names = []
    for tuman in tuman_l:
        tuman_names.append(tuman.text)
    form = ProfileForm()
    form.category.choices = category_names
    form.respublika.choices = respublika_names
    form.viloyat.choices = viloyat_names
    form.tuman.choices = tuman_names
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        respublika = form.respublika.data
        viloyat = form.viloyat.data
        tuman = form.tuman.data
        street = form.street.data
        
        category = models.ProfileCategory.query.filter_by(title=category, is_deleted=False).first()
        profile = models.Profile(title, respublika, viloyat, tuman, street, category.id, current_user.id)
        models.db.session.add(profile)
        profile.image = "/uploads/profile_image.jpg"
        models.db.session.commit()

        profile = models.Profile.query.filter_by(title=title, is_deleted=False, created_by=current_user.id).first()
        
        for i in range(1, 11):
            filename = "profile_image.jpg"
            p_im = models.ProfileImage("/uploads/"+filename, profile.id, current_user.id, i)
            models.db.session.add(p_im)
            models.db.session.commit()

        for i in range(0, 7):
            now = datetime.now()
            if (now.month + i) == 13:
               break
            curr_now = datetime(now.year, now.month + i, now.day, now.hour, now.minute, now.second, now.microsecond)
            day_count = monthrange(curr_now.year, curr_now.month)
            month_name = curr_now.strftime("%B")
            for d_count in range(1, day_count[1]+1):
                calendar = models.Calendar(profile.id, d_count, month_name, True, current_user.id)
                models.db.session.add(calendar)
                models.db.session.commit()
        return redirect(url_for("profile_get_page", id=profile.id))
    else:
        category_l = models.ProfileCategory.query.filter_by(is_deleted=False).all()
        return render_template("servisman.html", form=form, respublika_list=respublika_l, viloyat_list=viloyat_l, tuman_list=tuman_l)

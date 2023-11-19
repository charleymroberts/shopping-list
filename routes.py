from flask import render_template, request, redirect, url_for
from app import app, db
from models import Item


@app.route("/", methods=["GET", "POST"])
def home():
    items = list(Item.query.order_by(Item.id).all())
    if request.method == "POST":
        item = Item(name=request.form.get("item_name"))
        db.session.add(item)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("home.html", items=items)


@app.route("/delete_item/<int:item_id>")
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("home"))



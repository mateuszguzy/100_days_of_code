import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    # method switching DB result into a dictionary
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():
    random_cafe = random.choice(db.session.query(Cafe).all())
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    return jsonify(all_cafes=[cafe.to_dict() for cafe in db.session.query(Cafe).all()])

@app.route("/search")
def search_cafe():
    searched_cafes = Cafe.query.filter_by(location=request.args.get("loc"))
    cafes = [cafe.to_dict() for cafe in searched_cafes]
    if len(cafes) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have cafe in that location"})
    return jsonify(cafes)

@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if request.method == "POST":
        print(request.args)
        return jsonify(response={"Success": "Successfully added the new cafe"})

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    try:
        price = request.args.get("coffee_price")
        cafe.coffee_price = price
        db.session.commit()
        return jsonify(response={"Success": "Successfully updated coffee price"})
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe with that id"})

@app.route("/delete-cafe/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.args.get("api_key") == "0123456":
        cafe = Cafe.query.get(cafe_id)
        if cafe is None:
            return jsonify(error={"Not Data": "Sorry, we don't have a cafe with that id"})
        else:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"Success": "Record has been deleted"})
    else:
        return jsonify(error={"Not Access": "Sorry, you don't have a permission to do that"})

if __name__ == '__main__':
    app.run(debug=True)

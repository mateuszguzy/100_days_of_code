from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), URL()])
    open_time = StringField('Open Time e.g. 8:00AM', validators=[DataRequired(), Length(max=7)])
    close_time = StringField('Close Time e.g 10:00PM', validators=[DataRequired(), Length(max=7)])
    coffee_rating = SelectField('Coffee rating',
                                choices=[("☕", "☕"), ("☕☕", "☕☕"), ("☕☕☕", "☕☕☕"), ("☕☕☕☕", "☕☕☕☕"), ("☕☕☕☕☕", "☕☕☕☕☕")],
                                validators=[DataRequired()]
                                )
    wifi_rating = SelectField('Wifi rating',
                              choices=[("✘", "✘"), ("💪", "💪"), ("💪💪", "💪💪"), ("💪💪💪", "💪💪💪"),
                                       ("💪💪💪💪", "💪💪💪💪"), ("💪💪💪💪💪", "💪💪💪💪💪")],
                              validators=[DataRequired()])
    power_rating = SelectField('Power rating',
                               choices=[("✘", "✘"), ("🔌", "🔌"), ("🔌🔌", "🔌🔌"), ("🔌🔌🔌", "🔌🔌🔌"),
                                        ("🔌🔌🔌🔌", "🔌🔌🔌🔌"), ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌")],
                               validators=[DataRequired()])

    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='') as csv_file:
            csv_data = csv.writer(csv_file, delimiter=',')
            csv_data.writerow([form.data['cafe']] +
                              [form.data['location']] +
                              [form.data['open_time']] +
                              [form.data['close_time']] +
                              [form.data['coffee_rating']] +
                              [form.data['wifi_rating']] +
                              [form.data['power_rating']]
                              )
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True)

from flask import *
from main import app
from models import *
import csv


@app.before_first_request
def create_tables():
    db.create_all(app=app)

    fieldnames = ['user_id', 'first_name', 'last_name', 'money', 'account_number', 'account_active_to',
                  'deposit_amount', 'deposit_month_number', 'credit_amount', 'credit_month_number']

    dict_reader = csv.DictReader(open('../data.csv', 'r'), fieldnames=fieldnames, delimiter=',', quotechar='"')

    for row in dict_reader:
        user_item = UserModel(
            user_id=int(row['user_id']),
            first_name=row['first_name'],
            last_name=row['last_name'],
            money=float(row['money'])
        )

        account_item = AccountModel(
            account_number=row['account_number'],
            money=row['money'],
            active_to=row['account_active_to'],
            owner_id=int(row['user_id'])
        )

        deposit_item = DepositModel(
            owner_id=int(row['user_id']),
            amount=row['deposit_amount'],
            month_number=row['deposit_month_number']
        )

        credit_item = CreditModel(
            owner_id=int(row['user_id']),
            amount=row['credit_amount'],
            month_number=row['credit_month_number']
        )

        db.session.add(user_item)
        db.session.add(account_item)
        db.session.add(deposit_item)
        db.session.add(credit_item)

        db.session.commit()


@app.route('/users', methods=['GET'])
def index():
    users_list = UserModel.query.all()

    return render_template("index.html", users_list=users_list)


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        new_user = UserModel(
            first_name=request.form['firstName'],
            last_name=request.form['lastName']
        )
        new_user.save_to_db()

        return redirect('/users')

    return render_template("add-user.html")


@app.route('/remove-user/<int:user_id>', methods=['GET'])
def remove_user(user_id):
    UserModel.query.filter_by(user_id=user_id).delete()
    db.session.commit()

    return redirect('/users')


@app.route('/edit-user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user_item = UserModel.query.filter_by(user_id=user_id).first()

    if request.method == 'POST':
        user_item.first_name = request.form['firstName']
        user_item.last_name = request.form['lastName']

        db.session.commit()

        return redirect('/users')

    return render_template("edit-user.html", user_id=user_id, first_name=user_item.first_name, last_name=user_item.last_name)

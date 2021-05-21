from flask import render_template, session, flash, request, redirect, url_for, send_from_directory, abort
from app import app, db, Status, Unit, CreateProductForm, LoginForm, lm,  UpdateAccount1
from app.models.tables import Products, Order,  Users
from flask_login import login_user, logout_user, current_user, login_required
from PIL import Image
import secrets
import os
from datetime import timedelta

# função para deslogar o user em determinado momento
app.permanent_session_lifetime = timedelta(seconds=30000)

# função login
@lm.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# tela inicial
@app.route("/")
def index():
    
    return render_template('index.html')

# rota de login
@app.route("/index/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        if current_user.id ==1:
            return redirect(url_for('orders'))
        return redirect(url_for('historic'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            if user.id == 1:
                login_user(user)
                session.permanent = True
                return redirect(url_for("orders"))
            login_user(user)
            session.permanent = True
            return redirect(url_for("historic"))
        else:
            flash("login invalido")
   
    return render_template('login.html', form=form)


#rota para deslogar
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

# rota para edição de dados da conta
@app.route("/accounts", methods=['GET','POST'])
@login_required
def account():
    if current_user.id == 1:
        abort(403)
    form = UpdateAccount1()
    print('entrou1')
    if form.validate_on_submit():
        print(form.errors)
        current_user.username=form.username.data
        current_user.password=form.password.data
        current_user.contato=form.contato.data
        current_user.city=form.city.data
        current_user.street=form.street.data
        current_user.number=form.number.data
        db.session.commit()
        flash('Os dados de sua conta foram atualizados', 'success')
        return redirect(url_for("historic", form=form))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.password.data = current_user.password
        form.contato.data = current_user.contato
        form.city.data = current_user.city
        form.street.data = current_user.street
        form.number.data = current_user.number

    return render_template("conta.html", form=form)

# rota para criar usuario
@app.route("/user/new", methods=['GET','POST'])
def new_user():
    form =UpdateAccount1()
    users = Users.query.all()
    if form.validate_on_submit():
                for o in users:
                    if o.username == form.username.data:
                        flash('Já existe um usuário com este nome tente um valor diferente')
                        return  render_template('create_user.html', 
                                form=form, legend='Novo usuário', )
                i = Users(username=form.username.data, password=form.password.data, contato=form.contato.data, city=form.city.data, street=form.street.data, number=form.number.data)
                db.session.add(i)
                db.session.commit()
                flash('Seu usuário foi criado', 'success')
                return redirect(url_for('login'))
    return render_template('create_user.html', form=form, legend='Novo usuário', )

# rota para adicionar produto
@app.route("/products/new", methods=['GET','POST'])
def newproducts():
    if current_user.id != 1:
        abort(403)
    products = Products.query.all()
    form = CreateProductForm()
    if form.validate_on_submit():
        for o in products:
            if o.title == form.title.data:
                flash('Já existe um produto com este nome')
                return  render_template('newproduct.html', title='Nova linguagem',
                           form=form, legend='Novo produto')
        picture_file = ''
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
        i = Products(title=form.title.data, subtitle=form.description.data, img=picture_file, prices=round(form.price.data, 2))
        db.session.add(i)
        db.session.commit()
        flash('Uma novo produto foi adicionada', 'success')
        return redirect(url_for('listproduct'))
    return render_template("newproduct.html", form=form, legend='Novo produto')

# rota para deletar pedido realizado do historico
@app.route("/order/delete/<order_id>", methods=['GET','POST'])
def deleteorder(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    flash('Pedido excluido do histórico', 'success')
    return redirect(url_for('historic'))
    

# função para formatar a imagem para receber no form
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/storage', picture_fn)

    output_size = (1600, 1200)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

# rota para listar produtos
@app.route("/products/list", methods=['GET','POST'])
def listproduct():
    form = CreateProductForm()
    products = Products.query.all()
    return render_template("listproducts.html", products=products, form=form)


# rota para exibir historico do cliente
@app.route("/historic", methods=['GET','POST'])
@login_required
def historic():
    if current_user.id == 1:
        abort(403)
    order = Order.query.all()
    product = Products.query.all()
 
    return render_template("historic.html", product=product, order=order)

# rota para exibir historico do adm
@app.route("/historic/adm", methods=['GET','POST'])
@login_required
def historicadm():
    if current_user.id != 1:
        abort(403)
    form = Status()
    order = Order.query.all()
    product = Products.query.all()
    users = Users.query.all()
    return render_template("historicadm.html", form=form, users=users, product=product, order=order)


# rota para criar um pedido
@app.route("/products/order/<user_id>/<product_id>", methods=['GET','POST'])
@login_required
def order(user_id, product_id):
    if current_user.id == 1:
        abort(403)
    units = Unit()
    form = CreateProductForm()
    products= Products.query.all()
    product = Products.query.get_or_404(product_id)
    user = Users.query.get_or_404(user_id)
    if units.validate_on_submit():
        i = Order(user_id=user_id, product_id=product_id, units=units.unit.data, status="Em andamento")
        db.session.add(i)
        db.session.commit()
        flash('Pedido Realizado', 'success')
        return redirect(url_for('order', user_id=user_id, product_id=product_id))
    return render_template("choiceproduct.html", units=units, products=products, form=form, user=user, product=product)


#rota para ver pedidos dos clientes
@app.route("/orders", methods=['GET','POST'])
@login_required
def orders():
    if current_user.id != 1:
        abort(403)
    form = Status()
    order = Order.query.all()
    product = Products.query.all()
    users = Users.query.all()
    return render_template("orders.html", users=users, form=form, order=order, product=product)


#rota para atualizar status do pedido
@app.route("/orders/<order_id>", methods=['GET','POST'])
@login_required
def ordersupdate(order_id):
    if current_user.id != 1:
        abort(403)
    form = Status()
    orders = Order.query.get_or_404(order_id)
    product = Products.query.all()
    if form.status.data != "finalizado":
        flash("Insira o valor corretamente","sucess")
        return redirect(url_for('orders'))
    orders.status=form.status.data
    db.session.commit()
    flash("Pedido finalizado com sucesso","sucess")
    return redirect(url_for('orders'))

# rota para excluir produto
@app.route("/product/delete/<product_id>", methods=['GET','POST'])
@login_required
def productdelete(product_id):
    if current_user.id != 1:
        abort(403)
    product = Products.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Produto excluido', 'success')
    return redirect(url_for('listproduct'))

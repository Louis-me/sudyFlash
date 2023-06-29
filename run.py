from flask import Flask, render_template, request, redirect
from util.db import MysqlDB

# 构造函数使用当前模块（__name __）的名称作为参数
app = Flask(__name__)

@app.route("/")
def hello():
    # 需要传递的数据
    str_data = "hello,world!"
    int_data = 100000
    array_data = [1, 2, 3, 4, 5, 6]
    dict_data = {"name": 'zhangsan', "age": 20}
    # render_template：渲染模板
    # 参数代表：模板html中的名称=需要传进去的数据
    return render_template("hello.html", str_data=str_data, int_data=int_data,
                           array_data=array_data, dict_data=dict_data)


@app.route("/tijiao")
def tijiao():
    # if request.method == "POST":
    return render_template("sql_insert.html")


@app.route("/info", methods=['GET', 'POST'])
def info():
    # 调用
    sql = "SELECT * from test.class"
    db = MysqlDB()
    result = db.select(sql)
    return render_template("sql_select.html", results=result)


@app.route("/submit_insert")
def submit_insert():
    return render_template("sql_insert.html")


@app.route("/insert", methods=['GET', 'POST'])
def insert():
    if request.method == "POST":
        name = request.form["name"]
        sex = request.form["sex"]
        sql = "INSERT into test.class(name,sex) VALUES ('%s','%s')" % (name, sex)
        db = MysqlDB()
        db.execute(sql)
        db.close()
        # return redirect('/info')
        return render_template("result_insert.html", results=request.form)


@app.route("/submit_update")
def submit_update():
    id = request.args.get("id")  # 获取get请求的参数
    sql = "SELECT * from test.class where id=" + id
    db = MysqlDB()
    result = db.select(sql)
    db.close()
    return render_template("sql_update.html", results=result[0])


@app.route("/update", methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        name = request.form["name"]
        sex = request.form["sex"]
        id = request.form["id"]
        db = MysqlDB()
        sql2 = "update test.class set name='%s',sex='%s' where id=%s" % (name, sex, id)
        db.execute(sql2)
        db.close()

        return render_template("result_update.html", results=request.form)


@app.route("/delete")
def delete():
    id = request.args.get("id")
    sql2 = "delete from test.class where id=" + id
    db = MysqlDB()
    db.execute(sql2)
    db.close()
    return render_template("result_delete.html", id=id)


if __name__ == "__main__":
    app.run(app.run(debug=True, port=5000, host='127.0.0.1'))

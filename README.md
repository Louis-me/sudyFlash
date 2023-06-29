# 说明

- 本项目代码主要使用flask,mysql,html实现了增删改查

- 项目环境：python3.7， win10，flask 1.1.12
- 运行入入口代码为：run.py

## 说明

- 如果要传递json怎么做

```json
 return render_template("/user/index.html")
 修改为
  return jsonify({"errno": 0, "errmsg": "登录成功", })
```

- 如何修改css js登录路径

```
# 初始化的时候，指定文件夹即可
app = Flask(__name__,template_folder="static")
```


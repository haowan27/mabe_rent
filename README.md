# Description
It is just a learning example, and maby useful for my firend zhizhang.


# Directory Structure
```
project/
├── controllers/
│   ├── __init__.py
│   ├── controller1.py
│   └── controller2.py
├── services/
│   ├── __init__.py
│   ├── service1.py
│   └── service2.py
└── persistence/
    ├── __init__.py
    ├── models.py
    └── database.py
```
# For Coding Comfortable
- python代码格式化插件使用的是black formatter, vscode应该会自动安装,[开箱即用的配置](#black-formatter配置)
- python版本3.12.3
- 启动配置文件在.vscode/launch.json, 需要安装python debuger插件

# MySQL 安装
 1. [这里下载8.4.0 lts的二进制zip](https://dev.mysql.com/downloads/mysql/)
 2. 在解压目录下新建一个[my.ini](#myini-配置示例), 它是mysql服务端的配置文件
 3. 先cd到mysql下的bin路径, 然后执行命令安装MySQL服务并指定配置文件,  路径记得替换成自己的
 - ```.\mysqld --install "MySQL" --defaults-file="D:\mysql\my.ini"```
 4. 初始化Mysql ``` .\mysqld --initialize --console ``` 这个步骤会打开一个console，里面有一串随机密码，需要保存，下文会用到
 5. 启用服务 ``` net start mysql ```
 6. 使用mysql自带客户端登录 ``` .\mysql -uroot -p ``` 输入上文中保存的密码
 7. 修改root密码 ``` ALTER USER 'root'@'localhost' IDENTIFIED BY '123459'; ```


### my.ini 配置示例
```ini
[mysqld]
#设置3306端口号
port=3306
#设置MySQL的安装目录
basedir=D:\\mysql\\mysql-8.4.0-winx64
#设置MySQL数据库的数据存放目录
datadir=D:\\mysql\\data
#运行最大连接数
max_connections=200
#运行连接失败的次数。这也是为了防止有人从该主机试图攻击数据库系统
max_connect_errors=10
#服务端使用的字符集默认为utf-8
character-set-server=utf8mb4
[mysql]
#客户端使用的字符集默认为utf8
default-character-set=utf8mb4
[client]
#客户端默认端口号为3306
port=3306
```

### black formatter配置
- Integrated formatting: Once this extension is installed in VS Code, Black will be automatically available as a formatter for Python. This is because the extension ships with a Black binary. You can ensure VS Code uses Black by default for all your Python files by setting the following in your User settings (View > Command Palette... and run Preferences: Open User Settings (JSON)):
```json
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
```
- Format on save: Automatically format your Python files on save by setting the editor.formatOnSave setting to true and the editor.defaultFormatter setting to ms-python.black-formatter. You can also enable format on save for Python files only by adding the following to your settings:
```json
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true
  }
```
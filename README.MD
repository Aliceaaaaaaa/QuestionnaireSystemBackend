# 问卷调查系统后端

开发语言：Python 3.7（>=3.5 应该可以）

数据库支持：MySQL（其他未测试 但基本支持主流数据库）

支持平台：Windows/Linux（建议Linux，异步服务Windows下只支持select模式）

开发流程及文档：https://github.com/Wh1isper/QuestionnaireSystemDoc

前端：https://github.com/JellyBeanXiewh/QuestionnaireSystemFrontend

## 安装流程

### 1. 安装依赖包

pip install -r requirements.txt

### 2. 导入数据库表

见 /db/crebas.sql

### 3. 配置数据库

见 /ORM/db_config.py

### 4. 运行app.py

# GFRobot

钉钉提醒干饭机器人。准点干饭，是打工人的基本素养。

## 提醒干饭的时间

目前会在每个工作日的 `11:55`、`17:55`、`20:55` 提醒大家干饭。

## 使用指南

1. clone 本项目
    ```bash
    git clone --depth=1 https://github.com/LucienShui/GFRobot.git
    ```
    
2. 编辑 `config.json`，填充 `token` 和 `secret` 字段
    ```bash
    cp config.example.json config.json
    ```
    
3. 安装 `requirements.txt` 依赖
    ```bash
    pip install -r requirements.txt
    ```
    
4. 启动程序
    ```bash
    python main.py
    ```

import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
import json
from email_api.agent_email_sql import Session, Agent
import logging

logger = logging.getLogger("my_logger")

# 邮件模板data样式
###data = [  ["Row 1, Column 1", "Row 1, Column 2"],
###  ["Row 2, Column 1", "Row 2, Column 2"],
###  ["Row 3, Column 1", "Row 3, Column 2"],
###]


# 邮件模板修改
def mail_template(clasue, address, data):
    # 读取列表数据并生成
    table_rows = ""
    for row in data:
        table_rows += (
            "<tr><td style='border: 1px solid black;'>{}</td><td style='border: 1px solid black;'>{}</td></tr>".format(
                row[0], row[1]
            )
        )
    # 邮件模板
    html_template = """
    <html>
    <head>
    <title>DAP shipment</title>
    </head>
    <body>
    <p>Dear team,<p>
    <p>This is a {clasue} shipment, Pls share price to us </p>
    <p>Address:</p>
    <p>{address}</p>
    <p>Details:</p>
    <table style='border-collapse: collapse;'>
        {table_rows}
    </table>
    <p>Thanks and best regards!</p>
    <p>NVOCC#SMTC-NV00275/FMCBond#026678/WCA#92530</p>
    <img src="cid:image1">
    </body>
    </html>
    """.format(
        clasue=clasue, address=address, table_rows=table_rows
    )
    return html_template


# 邮件发送
def send_mail(name, subject, data):
    try:
        # 使用split函数将邮件作为列表
        email = name.split(",")
        # 从配置文件中获取邮箱账号和密码
        with open(os.path.join(os.getcwd(), "conf", "email.json"), "r") as f:
            email_conf = json.load(f)
        # 读取签名照片
        with open(os.path.join(os.getcwd(), "conf", "signature.jpg"), "rb") as f:
            img_data = f.read()
        msg = MIMEMultipart()
        msg.attach(MIMEText(data, "html"))
        # 图片部分
        img = MIMEImage(img_data, _subtype="jpg")
        img.add_header("Content-ID", "<image1>")
        msg.attach(img)
        # 邮件发送
        msg["Subject"] = subject
        msg["From"] = f'{email_conf["name"]} <{email_conf["smtp_user"]}>'
        msg["To"] = ",".join(email)
        smtp = smtplib.SMTP_SSL(email_conf["smtp_server"], port=email_conf["smtp_port"])
        smtp.login(email_conf["smtp_user"], email_conf["smtp_password"])
        smtp.sendmail(email_conf["smtp_user"], email, msg.as_string())
        smtp.quit()
        return True
    except Exception as e:
        logger.error(e)
        return False

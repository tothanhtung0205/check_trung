# -*- coding=utf-8 -*-
# author = "tungtt"
from flask import Flask, flash , render_template, request
from werkzeug.utils import secure_filename
from check_duplicate import checking
import os
from time import time

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        t0 = time()
        f = request.files['file']
        f.save(secure_filename(f.filename))
        ff = f.filename
        print("Checking.....")
        try:
            dupli_code,dupli_ques,dupli_ans = checking(ff)
            if(len(dupli_code) == 0 and len(dupli_ques) == 0 and len(dupli_ans) ==0):
                flash(u"Không có câu nào bị trùng !")
                render_template('upload.html')
        except:
            flash(u"File check bị lỗi !!! Vui lòng chọn file docx với format chuẩn ")
            return render_template('upload.html')
        print("Checking time ")
        print(time() - t0)
        return render_template('upload.html', dup_code = dupli_code , dup_qes = dupli_ques , dup_ans = dupli_ans )

if __name__ == '__main__':
    app.run( port=2222)
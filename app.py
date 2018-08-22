from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from check_duplicate import checking
import os
from time import time

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        t0 = time()
        f = request.files['file']
        print(time()-t0)
        print("Uploading...")
        f.save(secure_filename(f.filename))
        ff = f.filename
        print("Checking.....")
        dupli_code,dupli_ques,dupli_ans = checking(ff)
        os.remove(ff)

        print("dupli code ")
        print(dupli_code)
        return render_template('upload.html', dup_code = dupli_code , dup_qes = dupli_ques , dup_ans = dupli_ans )


if __name__ == '__main__':
    app.run(port=2222)
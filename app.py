# from fileinput import filename
from flask import *
from phantich import phantichfile, ve_bieu_do

app = Flask(__name__)


@app.route('/')
def main():
  return render_template("index.html")


@app.route('/success', methods=['POST'])
def success():
  if request.method == 'POST':
    f = request.files['file']
    f.save(f.filename)
    data = phantichfile(f.filename)
    data_dict = data[1].to_dict()
    row_num = len(data_dict['Item'].keys())

    list_datasets = ve_bieu_do(f.filename)
    return render_template("acknowledgement.html",
                           name=f.filename,
                           data=data,
                           data_dict=data_dict,
                           row_num=row_num,
                           list_datasets=list_datasets)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

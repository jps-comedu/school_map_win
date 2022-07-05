from flask import Flask, render_template # flask를 FLASK의 이름으로 불러옴

app = Flask(__name__)

# 기본 주소로 접속하면 hello를 반환 -> hello 표시
@app.route('/')
def hello():
    return "hello"

@app.route('/map') # /map 접속 -> templates의 hs_map_all.html파일 응답
def map():
    return render_template("hs_map_all.html")

# main 함수
def main():
    app.run(debug=True, port=80) # flask 웹 서버 실행

# 코드를 직접 실행 -> main 함수 실행    
if __name__ == '__main__': 
    # __name__은 코드 직접 실행시 이름이 __main__임. 
    # -> 코드를 직접 실행시 조건이 참
    main()
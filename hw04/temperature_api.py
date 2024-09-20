from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    html_str = """
<!DOCTYPE html>
<html lang="kr">
<head>
<meta charset="UTF-8">
<title>Temperature_conversion</title>
</head>
<body>
<form method="GET" action="/temperature">
<h2>온도 변환하기</h2>
<label>온도 :
<input type="text" name="temp">
</label>
<button type="submit", name="convert_type", value="to_f">화씨로 바꾸기</button>
<button type="submit", name="convert_type", value="to_c">섭씨로 바꾸기</button>
</form>
</body>
</html>
"""
    return html_str

@app.route("/temperature")
def convert_temp():
    temp = request.args.get('temp')
    convert_type = request.args.get('convert_type')
    try:
        temp = float(temp)
        if convert_type == "to_f":
            result = (temp * 9 / 5) + 32
            message = f"{temp}℃ -> {result:.1f}F입니다."
        elif convert_type == "to_c":
            result = (temp - 32) * 5/9
            message = f"{temp}F -> {result:.1f}C입니다."
    except ValueError:
        message = "유효한 숫자를 입력해 주세요."
    return f"<h2>{message}</h2>"

app.run(debug=True)

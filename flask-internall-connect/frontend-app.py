from flask import Flask, render_template_string, jsonify
import requests

app = Flask(__name__)

# Backend Private IP
BACKEND_URL = "http://172.31.25.146:3000/api/message"

HTML_PAGE = """

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Frontend Flask Dashboard veera</title>

    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
        }

        body{
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            overflow:hidden;
            font-family:'Poppins', sans-serif;
            background:linear-gradient(
                135deg,
                #0f2027,
                #203a43,
                #2c5364
            );
        }

        .bg{
            position:absolute;
            width:100%;
            height:100%;
            overflow:hidden;
            z-index:0;
        }

        .bubble{
            position:absolute;
            border-radius:50%;
            background:rgba(255,255,255,0.08);
            animation:float 10s infinite ease-in-out;
        }

        .bubble:nth-child(1){
            width:220px;
            height:220px;
            top:10%;
            left:5%;
        }

        .bubble:nth-child(2){
            width:150px;
            height:150px;
            bottom:10%;
            right:10%;
            animation-delay:2s;
        }

        .bubble:nth-child(3){
            width:120px;
            height:120px;
            top:70%;
            left:20%;
            animation-delay:4s;
        }

        @keyframes float{
            0%{
                transform:translateY(0px);
            }

            50%{
                transform:translateY(-25px);
            }

            100%{
                transform:translateY(0px);
            }
        }

        .card{
            position:relative;
            z-index:1;
            width:450px;
            padding:40px;
            border-radius:25px;
            background:rgba(255,255,255,0.12);
            backdrop-filter:blur(12px);
            box-shadow:0 8px 35px rgba(0,0,0,0.4);
            text-align:center;
            color:white;
            animation:fadeIn 1s ease;
        }

        @keyframes fadeIn{
            from{
                opacity:0;
                transform:translateY(20px);
            }

            to{
                opacity:1;
                transform:translateY(0px);
            }
        }

        h1{
            font-size:34px;
            margin-bottom:10px;
            font-weight:700;
        }

        p{
            color:#d8d8d8;
            margin-bottom:30px;
            font-size:15px;
        }

        .status{
            margin-bottom:25px;
            color:#7CFC00;
            font-size:14px;
        }

        button{
            padding:15px 35px;
            border:none;
            border-radius:50px;
            background:linear-gradient(
                45deg,
                #00c6ff,
                #0072ff
            );
            color:white;
            font-size:17px;
            font-weight:600;
            cursor:pointer;
            transition:0.3s;
            box-shadow:0 4px 20px rgba(0,114,255,0.5);
        }

        button:hover{
            transform:scale(1.08);
            box-shadow:0 6px 25px rgba(0,114,255,0.8);
        }

        #result{
            margin-top:30px;
            padding:25px;
            min-height:90px;
            border-radius:18px;
            background:rgba(255,255,255,0.12);
            display:flex;
            justify-content:center;
            align-items:center;
            text-align:center;
            font-size:20px;
            font-weight:600;
            transition:0.4s;
            border:2px solid transparent;
        }

        .success{
            background:rgba(0,255,127,0.15) !important;
            border:2px solid #00ff99 !important;
            color:#00ff99;
            box-shadow:0 0 20px rgba(0,255,153,0.6);
            animation:pulse 1s infinite;
        }

        .error{
            background:rgba(255,0,0,0.12) !important;
            border:2px solid #ff4d4d !important;
            color:#ff8080;
        }

        .loading{
            color:#ffd369;
        }

        @keyframes pulse{

            0%{
                transform:scale(1);
            }

            50%{
                transform:scale(1.03);
            }

            100%{
                transform:scale(1);
            }
        }

    </style>
</head>

<body>

    <div class="bg">
        <div class="bubble"></div>
        <div class="bubble"></div>
        <div class="bubble"></div>
    </div>

    <div class="card">

        <h1>🚀 Frontend Flask EC2 veera</h1>

        <p>
            Flask Frontend Connected to Flask Backend
        </p>

        <div class="status">
            ● Internal Private IP Communication using flask
        </div>

        <button onclick="getData()">
            Fetch Backend Data
        </button>

        <div id="result">
            Waiting for backend response...
        </div>

    </div>

<script>

async function getData() {

    const result = document.getElementById("result");

    result.className = "loading";

    result.innerHTML =
        "⏳ Fetching data from backend server...";

    try {

        const response = await fetch("/get-data");

        const data = await response.json();

        result.innerHTML =
            "✅ " + data.message;

        result.className = "success";

    } catch(error) {

        result.innerHTML =
            "❌ Failed to connect backend server";

        result.className = "error";

        console.log(error);
    }
}

</script>

</body>
</html>

"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/get-data')
def get_data():

    response = requests.get(BACKEND_URL)

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

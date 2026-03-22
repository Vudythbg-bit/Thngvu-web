<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Animation</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: #111;
            overflow: hidden;
        }

        .container {
            position: relative;
            width: 450px;
            height: 450px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .container i {
            position: absolute;
            inset: 0;
            border: 2px solid #fff;
            transition: 0.5s;
        }

        .container i:nth-child(1) {
            border-radius: 38% 62% 63% 37% / 41% 44% 56% 59%;
            animation: animate 6s linear infinite;
        }

        .container i:nth-child(2) {
            border-radius: 41% 44% 56% 59% / 38% 62% 63% 37%;
            animation: animate 4s linear infinite;
        }

        .container i:nth-child(3) {
            border-radius: 50% 50% 33% 67% / 55% 27% 73% 45%;
            animation: animate2 10s linear infinite;
        }

        .container:hover i {
            border: 6px solid var(--clr);
            filter: drop-shadow(0 0 20px var(--clr));
        }

        @keyframes animate {
            0% {
                transform: rotate(0deg);
            }
            100% {
                transform: rotate(360deg);
            }
        }

        @keyframes animate2 {
            0% {
                transform: rotate(360deg);
            }
            100% {
                transform: rotate(0deg);
            }
        }

        .login {
            position: absolute;
            width: 300px;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            gap: 20px;
        }

        .login h2 {
            font-size: 2em;
            color: #fff;
        }

        .login .input-box {
            position: relative;
            width: 100%;
        }

        .login .input-box input {
            position: relative;
            width: 100%;
            padding: 12px 20px;
            background: transparent;
            border: 2px solid #fff;
            border-radius: 40px;
            font-size: 1.1em;
            color: #fff;
            outline: none;
        }

        .login .input-box input::placeholder {
            color: rgba(255, 255, 255, 0.75);
        }

        .login .input-box input[type="submit"] {
            background: linear-gradient(45deg, #0078ff, #b153d7);
            border: none;
            cursor: pointer;
            transition: 0.3s;
        }

        .login .input-box input[type="submit"]:hover {
            background: linear-gradient(45deg, #7adaa5, #0078ff);
            box-shadow: 0 0 15px #fff;
        }

        .login .links {
            width: 100%;
            display: flex;
            justify-content: space-between;
            padding: 0 5px;
        }

        .login .links a {
            color: #fff;
            text-decoration: none;
            font-size: 0.9em;
        }

        .login .links a:hover {
            color: #0ef;
        }
    </style>
</head>
<body>
    <div class="container">
        <i style="--clr:#4ca0ff;"></i>
        <i style="--clr:#7adaa5;"></i>
        <i style="--clr:#b153d7;"></i>

        <div class="login">
            <h2>Login Form</h2>

            <div class="input-box">
                <input type="text" placeholder="Username">
            </div>

            <div class="input-box">
                <input type="password" placeholder="Password">
            </div>

            <div class="input-box">
                <input type="submit" value="Sign In">
            </div>

            <div class="links">
                <a href="#">Forgot Password?</a>
                <a href="#">Sign Up</a>
            </div>
        </div>
    </div>
</body>
</html>

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
            animation: animate 7s linear infinite;
            transform: rotate(45deg);
        }

        .container i:nth-child(2) {
            animation: animate 9s linear infinite;
            transform: rotate(45deg);
        }

        .container i:nth-child(3) {
            animation: animate2 12s linear infinite;
            transform: rotate(45deg);
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
            font-size: 1.2em;
            color: #fff;
            box-shadow: none;
            outline: none;
        }

        .login .input-box input[type="submit"] {
            width: 100%;
            background: #0078ff;
            background: linear-gradient(45deg, #0078ff, #b153d7);
            border: none;
            cursor: pointer;
        }

        .login .input-box input[type="submit"]:hover {
            background: linear-gradient(45deg, #7adaa5, #0078ff);
            box-shadow: 1px 1px 20px 1px #fff;
        }

        .login .input-box input::placeholder {
            color: rgba(255, 255, 255, .75);
        }

        .login .links {
            position: relative;
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 20px;
        }

        .login .links a {
            text-decoration: none;
            color: #fff;
        }

        .login .links a:hover {
            color: #0078ff;
        }
    </style>
</head>
<body>
    <div class="container">
        <i style="--clr: #4ca0ff;"></i>
        <i style="--clr: #7adaa5;"></i>
        <i style="--clr: #b153d7;"></i>

        <div class="login">
            <h2>Login Form</h2>
            <div class="input-box">
                <input type="text" placeholder="Username" required>
            </div>
            <div class="input-box">
                <input type="password" placeholder="Password" required>
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

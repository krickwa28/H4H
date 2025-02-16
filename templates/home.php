<!DOCTYPE html>
<html>
    <head>
    <link rel="stylesheet" href="home.css">
        <style>
            .rectangle {
                width: 100%;
                height: 100%;
                background-color: #99BDC5;
            }
            .square{
                width: 5px;
                height: 50px;
                background-color: gray;
                opacity: 30%;
                border-radius: 100px;
            }
        </style>
    </head>
    <?php
        $name = $_GET["username"];
        echo ("Hello". $name."!");
    ?>

    <button className = "addplastic">Add Plastic</button>
    <body>
        <div class="rectangle"></div>
        <div class="square"></div>
        <div class="square"></div>
        <div class="square"></div>
    </body>

</html>
   
    
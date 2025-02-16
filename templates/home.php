<!DOCTYPE html>
<html>
    <head>
    </head>

    <div>
        <?php
            $Weight: {{weight}};
            if ($Weight >= 2)
                $image = "C:\Users\ktric\Downloads\animal.png"
            else 
                $image = " "
        ?>
    </div>

    <header style="text-align: center; color: white; background-color: #7ea2aa; font-size: 60px; padding: 20px 30px;">
        Hello user!
    </header>
    <h1 style="text-align: center; color: #7ea2aa; font-size: 30px;">
        Let's help save the world today :)
    </h1>
    <body style="background-color: #EEDCC3;">
        <form action = "recyclingInfo" method = "GET">
            <button class = "recyclinginfo" style="padding: 20px 30px; font-size: 30px; font-family: 'Trebuchet MS'; background-color: white; color: #99BDC5">Recycling Information</button>
        </form>
        <br>
        <img src= $image>
        <br>
    <form action = "addPlastic" method = "GET" >
        <button class = "addplastic" style="padding: 20px 30px; font-size: 30px; font-family: 'Trebuchet MS'; background-color: white; color: #99BDC5">Add Plastic</button>
    
    </body>

</html>
   
    
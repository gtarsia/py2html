unyfy
=======

A python templating engine.

What is unyfy
=======

unyfy is many things.
* A web templating engine.
* A css, html and js syntax simplifier
* An objected oriented javascript library  

The objective of unyfy is to make web code simpler, thus, more readable and easier and fun to code.

Examples speak more than words:

    css:
        Body:
            default:
                background-color=black
            hover:
                background-color=blue
        
        demo:
            default:
                background-color=black
            hover:
                background-color=blue
    
    html:
        Body:
            demo Paragraph():
                "This is a paragraph.
            DateButton()
            DateButton()
    
    js:
        class DateButton(InputButton):
            def __init__():
                onclick = display_date
                innerHTML = "Display Date"
            
            def display_date():
                demo.innerHTML = js.Date()
                
to HTML:

    h1 {
        background-color: black
    }
    h1 :hover {
        background-color: blue
    }
    id {
        background-color=black
    }
    id :hover {
        background-color=blue
    }
    
    <html>
        <body id="hello">
            <p id="demo">This is a paragraph.</p>
            <input type="button", onclick="displayDate()">Display Date</button>
            <input type="button", onclick="displayDate()">Display Date</button>
        </body>
    
        <script>
            function displayDate() {
                document.getElementById("demo").innerHTML=Date()
            }
        </script>
    </html>

I expect to develop an eclipse plugin to enjoy goodies like autocomplete and make you happy.

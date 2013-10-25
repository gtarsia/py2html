unyfy
=======

A python templating engine.

What is unyfy
=======

unyfy is a template engine, but also a web language.  
unyfy translates to css, html and js code from a Python-like syntax.  
unyfy takes many concepts from object oriented programming (even though, html is NOT a programming language)  

A unyfy code block can have parts of css, html, js and templating, but it will look like a single homogenic language.

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

unyfy aims to make web code more readable, thus easier to learn(in other words, making css, html, 
and js easier to learn at the same time), and fun.  
I expect to develop an eclipse plugin to enjoy goodies like autocomplete and make you happy.

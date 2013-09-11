unyfy
=======

A python templating engine.

What is unyfy
=======

unyfy is a template engine, but also a web language.
unyfy translates css, html and js coding to a Python-like syntax.
The template engine has also the same syntax.

A unyfy code block can have parts of css, html, js and templating, but it will look like a single homogenic language.

Examples speak more than words:

    css:
        define(style):
            if default:
                background-color=black
            if hovered:
                background-color=blue
        apply(style, tag=h1, tag=h2)
    
    html:
        body(id="hello"):
            paragraph(id=demo):
                "This is a paragraph.
            input(type="button", onclick="displayDate()"):
                "Display Date
    
    js:
        def displayDate():
            document.getElementById("demo").innerHTML=Date()

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
        </body>
    
        <script>
            function displayDate() {
                document.getElementById("demo").innerHTML=Date()
            }
        </script>
    </html>

unyfy aims to make web code readable, thus easier to learn(in other words, making css, html, 
and js easier to learn at the same time), and fun.

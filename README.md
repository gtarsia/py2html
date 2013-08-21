unyfy
=======

A python templating engine.

What is unyfy
=======

Unyfy is a template engine, but also a web language.
Unyfy translates each css, html and js syntax into its Python-like syntax.
The templating system has also the same syntax.

A Unyfy code block can have parts of css, html, js and templating, but it will look like a single homogenic language.

Examples speak more than words:

    css.define(style):
        if default
            background-color=black
        if hovered
            background-color=blue
    
    css.apply(style, tag="h1")
    css.apply(style, id="hello")
    
    html.html:
        html.body(id="hello"):
            html.paragraph(id="demo"):
                "This is a paragraph.
            html.button(type="button", onclick="displayDate()"):
                "Display Date
        js.script:
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
            <button type="button", onclick="displayDate()">Display Date</button>
        </body>
    
        <script>
            function displayDate() {
                document.getElementById("demo").innerHTML=Date()
            }
        </script>
    </html>

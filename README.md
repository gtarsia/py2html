unyfy
=======

A python templating engine.

What is unyfy
=======

Unyfy is a python templating engine and also is a css, html and javascript unifier with a similar syntax.

Examples speak more than words:

    css.new_style(style):
        if default
            background-color=black
        if hovered
            background-color=blue
    
    css.h1.style = style
    css.footer.style = style
    
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

    h1, footer {
        background-color: black
    }
    h1, footer :hover {
        background-color: blue
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

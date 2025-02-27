

def main():

    from flask import Flask, render_template

    import conf.server
    import conf.website

    app = Flask(__name__)

    @app.route("/")
    @app.route("/index.html")
    def index():
        return render_template(fr"index.html", title=conf.website.TITLE)

    @app.route("/drugaStranica.html")
    def drugaStranica():
        return render_template(fr"drugaStranica.html", title=conf.website.TITLE)

    @app.route("/trecaStranica.html")
    def trecaStranica():
        return render_template(fr"trecaStranica.html", title=conf.website.TITLE)

    app.run(
        host=conf.server.HOST,
        port=7373,
        debug=True,
    )


if __name__ == "__main__":
    main()

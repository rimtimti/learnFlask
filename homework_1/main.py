from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/clothes/")
def clothes():
    clothes_list = [
        {
            "photo": "https://storage.vsemayki.ru/images/0/3/3373/3373437/previews/people_5_man_tshirt_premium_front_melange_500.jpg",
            "name": "товар1",
            "description": "описание",
            "cost": 1000,
        },
        {
            "photo": "https://storage.vsemayki.ru/images/0/3/3373/3373437/previews/people_10_man_knit_suit_front_melange_500.jpg",
            "name": "товар2",
            "description": "описание",
            "cost": 2000,
        },
    ]
    return render_template("clothes.html", clothes_list=clothes_list)


@app.route("/jackets/")
def jackets():
    jacket_list = [
        {
            "photo": "http://steklo-foto.ru/images/phocagallery/2017/37/steklo-foto%201.jpg",
            "name": "товар1",
            "description": "описание",
            "cost": 15000,
        },
        {
            "photo": "http://steklo-foto.ru/images/phocagallery/2020/1/steklo-foto%204.jpg",
            "name": "товар2",
            "description": "описание",
            "cost": 18000,
        },
    ]
    return render_template("jackets.html", jacket_list=jacket_list)


@app.route("/shoes/")
def shoes():
    shoes_list = [
        {
            "photo": "https://img.freepik.com/premium-photo/shoes-on-a-white-background_192247-37.jpg",
            "name": "товар1",
            "description": "описание",
            "cost": 5000,
        },
        {
            "photo": "https://img.freepik.com/free-photo/men-shoes_1203-8433.jpg",
            "name": "товар2",
            "description": "описание",
            "cost": 8000,
        },
    ]
    return render_template("shoes.html", shoes_list=shoes_list)


if __name__ == "__main__":
    app.run(debug=True)

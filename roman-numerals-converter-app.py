from flask import Flask, render_template, request

app = Flask(__name__)

def convert(decimal_num):
  roman_numerals = { 1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }
  roman_numeral = ""
  
  for value, roman_symbol in roman_numerals.items():
    while decimal_num >= value:
      roman_numeral += roman_symbol
      decimal_num -= value
  return roman_numeral


@app.route('/', methods=["POST", "GET"])
def calculate():
  if request.method == "POST":
    alpha=request.form.get("number")
    if not alpha.isdecimal():
      return render_template("index.html", Developer_Name = "Sait Y", not_valid = True)
    number = int(alpha)
    if not 0 < number < 4000:
      return render_template("index.html", Developer_Name = "Sait Y", not_valid = True)
    return render_template("result.html", number_decimal = number, number_roman = convert(number), Developer_Name = "Sait")
  else:
    return render_template("index.html", Developer_Name = "Sait Y", not_valid = False)



if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)

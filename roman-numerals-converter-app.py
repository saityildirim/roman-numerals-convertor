from flask import Flask, render_template, request
app = Flask(__name__)

def int_to_roman(number):
  """Converts an integer to a Roman numeral.
  Args:
      number: An integer between 1 and 3999.
  Returns:
      The Roman numeral representation of the number.
  """
      
  roman_numerals = { 1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL",
      10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }

  roman_numeral = ""
  for value, numeral in roman_numerals.items():
    while number >= value:
      roman_numeral += numeral
      number -= value

  return roman_numeral


@app.route('/', methods=["GET", "POST"])
def calculate():
  if request.method == "POST":
    num=request.form.get("number")
    return render_template("result.html", number_decimal=int(num), number_roman=int_to_roman(int(num)), Developer_Name = "Sait")
  else:
<<<<<<< HEAD
    return render_template("index.html", Developer_Name = "Sait")
=======
    return render_template("index.html", Developer_Name = "Sait" )
>>>>>>> 00d2203954bb1f1a261b7f88066379fc9b48f4a8



if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=8080)

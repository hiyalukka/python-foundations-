{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNawUdYal7Frnx+xmZWkm2z",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/hiyalukka/python-foundations-/blob/main/Variables.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "3rE5SBR8SoWj"
      },
      "outputs": [],
      "source": [
        "#Problem 01\n",
        "#Your personal info store\n",
        "#Create variables for your name, age, city, and whether you're a student. Print each one with a label. Use the correct data type for each."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"Hiya\"\n",
        "age = 18\n",
        "City = \"Rajkot\"\n",
        "Student = True\n",
        "\n",
        "print(type(name))\n",
        "print(type(age))\n",
        "print(type(City))\n",
        "print(type(Student))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "du_T1ukiSyHl",
        "outputId": "aa8f6b90-b919-4176-a449-eaf208dfed84"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'str'>\n",
            "<class 'int'>\n",
            "<class 'str'>\n",
            "<class 'bool'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 02\n",
        "#Type detective\n",
        "#Create one variable of each type: int, float, str, bool. Print each variable AND its type using type(). Format the output neatly."
      ],
      "metadata": {
        "id": "Rs37FmbxTNFU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"Hiya\"\n",
        "age = 18\n",
        "country = \"India\"\n",
        "student = True\n",
        "percentage = 98.99\n",
        "\n",
        "print(name)\n",
        "print(age)\n",
        "print(country)\n",
        "print(student)\n",
        "print(percentage)\n",
        "print(type(name))\n",
        "print(type(age))\n",
        "print(type(country))\n",
        "print(type(student))\n",
        "print(type(percentage))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p3_DrvzYTVkc",
        "outputId": "b575b4c5-d512-4738-ef23-805b762ae0e5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hiya\n",
            "18\n",
            "India\n",
            "True\n",
            "98.99\n",
            "<class 'str'>\n",
            "<class 'int'>\n",
            "<class 'str'>\n",
            "<class 'bool'>\n",
            "<class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 03\n",
        "#Type conversion chain\n",
        "#Start with the string '3.14'. Convert it to float, then to int, then back to string. Print the value AND type at each step. What do you notice about the int conversion?"
      ],
      "metadata": {
        "id": "kmRA_TR8UUY7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "pie = '3.14'\n",
        "pie = float(pie)\n",
        "print(\"Value of pie :\", pie)\n",
        "print(\"Type:\", type(pie))\n",
        "pie = int(pie)\n",
        "print(\"Value of pie\", pie)\n",
        "print(\"Type:\", type(pie))\n",
        "pie = str(pie)\n",
        "print(\"Value of pie\", pie)\n",
        "print(\"Type:\", type(pie))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VtUgXOrMUcRs",
        "outputId": "f70c3032-220c-46df-8ffe-3eeacdd71de1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Value of pie : 3.14\n",
            "Type: <class 'float'>\n",
            "Value of pie 3\n",
            "Type: <class 'int'>\n",
            "Value of pie 3\n",
            "Type: <class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 04\n",
        "#Smart receipt printer\n",
        "#You bought 3 items. Store item name, quantity, and price per unit as separate variables. Calculate total cost. Print a formatted receipt using f-strings — show the item, qty, unit price, and total."
      ],
      "metadata": {
        "id": "XtULBp6WXiTI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "item1 = \"Milk\"\n",
        "item2 = \"Chocolates\"\n",
        "item3 = \"cookies\"\n",
        "\n",
        "quat_item1 = 15\n",
        "quat_item2 = 10\n",
        "quat_item3 = 7\n",
        "\n",
        "price_item1 = 20\n",
        "price_item2 = 30\n",
        "price_item3 = 4\n",
        "\n",
        "total_cost = (quat_item1 * price_item1) + (quat_item2 * price_item2) + (quat_item3 * price_item3)\n",
        "\n",
        "print(\"--------- RECEIPT ---------\")\n",
        "print(f\"Item: {item1}, Quantity: {quat_item1}, Unit Price: ₹{price_item1}, Total: {quat_item1 * price_item1}\")\n",
        "print(f\"Item: {item2}, Quantity: {quat_item2}, Unit Price: ₹{price_item2}, Total: {quat_item2 * price_item2}\")\n",
        "print(f\"Item: {item3}, Quantity: {quat_item3}, Unit Price: ₹{price_item3}, Total: {quat_item3 * price_item3}\")\n",
        "print(f\"Total Cost: {total_cost}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vkBXmRfUXmkL",
        "outputId": "c827ded9-cc32-4f07-f971-a2f60ffbfe6d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--------- RECEIPT ---------\n",
            "Item: Milk, Quantity: 15, Unit Price: ₹20, Total: 300\n",
            "Item: Chocolates, Quantity: 10, Unit Price: ₹30, Total: 300\n",
            "Item: cookies, Quantity: 7, Unit Price: ₹4, Total: 28\n",
            "Total Cost: 628\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 05\n",
        "#String inspector\n",
        "#Take any sentence as a string variable. Print: its length, it in ALL CAPS, it in all lowercase, the first word only, and whether the word 'python' appears in it (True/False)."
      ],
      "metadata": {
        "id": "zbmdRLWoagd8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sentence = \"My name is Hiya\"\n",
        "print(len(sentence))\n",
        "print(sentence.upper())\n",
        "print(sentence.lower())\n",
        "print(sentence.split()[0])\n",
        "print('python' in sentence)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2KeSUSAiajzL",
        "outputId": "048fb0dc-f18b-4d7f-a181-fa4a2159d5e9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n",
            "MY NAME IS HIYA\n",
            "my name is hiya\n",
            "My\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 06\n",
        "#The swap\n",
        "#Create two variables a = 10 and b = 25. Swap their values WITHOUT using a third variable. Print before and after."
      ],
      "metadata": {
        "id": "RtBBxQO2cY70"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "a = (10)\n",
        "b = (25)\n",
        "\n",
        "print(type(a))\n",
        "print(type(b))\n",
        "\n",
        "print(a)\n",
        "print(b)\n",
        "a , b = b , a\n",
        "\n",
        "print(a)\n",
        "print(b)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fgTu517lce6_",
        "outputId": "32c37e2d-7544-41d3-a0ea-31e360504beb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n",
            "<class 'int'>\n",
            "10\n",
            "25\n",
            "25\n",
            "10\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 07\n",
        "#BMI calculator\n",
        "#Take weight (kg) and height (m) as float variables. Calculate BMI = weight / height². Print the result rounded to 2 decimal places, and a string category: Underweight, Normal, Overweight, or Obese."
      ],
      "metadata": {
        "id": "jdzjDFRYezM9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "weight = float(input(\"Enter your weight in kg: \"))\n",
        "height = float(input(\"Enter your height in meters:\"))\n",
        "\n",
        "BMI = weight / (height ** 2)\n",
        "\n",
        "print(f\"Your BMI is: {BMI:.2f}\")\n",
        "if (BMI < 18.5):\n",
        "    print(\"Underweight\")\n",
        "elif (BMI >= 18.5 and BMI < 24.9):\n",
        "    print(\"Normal\")\n",
        "elif (BMI >= 24.9 and BMI < 29.9):\n",
        "    print(\"Overweight\")\n",
        "else :\n",
        "    print(\"Obese\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_yWFqPjCe2zo",
        "outputId": "e8af7d44-5249-4e44-fd13-b2f87357e239"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your weight in kg: 45\n",
            "Enter your height in meters:1.64\n",
            "Your BMI is: 16.73\n",
            "Underweight\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 08\n",
        "#Multiline f-string formatter\n",
        "#Store a student's name, subject, marks (out of 100), and grade as variables. Print a formatted report card using an f-string that spans multiple lines. The output should look like an actual report card."
      ],
      "metadata": {
        "id": "TgCmmpziglHr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"Hiya\"\n",
        "subject = \"Computer\"\n",
        "marks = 95\n",
        "grade = \"A\"\n",
        "\n",
        "print(f\"\"\"\n",
        "--- REPORT CARD ---\n",
        "Student Name: {name}\n",
        "Subject:      {subject}\n",
        "Marks:        {marks}\n",
        "Grade:        {grade}\n",
        "\n",
        "\"\"\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8wx6slK5gs69",
        "outputId": "2c3a1eed-89ea-474b-e96a-2a561329879e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "--- REPORT CARD ---\n",
            "Student Name: Hiya\n",
            "Subject:      Computer\n",
            "Marks:        95\n",
            "Grade:        A\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 09\n",
        "#The boolean logic tester\n",
        "#Create variables: age=20, has_id=True, is_member=False. Print the result of at least 5 different boolean expressions using and, or, not. For each, also print a plain English explanation of what it checked."
      ],
      "metadata": {
        "id": "L49NbGeSjVw5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "age=20\n",
        "has_id=True\n",
        "is_member=False\n",
        "\n",
        "print(\"Is this person an adult with valid ID?\")\n",
        "print(age >= 18 and has_id)\n",
        "\n",
        "print(\"Is this person a member or an adult?\")\n",
        "print(is_member or age >= 18)\n",
        "\n",
        "print(\"Is this person an adult and not a member?\")\n",
        "print(age >= 18 and not is_member)\n",
        "\n",
        "print(\"Is this person an adult or a member?\")\n",
        "print(age >= 18 or is_member)\n",
        "\n",
        "print(\"Is this person an adult and a member?\")\n",
        "print(age >= 18 and is_member)\n",
        "\n",
        "print(\"Is this person not a member?\")\n",
        "print(not is_member)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "38sLiJgxjYvA",
        "outputId": "30a43123-af0d-4ac5-b0bc-ad0de24d4244"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Is this person an adult with valid ID?\n",
            "True\n",
            "Is this person a member or an adult?\n",
            "True\n",
            "Is this person an adult and not a member?\n",
            "True\n",
            "Is this person an adult or a member?\n",
            "True\n",
            "Is this person an adult and a member?\n",
            "False\n",
            "Is this person not a member?\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 10\n",
        "#Mini profile builder\n",
        "#Ask yourself: what 6 pieces of data fully describe a person? Use at least 3 different data types. Store all 6, then print a nicely formatted profile. No input() — hardcode values. Make the output look presentable."
      ],
      "metadata": {
        "id": "tTTwMrDmlYrb"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "name = \"Hiya\"\n",
        "age = 18\n",
        "percent_12 = 98.99\n",
        "percent_10 = 98.99\n",
        "percent_graduation = 98.9\n",
        "is_student = True\n",
        "\n",
        "print(\"--------- PROFILE --------\")\n",
        "print(f\"Name: {name}\")\n",
        "print(f\"Age: {age}\")\n",
        "print(f\"12th Percentage: {percent_12}\")\n",
        "print(f\"10th Percentage: {percent_10}\")\n",
        "print(f\"Graduation Percentage: {percent_graduation}\")\n",
        "print(f\"Is Student: {is_student}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pp9oyXTfldhT",
        "outputId": "d0c8a85d-8339-4dfb-b6b0-a87b7158bcd6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--------- PROFILE --------\n",
            "Name: Hiya\n",
            "Age: 18\n",
            "12th Percentage: 98.99\n",
            "10th Percentage: 98.99\n",
            "Graduation Percentage: 98.9\n",
            "Is Student: True\n"
          ]
        }
      ]
    }
  ]
}
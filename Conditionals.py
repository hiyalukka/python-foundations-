{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPi2r03cJcJJvFLsuym5HWw",
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
        "<a href=\"https://colab.research.google.com/github/hiyalukka/python-foundations-/blob/main/Conditionals.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yG_VIabP9-hb"
      },
      "outputs": [],
      "source": [
        "#Problem 01\n",
        "#Positive, negative, or zero\n",
        "#Take a number as input. Print whether it is positive, negative, or zero. Simple if-elif-else — get your fingers moving."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "number = int(input(\"Enter a number: \"))\n",
        "if number > 0:\n",
        "    print(\"The number is positive.\")\n",
        "elif number < 0:\n",
        "    print(\"The number is negative.\")\n",
        "else:\n",
        "    print(\"The number is zero.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "f7uR_ooj-I_m",
        "outputId": "4080b17d-a04f-47e2-8b7c-505e5e32464f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: -45\n",
            "The number is negative.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 02\n",
        "#Even or odd\n",
        "#Take a number as input. Print whether it is even or odd. Also print whether it is divisible by 5. Two separate checks."
      ],
      "metadata": {
        "id": "-DQoxYoZ-ZwZ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "number = int(input(\"Enter a number: \"))\n",
        "if number % 2 == 0:\n",
        "    print(\"The number is even.\")\n",
        "else:\n",
        "    print(\"The number is odd.\")\n",
        "if number % 5 == 0:\n",
        "    print(\"The number is divisible by 5.\")\n",
        "else:\n",
        "    print(\"The number is not divisible by 5.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3geMpqvF-fXe",
        "outputId": "d6e8bcc1-2f06-4d62-ba18-027db3ad925c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: -78\n",
            "The number is even.\n",
            "The number is not divisible by 5.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 03\n",
        "#Voting eligibility\n",
        "#Take age as input. Print whether the person can vote, is too young to vote, or is a senior citizen (65+). Make sure all age ranges are covered with no gaps."
      ],
      "metadata": {
        "id": "UGbcRwgN_A3o"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "age = int(input(\"Enter your age: \"))\n",
        "if age < 18:\n",
        "    print(\"You are too young to vote.\")\n",
        "elif age >= 18 and age < 65:\n",
        "    print(\"You are eligible to vote.\")\n",
        "else:\n",
        "    print(\"You are a senior citizen.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bjEIY5Nz_HQe",
        "outputId": "6c66434d-90ab-46e5-cafd-6b60c092b62b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your age: 21\n",
            "You are eligible to vote.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 04\n",
        "#Grade calculator\n",
        "#Take marks (0–100) as input. Print the letter grade: A (90–100), B (75–89), C (60–74), D (45–59), F (below 45). Also print 'Invalid' if marks are outside 0–100.\n"
      ],
      "metadata": {
        "id": "4nLKIUgI_9RX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "marks = int(input(\"Enter your marks: \"))\n",
        "if marks < 0 or marks > 100:\n",
        "    print(\"Invalid\")\n",
        "elif marks >= 90:\n",
        "    print(\"A\")\n",
        "elif marks >= 75 and marks < 90:\n",
        "    print(\"B\")\n",
        "elif marks >= 60 and marks < 75:\n",
        "    print(\"C\")\n",
        "elif marks >= 45 and marks < 60:\n",
        "    print(\"D\")\n",
        "elif marks < 45:\n",
        "    print(\"F\")\n",
        "else:\n",
        "    print(\"Invalid\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0jj_kKolAAgq",
        "outputId": "4ec83e70-ac94-48f0-c2dd-f904d377fb33"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your marks: 89\n",
            "B\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 05\n",
        "#Electricity bill calculator\n",
        "#Units consumed: 0–100 units @ ₹5/unit, 101–300 @ ₹8/unit, above 300 @ ₹12/unit. Take units as input, calculate and print the total bill. Add a surcharge of 10% if bill exceeds ₹2000."
      ],
      "metadata": {
        "id": "soTnI2VMAivE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "units = int(input(\"Enter the number of units consumed: \"))\n",
        "if units <= 100 and units >= 0:\n",
        "    bill = units * 5\n",
        "elif units <= 300:\n",
        "    bill = 100 * 5 + (units - 100) * 8\n",
        "else:\n",
        "    bill = 100 * 5 + 200 * 8 + (units - 300) * 12\n",
        "\n",
        "if bill > 2000:\n",
        "    bill = bill * 1.1\n",
        "\n",
        "print(f\"Total bill: ₹{bill}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D3JBRjX9BNcT",
        "outputId": "a37ac74b-c5bc-406a-dc3a-f0a6366d5e02"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the number of units consumed: 305\n",
            "Total bill: ₹2376.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 06\n",
        "#Leap year checker\n",
        "#Take a year as input. Print whether it is a leap year or not. A year is a leap year if: divisible by 4, EXCEPT centuries (divisible by 100) which must also be divisible by 400.\n"
      ],
      "metadata": {
        "id": "uX1Xna7WJn02"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "year = int(input(\"Enter a year: \"))\n",
        "if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n",
        "    print(f\"{year} is a leap year.\")\n",
        "else:\n",
        "    print(f\"{year} is not a leap year.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QVIezWGkJxUE",
        "outputId": "9bc1fc3d-a5be-4de8-9939-780ea164c6ca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a year: 2026\n",
            "2026 is not a leap year.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 07\n",
        "#Triangle validator\n",
        "#Take three sides as input. First check if they form a valid triangle (sum of any two sides must be greater than the third). If valid, classify it: equilateral, isosceles, or scalene."
      ],
      "metadata": {
        "id": "BVp6isEyKpmg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "side_1 = int(input(\"Enter the first side: \"))\n",
        "side_2 = int(input(\"Enter the second side: \"))\n",
        "side_3 = int(input(\"Enter the third side: \"))\n",
        "\n",
        "if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_3:\n",
        "    if side_1 == side_2 == side_3:\n",
        "        print(\"Equilateral\")\n",
        "    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:\n",
        "        print(\"Isosceles\")\n",
        "    else:\n",
        "        print(\"Scalene\")\n",
        "else:\n",
        "    print(\"Not a valid triangle\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2JDh1_a-KroZ",
        "outputId": "a4a18638-4067-4465-9aa7-c659a5108729"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the first side: 12\n",
            "Enter the second side: 6\n",
            "Enter the third side: 7\n",
            "Scalene\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 08\n",
        "#Simple ATM\n",
        "#Set a balance and a PIN. Take PIN input — if wrong, print 'Access denied'. If correct, ask for withdrawal amount. Check if sufficient balance exists. Print updated balance or 'Insufficient funds'.\n"
      ],
      "metadata": {
        "id": "97OtHtKIMeSM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "PIN = 224422\n",
        "balance = 10000\n",
        "PIN = int(input(\"Enter your PIN: \"))\n",
        "\n",
        "if PIN != 224422:\n",
        "   print(\"Access denied\")\n",
        "else :\n",
        "\n",
        "   withdrawal = int(input(\"Enter the amount to withdraw: \"))\n",
        "   if withdrawal > balance:\n",
        "      print(\"Insufficient funds\")\n",
        "   else:\n",
        "      balance = balance - withdrawal\n",
        "      print(\"Your updated balance is: \", balance)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Lw72241aLEQN",
        "outputId": "c510d4b0-af35-4fe8-feaa-b0119d4c26ea"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your PIN: 224422\n",
            "Enter the amount to withdraw: 6000\n",
            "Your updated balance is:  4000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 09\n",
        "#Season and weather advisor\n",
        "#Take month (1–12) and temperature as input. Print the season (summer/monsoon/winter/spring). Then based on season AND temperature, print one clothing recommendation. Use both conditions together."
      ],
      "metadata": {
        "id": "bRWzJBAvPdA7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "month = int(input(\"Enter the month (1-12): \"))\n",
        "temperature = int(input(\"Enter the temperature: \"))\n",
        "print(\"Month: \", month)\n",
        "print(\"Temperature: \", temperature)\n",
        "if month == 11 or month == 12 or month == 1 or month == 2:\n",
        "    season = \"Winter\"\n",
        "elif month ==4 or month ==5 or month==6:\n",
        "    season = \"Summer\"\n",
        "elif month == 7 or month == 8 or month ==9 :\n",
        "    season = \"Monsoon\"\n",
        "else:\n",
        "    season = \"Spring\"\n",
        "\n",
        "print(f\"Season: {season}\")\n",
        "\n",
        "if season == \"Winter\" and temperature < 15:\n",
        "    print(\"Wear a woolen sweater\")\n",
        "elif season == \"Winter\" and temperature >= 15:\n",
        "    print(\"Wear a light sweater\")\n",
        "elif season == \"Summer\" and temperature < 15:\n",
        "    print(\"Wear light jacket\")\n",
        "elif season == \"Summer\" and temperature >= 15:\n",
        "    print(\"Wear light colored cotton clothes and a scarf\")\n",
        "elif season == \"Monsoon\" and temperature < 15:\n",
        "    print(\"Wear a light jacket\")\n",
        "elif season == \"Monsoon\" and temperature >= 15:\n",
        "    print(\"Wear a light jacket and a scarf and keep a raincoat\")\n",
        "elif season == \"Spring\" and temperature < 15:\n",
        "    print(\"Wear a light t-shirts and tops\")\n",
        "elif season == \"Spring\" and temperature >= 15:\n",
        "    print(\"Wear a light cotton clothes and a scarf\")\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vuC8RQlNPgOn",
        "outputId": "2952246a-d2f3-486f-c763-838ac486f6f7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the month (1-12): 2\n",
            "Enter the temperature: 25\n",
            "Month:  2\n",
            "Temperature:  25\n",
            "Season: Winter\n",
            "Wear a light sweater\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 10\n",
        "#College admission decider\n",
        "#A college admits students based on: marks >= 85 AND age between 17–22, OR marks >= 75 AND has_scholarship = True. Take all inputs, print admitted or rejected, and a reason why."
      ],
      "metadata": {
        "id": "vWcAaHwUUBoC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "age = int(input(\"Enter your age: \"))\n",
        "marks = int(input(\"Enter your marks: \"))\n",
        "has_scholarship = input(\"Do you have a scholarship? (True/False): \")\n",
        "\n",
        "if marks >= 85 and 17 <= age <= 22:\n",
        "    reason = \"Marks >= 85 and age between 17-22\"\n",
        "elif marks >= 75 and has_scholarship == \"True\":\n",
        "    reason = \"Marks >= 75 and has scholarship\"\n",
        "elif marks >= 75 and has_scholarship == \"True\" and not (17 <= age <= 22):\n",
        "    reason = \"Scholarship criteria met but age is not in valid range\"\n",
        "else:\n",
        "    reason = \"Did not meet any admission criteria\"\n",
        "\n",
        "if (marks >= 85 and 17 <= age <= 22) or (marks >= 75 and has_scholarship == \"True\"):\n",
        "    print(\"Admitted\")\n",
        "\n",
        "else:\n",
        "    print(\"Rejected\")\n",
        "\n",
        "print(f\"Reason: {reason}\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4dlxKxWcUE6i",
        "outputId": "f58515b5-7c11-4260-ec4d-377ed8ce3167"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your age: 15\n",
            "Enter your marks: 99\n",
            "Do you have a scholarship? (True/False): true\n",
            "Rejected\n",
            "Reason: Did not meet any admission criteria\n"
          ]
        }
      ]
    }
  ]
}
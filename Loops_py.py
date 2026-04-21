{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO2YIxIFHcewcXNBhzT1ud6",
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
        "<a href=\"https://colab.research.google.com/github/hiyalukka/python-foundations-/blob/main/Loops_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "-IBpeU4Evtoi"
      },
      "outputs": [],
      "source": [
        "#Problem 01\n",
        "#Count to N\n",
        "#Take a number N as input. Print all numbers from 1 to N using a for loop. Then do the same using a while loop. Two separate outputs."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "N = int(input(\"Enter a number: \"))\n",
        "for i in range(1, N+1):\n",
        "    print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ejv_wmS2v18L",
        "outputId": "367a329c-c3cb-4f00-f528-ae8ef171cbdb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 5\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "N = int(input(\"Enter a number: \"))\n",
        "i = 1\n",
        "while i <= N:\n",
        "    print(i)\n",
        "    i += 1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EcCPcYBkwdMB",
        "outputId": "5341b76d-1bfc-4823-b310-a6bb59e9da48"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 5\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 02\n",
        "#Sum and average\n",
        "#Take N as input. Calculate the sum of all numbers from 1 to N using a loop. Then calculate and print the average. No formulas — use a loop to add one by one."
      ],
      "metadata": {
        "id": "0AQm30QoxB0q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "N = int(input(\"Enter a number: \"))\n",
        "sum = 0\n",
        "for i in range(1, N+1):\n",
        "    sum += i\n",
        "print(\"The sum of all numbers from 1 to\", N, \"is\", sum)\n",
        "\n",
        "average = sum / N\n",
        "print(\"The average of all numbers from 1 to\", N, \"is\", average)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mzZHCPhOxEzK",
        "outputId": "719dbe6d-ab62-48ee-ff9c-a854edd9d880"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 5\n",
            "The sum of all numbers from 1 to 5 is 15\n",
            "The average of all numbers from 1 to 5 is 3.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 03\n",
        "#Multiplication table\n",
        "#Take a number as input. Print its multiplication table from 1 to 10. Format it neatly: '7 x 3 = 21'."
      ],
      "metadata": {
        "id": "S5QjVS6vxnn9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "N = int(input(\"Enter a number: \"))\n",
        "for i in range(1, 11):\n",
        "    print(N, \"x\", i, \"=\", N*i)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9iv7O51Uxum1",
        "outputId": "45ad5624-5eb3-4e58-9538-39ae0a8e1afe"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 7\n",
            "7 x 1 = 7\n",
            "7 x 2 = 14\n",
            "7 x 3 = 21\n",
            "7 x 4 = 28\n",
            "7 x 5 = 35\n",
            "7 x 6 = 42\n",
            "7 x 7 = 49\n",
            "7 x 8 = 56\n",
            "7 x 9 = 63\n",
            "7 x 10 = 70\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 04\n",
        "#Reverse countdown\n",
        "#Take N as input. Print a countdown from N to 1 using a while loop, then print 'Blast off!' at the end. Then do the same using a for loop with range()."
      ],
      "metadata": {
        "id": "_z4rNuhTx-oa"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "N = int(input(\"Enter a number: \"))\n",
        "while N > 0:\n",
        "    print(N)\n",
        "    N -= 1\n",
        "print(\"Blast off!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YyDOOj16yE9T",
        "outputId": "970e7ae4-959e-45c6-c23f-328c5443ff86"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 7\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n",
            "Blast off!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "N = int(input(\"Enter a number: \"))\n",
        "for i in range(N, 0, -1):\n",
        "    print(i)\n",
        "print(\"Blast off!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JFdwPzLYzEfB",
        "outputId": "1a4c5033-f6fd-40e7-f761-913fd0b6b751"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 7\n",
            "7\n",
            "6\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n",
            "Blast off!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 05\n",
        "#Factorial calculator\n",
        "#Take a number N as input. Calculate its factorial using a loop. Print the result. Handle the edge case: factorial of 0 is 1."
      ],
      "metadata": {
        "id": "cqEX2AqWzNLm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "N = int(input(\"Enter a number: \"))\n",
        "factorial = 1\n",
        "for i in range(1, N+1):\n",
        "    factorial *= i\n",
        "print(\"The factorial of\", N, \"is\", factorial)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZurGW6RDzPmh",
        "outputId": "597b2ad3-47a7-45d0-97cd-5fa86232b706"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 0\n",
            "The factorial of 0 is 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 06\n",
        "#Number pattern\n",
        "#Print this pattern for N=5 using nested loops:\n",
        "#1\n",
        "#1 2\n",
        "#1 2 3\n",
        "#1 2 3 4\n",
        "#1 2 3 4 5"
      ],
      "metadata": {
        "id": "heRb0X2VznWG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "N = 5\n",
        "\n",
        "for i in range(1, N + 1):        # outer loop for rows\n",
        "    for j in range(1, i + 1):    # inner loop for numbers\n",
        "        print(j, end=\" \")\n",
        "    print()  # move to next line after each row"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7BoBqxidzrYr",
        "outputId": "e73c92ba-d1af-4cc6-9db2-87acba624918"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 \n",
            "1 2 \n",
            "1 2 3 \n",
            "1 2 3 4 \n",
            "1 2 3 4 5 \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 07\n",
        "#FizzBuzz\n",
        "#Print numbers 1 to 50. But: print 'Fizz' for multiples of 3, 'Buzz' for multiples of 5, 'FizzBuzz' for multiples of both. This is one of the most famous coding problems — solve it cleanly.\n"
      ],
      "metadata": {
        "id": "ReDSO8aN1p1V"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1, 51):\n",
        "    if i % 3 == 0 and i % 5 == 0:\n",
        "        print(\"FizzBuzz\")\n",
        "    elif i % 3 == 0:\n",
        "        print(\"Fizz\")\n",
        "    elif i % 5 == 0:\n",
        "        print(\"Buzz\")\n",
        "    else:\n",
        "        print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aEILjeBj1uY6",
        "outputId": "7fff97aa-e170-4044-d54a-9572342fbcec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "Fizz\n",
            "4\n",
            "Buzz\n",
            "Fizz\n",
            "7\n",
            "8\n",
            "Fizz\n",
            "Buzz\n",
            "11\n",
            "Fizz\n",
            "13\n",
            "14\n",
            "FizzBuzz\n",
            "16\n",
            "17\n",
            "Fizz\n",
            "19\n",
            "Buzz\n",
            "Fizz\n",
            "22\n",
            "23\n",
            "Fizz\n",
            "Buzz\n",
            "26\n",
            "Fizz\n",
            "28\n",
            "29\n",
            "FizzBuzz\n",
            "31\n",
            "32\n",
            "Fizz\n",
            "34\n",
            "Buzz\n",
            "Fizz\n",
            "37\n",
            "38\n",
            "Fizz\n",
            "Buzz\n",
            "41\n",
            "Fizz\n",
            "43\n",
            "44\n",
            "FizzBuzz\n",
            "46\n",
            "47\n",
            "Fizz\n",
            "49\n",
            "Buzz\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 08\n",
        "#Digit sum and reversal\n",
        "#Take a number as input. Using a while loop, calculate the sum of its digits. Also reverse the number. Print both. No string conversion allowed — use math only."
      ],
      "metadata": {
        "id": "tMDI9c-12saG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "n = int(input(\"Enter a number: \"))\n",
        "\n",
        "original = n\n",
        "sum_digits = 0\n",
        "reverse = 0\n",
        "\n",
        "while n > 0:\n",
        "    digit = n % 10          # extract last digit\n",
        "    sum_digits += digit     # add to sum\n",
        "    reverse = reverse * 10 + digit  # build reverse\n",
        "    n = n // 10             # remove last digit\n",
        "\n",
        "print(\"Sum of digits:\", sum_digits)\n",
        "print(\"Reversed number:\", reverse)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7vVGocH_3yO0",
        "outputId": "5dba3b9e-f63e-42b9-dfb8-984387eb3d55"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 123\n",
            "Sum of digits: 6\n",
            "Reversed number: 321\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 09\n",
        "#Prime number checker and lister\n",
        "#First: take a number and check if it's prime. Then: print all prime numbers between 1 and 100. Two parts, both using loops."
      ],
      "metadata": {
        "id": "c7C5JnVr4fMc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "num_to_check = int(input(\"Enter a number: \"))\n",
        "is_prime = True\n",
        "\n",
        "if num_to_check < 2:\n",
        "    is_prime = False\n",
        "else:\n",
        "\n",
        "    for i in range(2, num_to_check):\n",
        "        if num_to_check % i == 0:\n",
        "            is_prime = False\n",
        "            break\n",
        "\n",
        "if is_prime:\n",
        "    print(f\"{num_to_check} is prime.\")\n",
        "else:\n",
        "    print(f\"{num_to_check} is not prime.\")\n",
        "\n",
        "\n",
        "\n",
        "print(\"Primes between 1 and 100:\")\n",
        "\n",
        "for n in range(1, 101):\n",
        "\n",
        "    if n < 2:\n",
        "        continue\n",
        "\n",
        "\n",
        "    is_prime_loop = True\n",
        "    for i in range(2, n):\n",
        "        if n % i == 0:\n",
        "            is_prime_loop = False\n",
        "            break\n",
        "\n",
        "    if is_prime_loop:\n",
        "        print(n, end=\" \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JCqhxL-t4h5D",
        "outputId": "2da3e44f-8149-4002-ff85-9094ebaa7b0e"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 3\n",
            "3 is prime.\n",
            "Primes between 1 and 100:\n",
            "2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Problem 10\n",
        "#Simple number guessing game\n",
        "#Set a secret number. Use a while loop to keep asking the user to guess. Tell them 'Too high', 'Too low', or 'Correct!' after each guess. Count how many attempts it took. Print the attempt count when they win."
      ],
      "metadata": {
        "id": "bIdq1zdgdtmd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "secret_number = 42\n",
        "guess = 0\n",
        "attempts = 0\n",
        "\n",
        "print(\"Welcome to the Guessing Game!\")\n",
        "\n",
        "\n",
        "while guess != secret_number:\n",
        "\n",
        "    guess = int(input(\"Enter your guess: \"))\n",
        "    attempts = attempts + 1\n",
        "\n",
        "\n",
        "    if guess > secret_number:\n",
        "        print(\"Too high!\")\n",
        "    elif guess < secret_number:\n",
        "        print(\"Too low!\")\n",
        "    else:\n",
        "        print(\"Correct!\")\n",
        "\n",
        "\n",
        "print(f\"It took you {attempts} attempts to win.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yYAgXz9gdwvr",
        "outputId": "e902062a-38af-40fd-f43d-1c5534e034fb"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to the Guessing Game!\n",
            "Enter your guess: 4\n",
            "Too low!\n",
            "Enter your guess: 24\n",
            "Too low!\n",
            "Enter your guess: 40\n",
            "Too low!\n",
            "Enter your guess: 42\n",
            "Correct!\n",
            "It took you 4 attempts to win.\n"
          ]
        }
      ]
    }
  ]
}
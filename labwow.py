{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPIynV/UL0YTGe9MpP1Dzxp",
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
        "<a href=\"https://colab.research.google.com/github/rawnakwow/viva_selection/blob/main/labwow.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 67,
      "metadata": {
        "id": "upqVUlm5e0qk"
      },
      "outputs": [],
      "source": [
        "import random\n",
        "import math\n",
        "import matplotlib.pyplot as plt"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def argmaxall(gen):\n",
        "    \"\"\"gen is a generator of (element,value) pairs, where value is a real.\n",
        "    argmaxall returns a list of all of the elements with maximal value.\n",
        "    \"\"\"\n",
        "    maxv = -math.inf       # negative infinity\n",
        "    maxvals = []      # list of maximal elements\n",
        "    for (e,v) in gen:\n",
        "        if v > maxv:\n",
        "            maxvals, maxv = [e], v\n",
        "        elif v == maxv:\n",
        "            maxvals.append(e)\n",
        "    return maxvals"
      ],
      "metadata": {
        "id": "b7v4YEEpV3mV"
      },
      "execution_count": 68,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def argmaxe(gen):\n",
        "    \"\"\"gen is a generator of (element,value) pairs, where value is a real.\n",
        "    argmaxe returns an element with maximal value.\n",
        "    If there are multiple elements with the max value, one is returned at random.\n",
        "    \"\"\"\n",
        "    return random.choice(argmaxall(gen))"
      ],
      "metadata": {
        "id": "G8o284hWV9er"
      },
      "execution_count": 69,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def select_from_dist(item_prob_dist):\n",
        "    \"\"\" returns a value from a distribution.\n",
        "    item_prob_dist is an item:probability dictionary, where the probabilities sum to 1.\n",
        "    returns an item chosen in proportion to its probability\n",
        "    \"\"\"\n",
        "    ranreal = random.random()\n",
        "    for (it, prob) in item_prob_dist.items():\n",
        "        if ranreal < prob:\n",
        "            return it\n",
        "        else:\n",
        "            ranreal -= prob\n",
        "    raise RuntimeError(f\"{item_prob_dist} is not a probability distribution\")"
      ],
      "metadata": {
        "id": "MBELjgzpV9gE"
      },
      "execution_count": 70,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class Displayable(object):\n",
        "    \"\"\"Class that uses 'display'.\"\"\"\n",
        "    max_display_level = 1   # can be overridden in subclasses or instances\n",
        "\n",
        "    def display(self, level, *args, **nargs):\n",
        "        \"\"\"print the arguments if level is less than or equal to the current max_display_level.\"\"\"\n",
        "        if level <= self.max_display_level:\n",
        "            print(*args, **nargs)"
      ],
      "metadata": {
        "id": "pncQpMygWLDV"
      },
      "execution_count": 71,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class Plot_history(object):\n",
        "    \"\"\"Set up the plot for history of price and number in stock\"\"\"\n",
        "    def __init__(self, ag, env):\n",
        "        self.ag = ag\n",
        "        self.env = env\n",
        "        plt.ion()\n",
        "        plt.xlabel(\"Time\")\n",
        "        plt.ylabel(\"Value\")\n",
        "\n",
        "    def plot_env_hist(self):\n",
        "        \"\"\"plot history of price and instock\"\"\"\n",
        "        num = len(self.env.stock_history)\n",
        "        plt.plot(range(num), self.env.price_history, label=\"Price\")\n",
        "        plt.plot(range(num), self.env.stock_history, label=\"In stock\")\n",
        "        plt.legend()\n",
        "\n",
        "    def plot_agent_hist(self):\n",
        "        \"\"\"plot history of buying\"\"\"\n",
        "        num = len(self.ag.buy_history)\n",
        "        plt.bar(range(1, num+1), self.ag.buy_history, label=\"Bought\")\n",
        "        plt.legend()"
      ],
      "metadata": {
        "id": "oto_uliNYiF-"
      },
      "execution_count": 72,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class Agent(Displayable):\n",
        "    def initial_action(self, percept):\n",
        "        \"\"\"return the initial action.\"\"\"\n",
        "        return self.select_action(percept)  # same as select_action\n",
        "    def select_action(self, percept):\n",
        "        \"\"\"\n",
        "\n",
        "        Args:\n",
        "          percept:\n",
        "        \"\"\"\n",
        "        raise NotImplementedError(\"go\")  # abstract method"
      ],
      "metadata": {
        "id": "2yDgQc_SYr8U"
      },
      "execution_count": 73,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class Environment(Displayable):\n",
        "    def initial_percept(self):\n",
        "        \"\"\"returns the initial percept for the agent\"\"\"\n",
        "        raise NotImplementedError(\"initial_percept\")  # abstract method\n",
        "\n",
        "    def do(self, action):\n",
        "        \"\"\"does the action (buy) and returns the next percept\"\"\"\n",
        "        raise NotImplementedError(\"Environment.do\")  # abstract method"
      ],
      "metadata": {
        "id": "GX0Pnr_yY49V"
      },
      "execution_count": 74,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class Simulate(Displayable):\n",
        "    \"\"\"Simulate the interaction between the agent and the environment for n time steps.\"\"\"\n",
        "    def __init__(self, agent, environment):\n",
        "        self.agent = agent\n",
        "        self.env = environment\n",
        "        self.percept = self.env.initial_percept()\n",
        "        self.percept_history = [self.percept]\n",
        "        self.action_history = []\n",
        "\n",
        "    def go(self, n):\n",
        "        for i in range(n):\n",
        "            action = self.agent.select_action(self.percept)\n",
        "            print(f\"i={i} action={action}\")\n",
        "            self.percept = self.env.do(action, i)\n",
        "            print(f\"      percept={self.percept}\")"
      ],
      "metadata": {
        "id": "j-DwhYu9ZBFN"
      },
      "execution_count": 75,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class SmartphoneEnv(Environment):\n",
        "    price_delta = [0, 0, 0, 21, 0, 20, 0, -64, 0, 0, 23, 0, 0, 0, -35,\n",
        "                  0, 76, 0, -41, 0, 0, 0, 21, 0, 5, 0, 5, 0, 0, 0, 5, 0, -15, 0, 5,\n",
        "                  0, 5, 0, -115, 0, 115, 0, 5, 0, -15, 0, 5, 0, 5, 0, 0, 0, 5, 0,\n",
        "                  -59, 0, 44, 0, 5, 0, 5, 0, 0, 0, 5, 0, -65, 50, 0, 5, 0, 5, 0, 0,\n",
        "                  0, 5, 0]\n",
        "    sd = 5  # noise standard deviation\n",
        "\n",
        "    def __init__(self):\n",
        "        self.time = 0\n",
        "        self.stock = 20\n",
        "        self.stock_history = []  # memory of the stock history\n",
        "        self.price_history = []  # memory of the price history\n",
        "\n",
        "    def initial_percept(self):\n",
        "        \"\"\"return initial percept\"\"\"\n",
        "        self.stock_history.append(self.stock)\n",
        "        self.price = round(234 + self.sd * random.gauss(0, 1))\n",
        "        self.price_history.append(self.price)\n",
        "        return {'price': self.price, 'instock': self.stock}\n",
        "\n",
        "    def do(self, action, time_unit):\n",
        "        \"\"\"does action (buy) and returns percept consisting of price and instock\"\"\"\n",
        "        used = select_from_dist({6: 0.1, 5: 0.1, 4: 0.1, 3: 0.3, 2: 0.2, 1: 0.2})\n",
        "        bought = action['buy']\n",
        "        self.stock = self.stock + bought - used\n",
        "        self.stock_history.append(self.stock)\n",
        "        self.time += 1\n",
        "        self.price = round(self.price + self.price_delta[self.time % len(self.price_delta)]\n",
        "                           + self.sd * random.gauss(0, 1))  # price fluctuates\n",
        "        self.price_history.append(self.price)\n",
        "        return {'price': self.price, 'instock': self.stock}"
      ],
      "metadata": {
        "id": "HxbfarCNZDzd"
      },
      "execution_count": 76,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class SmartphoneAgent(Agent):\n",
        "    def __init__(self):\n",
        "        self.spent = 0\n",
        "        percept = env.initial_percept()\n",
        "        self.ave = self.last_price = percept['price']\n",
        "        self.instock = percept['instock']\n",
        "        self.buy_history = []\n",
        "\n",
        "    def select_action(self, percept):\n",
        "        \"\"\"return next action to carry out\"\"\"\n",
        "        self.last_price = percept['price']\n",
        "        self.ave = self.ave + (self.last_price - self.ave) * 0.05  # smooth average\n",
        "        self.instock = percept['instock']\n",
        "        if self.last_price < 0.8 * self.ave and self.instock < 60:\n",
        "            tobuy = 48  # order 48 units if price is 20% below average and stock is below 60\n",
        "        elif self.instock < 12:\n",
        "            tobuy = 12  # order 12 units if stock is below 12\n",
        "        else:\n",
        "            tobuy = 0  # no order if none of the conditions are met\n",
        "        self.spent += tobuy * self.last_price\n",
        "        self.buy_history.append(tobuy)\n",
        "        return {'buy': tobuy}\n"
      ],
      "metadata": {
        "id": "K8yEKNMrZIm8"
      },
      "execution_count": 77,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Initialize environment and agent\n",
        "env = SmartphoneEnv()\n",
        "ag = SmartphoneAgent()\n",
        "\n",
        "# Simulate the environment and agent interaction\n",
        "sim = Simulate(ag, env)\n",
        "sim.go(10)  # Simulate for 10 time steps\n",
        "\n",
        "# Display the results\n",
        "ag.spent / env.time  # Calculate average spent per time step\n",
        "\n"
      ],
      "metadata": {
        "id": "nhK_43TXZIoa",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f9c8f065-51d4-411a-98cf-eb2fa76ee52b"
      },
      "execution_count": 78,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "i=0 action={'buy': 0}\n",
            "      percept={'price': 231, 'instock': 16}\n",
            "i=1 action={'buy': 0}\n",
            "      percept={'price': 229, 'instock': 13}\n",
            "i=2 action={'buy': 0}\n",
            "      percept={'price': 255, 'instock': 12}\n",
            "i=3 action={'buy': 0}\n",
            "      percept={'price': 253, 'instock': 8}\n",
            "i=4 action={'buy': 12}\n",
            "      percept={'price': 271, 'instock': 18}\n",
            "i=5 action={'buy': 0}\n",
            "      percept={'price': 278, 'instock': 15}\n",
            "i=6 action={'buy': 0}\n",
            "      percept={'price': 218, 'instock': 13}\n",
            "i=7 action={'buy': 0}\n",
            "      percept={'price': 220, 'instock': 7}\n",
            "i=8 action={'buy': 12}\n",
            "      percept={'price': 216, 'instock': 13}\n",
            "i=9 action={'buy': 0}\n",
            "      percept={'price': 235, 'instock': 11}\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "567.6"
            ]
          },
          "metadata": {},
          "execution_count": 78
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Plot the results\n",
        "plot_history = Plot_history(ag, env)\n",
        "plot_history.plot_env_hist()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 449
        },
        "id": "aS3I86dBnGXR",
        "outputId": "21100838-ccca-4dcb-ebcd-0cb2b9d146c6"
      },
      "execution_count": 79,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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F2PWrFkoKCjA4MGDsX37dri6ulpfs379esTFxWHkyJGQy+WYOHEiVqxY0eyfhYiIiByTw8yzIybOs0NEROR8nH6eHSIiIqKmwLBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLGsENERESSxrBDREREksawQ0RERJLm0GHn1VdfhUwms7l17tzZur6srAyxsbFo2bIlPD09MXHiROTm5opYMRERETkahw47ANC1a1dcunTJetu3b5913TPPPIPNmzfjf//7H5KSkpCdnY0HHnhAxGqJiIjI0SjFLuB2lEoldDrdTc/r9Xr85z//wYYNG3DvvfcCANauXYsuXbpg//79GDBgQHOXSkRERA7I4Vt2Tp8+jcDAQLRr1w5TpkzB+fPnAQApKSkwGo2Iioqybtu5c2eEhIQgOTn5lvssLy+HwWCwuREREZE0OXTY6d+/P9atW4ft27fjww8/RGZmJoYMGYLCwkLk5ORApVLB29vb5jX+/v7Iycm55X7j4+Oh1Wqtt+DgYDt+CiIiIhKTQ3djjR492vq4e/fu6N+/P9q0aYOvvvoKbm5ujd7vwoULMX/+fOuywWBg4CEiIpIoh27ZuZG3tzc6duyIjIwM6HQ6VFRUoKCgwGab3NzcWsf41KRWq6HRaGxuREREJE1OFXaKiopw5swZBAQEoHfv3nBxcUFiYqJ1fXp6Os6fP4/IyEgRqyQiIiJH4tDdWM899xzGjRuHNm3aIDs7G0uWLIFCocDDDz8MrVaLGTNmYP78+fDx8YFGo8GcOXMQGRnJM7GIiIjIyqHD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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "soB8ZKjcnGZB"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "----------- WELCOME TO TIC TAC TOE ------------\n",
      "\n",
      "\n",
      "    │    │     \n",
      "────┼────┼────\n",
      "    │    │     \n",
      "────┼────┼────\n",
      "    │    │     \n",
      "\n",
      "Player 1 : Shubham\n",
      "Player 2 : Ankit\n",
      "\n",
      "-------- Instructions ---------\n",
      "-> Shubham you will using X\n",
      "-> Ankit you will using 0\n",
      "-> Turn starts from Shubham\n",
      "-> Potisions are like :-\n",
      "  1 │  2 │ 3  \n",
      "────┼────┼────\n",
      "  4 │ 5  │ 6  \n",
      "────┼────┼────\n",
      "  7 │ 8  │ 9  \n",
      "-> press S to start the game\n",
      "s\n",
      "\n",
      "this is ur turn Shubham\n",
      "Please Enter postion : 1\n",
      " x  │    │     \n",
      "────┼────┼────\n",
      "    │    │     \n",
      "────┼────┼────\n",
      "    │    │     \n",
      "\n",
      "this is ur turn Ankit\n",
      "Please Enter postion : 3\n",
      " x  │    │  0  \n",
      "────┼────┼────\n",
      "    │    │     \n",
      "────┼────┼────\n",
      "    │    │     \n",
      "\n",
      "this is ur turn Shubham\n",
      "Please Enter postion : 9\n",
      " x  │    │  0  \n",
      "────┼────┼────\n",
      "    │    │     \n",
      "────┼────┼────\n",
      "    │    │  x  \n",
      "\n",
      "this is ur turn Ankit\n",
      "Please Enter postion : 5\n",
      " x  │    │  0  \n",
      "────┼────┼────\n",
      "    │ 0  │     \n",
      "────┼────┼────\n",
      "    │    │  x  \n",
      "\n",
      "this is ur turn Shubham\n",
      "Please Enter postion : 7\n",
      " x  │    │  0  \n",
      "────┼────┼────\n",
      "    │ 0  │     \n",
      "────┼────┼────\n",
      " x  │    │  x  \n",
      "\n",
      "this is ur turn Ankit\n",
      "Please Enter postion : 4\n",
      " x  │    │  0  \n",
      "────┼────┼────\n",
      " 0  │ 0  │     \n",
      "────┼────┼────\n",
      " x  │    │  x  \n",
      "\n",
      "this is ur turn Shubham\n",
      "Please Enter postion : 8\n",
      " x  │    │  0  \n",
      "────┼────┼────\n",
      " 0  │ 0  │     \n",
      "────┼────┼────\n",
      " x  │ x  │  x  \n",
      "\n",
      "\n",
      "Hurray !!, Shubham you win ♥♥\n"
     ]
    }
   ],
   "source": [
    "# for display the tic tac toe board\n",
    "def print_board(a):\n",
    "    print(\"\",a[1],\" │\",a[2],\" │ \",a[3],\" \")\n",
    "    print(\"────┼────┼────\")\n",
    "    print(\"\",a[4],\" │\",a[5],\" │ \",a[6],\" \")\n",
    "    print(\"────┼────┼────\")\n",
    "    print(\"\",a[7],\" │\",a[8],\" │ \",a[9],\" \")\n",
    "    \n",
    "# for display the instruction of game\n",
    "def print_instructions():\n",
    "    print(\"\\n----------- WELCOME TO TIC TAC TOE ------------\\n\\n\")\n",
    "    print_board(pos)\n",
    "    print()\n",
    "    \n",
    "    players[0] = input(\"Player 1 : \")\n",
    "    players[1] = input(\"Player 2 : \")\n",
    "    \n",
    "    print(\"\\n-------- Instructions ---------\")\n",
    "    print(\"->\",players[0],\"you will using X\")\n",
    "    print(\"->\",players[1],\"you will using 0\")\n",
    "    print(\"-> Turn starts from\",players[0])\n",
    "    print(\"-> Potisions are like :-\")\n",
    "    print(\"  1 │  2 │ 3  \")\n",
    "    print(\"────┼────┼────\")\n",
    "    print(\"  4 │ 5  │ 6  \")\n",
    "    print(\"────┼────┼────\")\n",
    "    print(\"  7 │ 8  │ 9  \")\n",
    "    print(\"-> press S to start the game\")\n",
    "    flag = input()    \n",
    "    return flag\n",
    "\n",
    "# for start the game\n",
    "def startgame():\n",
    "    turn = 0\n",
    "    for i in range(9):\n",
    "        if turn % 2 == 0:\n",
    "            print(\"\\nthis is ur turn\",players[0])\n",
    "            p = int(input(\"Please Enter postion : \"))\n",
    "            v = 'x'\n",
    "            pos[p] = v\n",
    "            print_board(pos)\n",
    "            winner = checkwin(v)\n",
    "            if winner is \"nobody\":\n",
    "                turn = 1\n",
    "                continue\n",
    "            else:\n",
    "                print(\"\\n\\nHurray !!,\",players[0],\"you win ♥♥\")\n",
    "                break\n",
    "        else:\n",
    "            print(\"\\nthis is ur turn\",players[1])\n",
    "            p = int(input(\"Please Enter postion : \"))\n",
    "            v = '0'\n",
    "            pos[p] = v\n",
    "            print_board(pos)\n",
    "            winner = checkwin(v)\n",
    "            if winner is \"nobody\":\n",
    "                turn = 0\n",
    "                continue\n",
    "            else:\n",
    "                print(\"\\n\\nHurray !!,\",players[1],\"you win ♥♥\")    \n",
    "                break\n",
    "    else:\n",
    "        print(\"\\n\\nGame is Tie\")\n",
    "        \n",
    "# check for winner \n",
    "def checkwin(v):\n",
    "    for i in winning_conditions:\n",
    "        if (pos[i[0]], pos[i[1]], pos[i[2]]) == (v,v,v):\n",
    "            winner = players[0]\n",
    "            break\n",
    "        elif (pos[i[0]], pos[i[1]], pos[i[2]]) == (v,v,v):\n",
    "            winner = players[1]\n",
    "            break\n",
    "    else:\n",
    "        winner = \"nobody\"\n",
    "    return winner\n",
    "\n",
    "# main code \n",
    "pos = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']\n",
    "players = ['','']\n",
    "winning_conditions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]\n",
    "flag = print_instructions()\n",
    "if flag == 's' or flag == 'S':\n",
    "    startgame()\n",
    "else:\n",
    "    print(\"Invalid Entry\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
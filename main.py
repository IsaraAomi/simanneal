import os
import random
import time

import matplotlib.pyplot as plt

from simanneal import Annealer


# 計算関数の例
def calculate(x, y, z):
    if x == "a" and y == "a" and z == "a":
        return 1
    elif x == "b" and y == "b" and z == "b":
        return 2
    elif x == "c" and y == "c" and z == "c":
        return 3
    elif x == "d" and y == "d" and z == "d":
        return 4
    else:
        return 5


class MyProblem(Annealer):
    """simanneal の Annealer クラスを継承して問題を定義"""

    def __init__(self, state, states):
        super(MyProblem, self).__init__(state)
        self.states = states
        self.energy_history = []
        self.record_history = False  # ヒストリーを記録するかどうかのフラグ

    def move(self):
        """状態をランダムに変更する"""
        new_x = random.choice(self.states)
        new_y = random.choice(self.states)
        new_z = random.choice(self.states)
        self.state = (new_x, new_y, new_z)

    def energy(self):
        """目的関数 z の値を計算し、エネルギーとして返す"""
        x, y, z = self.state
        e = calculate(x, y, z)
        if self.record_history:  # フラグがTrueのときだけ記録
            self.energy_history.append(e)
        return e


def plot_energy_history(energy_history, filename="energy_vs_iteration.png"):
    """エネルギーの履歴をプロットし、画像として保存する関数"""
    os.environ["DISPLAY"] = ""
    plt.plot(energy_history)
    plt.xlabel("Iteration")
    plt.ylabel("Energy")
    plt.title("Energy vs Iteration")

    # グラフを画像として保存
    plt.savefig(filename)
    print(f"グラフは '{filename}' として保存されました。")


def main():
    """最適化プロセスのメイン関数"""
    random.seed(1)

    # 状態の定義
    states = ["a", "b", "c", "d"]

    # 初期状態を設定
    initial_state = ("c", "c", "d")

    # 問題を定義
    problem = MyProblem(initial_state, states)

    # 自動スケジュールを取得（この時はenergy_historyに追加しない）
    problem.set_schedule(problem.auto(minutes=0.2))

    # 最大イテレーション数を設定
    problem.steps = 10

    # 探索の開始時にヒストリーの記録をオンにする
    problem.record_history = True

    # 最適化を実行
    best_state, best_energy = problem.anneal()

    # 結果を表示
    print()
    print(len(problem.energy_history))
    print(problem.energy_history)
    print("最適解:", best_state)
    print("エネルギー:", best_energy)

    # エネルギーの履歴をプロット
    plot_energy_history(problem.energy_history)


if __name__ == "__main__":
    main()

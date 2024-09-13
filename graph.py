import os

os.environ["DISPLAY"] = ""

import matplotlib.pyplot as plt
import numpy as np

# データの準備
x = np.linspace(0, 10, 100)
y = np.sin(x)

# グラフの描画
plt.plot(x, y, label="sin(x)")
plt.title("Sample Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()

# グラフをPNGファイルとして保存
plt.savefig("sine_wave.png")

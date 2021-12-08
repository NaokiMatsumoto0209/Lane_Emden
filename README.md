# Lane_Emden
Lane_Emden方程式の計算コード

## 計算方法
gccの使い方は

`gcc -o lane_emden lane_emden.c`

とする。

実行の際は、main関数に引数を2つとっているので、

`./lane_emden lnem_1.dat 1.0`

のように、

`実行ファイル名 書き出しファイル名 パラメータ`

とする。

なお、ここでいうところのパラメータとは

$$

  \frac{1}{\xi^{2}}\frac{\mathrm{d}}{\mathrm{d}\xi}\left( \xi^{2}\frac{\mathrm{d}\theta}{\mathrm{d}\xi} \right) = -\theta^{N}

$$

の$N$である。

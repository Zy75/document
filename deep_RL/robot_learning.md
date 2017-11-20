# 知能ロボットについての調査

2017/11

## どこまで来たか

論文１では、強化学習と深層学習を組み合わせた深層強化学習という手法によって、人工知能にAtariのゲームをうまくプレイさせることに成功した。

深層強化学習はロボット制御への応用も研究されていて、シミュレータ環境ではレベルの高い知能を実現している。

ビデオ：https://www.youtube.com/watch?v=gn4nRCC9TwQ

行動空間を連続にしたり[4]、並列計算でCPUでも学習できる方法[3],人間による手本を使う方法[5]、疎な報酬でも好奇心によって行動する方法[6]などが提案されている。

以下のプログラムを実行してみるとよくわかる。

https://github.com/joschu/modular_rl

https://gist.github.com/joschu/6de0710846dff7230543016fc7639f82

## 実際どうなのか？

humanoidは、人型２足歩行ロボットの環境だ。一見難しそうだが、関節の角度はある範囲を超えることはなく、数学的な構造はシンプルで、学習させる関数もシンプルかもしれない。

## 問題点 

ひとつ目の問題は、深層強化学習のロボットへの応用はほとんどがシミュレーション環境でのものだということだ。

また、ロボットに家事など複雑な作業をさせるには、シミュレータであっても学習に時間がかかると思われる。

### 実機に持ち込めない理由

学習時間がかかる。シミュレータでは時間を早送りしてデータをサンプルできるが、実機ではリアルな時間に従わなければならない。

また,シミュレータで使ったロボットのハードと実機のハードに違いがある場合、その違いを吸収する必要がある。転移学習といって、論文２など、いくつも解決策が提案されているが、実際試している例は知らない。

また、学習中にロボットがダメージを受けるという問題もある。　例えば、二足歩行ロボットでは、何回も転んだりしながら試行錯誤で学習しなければならない。
この例では、上からひもで吊るす方法があるが、完全ではない気がする。



## まとめ

深層強化学習の実機ロボット制御への応用はまだまだ。

## 文献

1. Human-level control through deep reinforcement learning
2. Sim-to-Real Robot Learning from Pixels with Progressive Nets
3. Asynchronous Methods for Deep Reinforcement Learning
4. Continuous control with deep reinforcement learning
5. Leveraging Demonstrations for Deep Reinforcement Learning on Robotics Problems with Sparse Rewards
6. Curiosity-driven Exploration by Self-supervised Prediction
7. Trust Region Policy Optimization
8. Proximal Policy Optimization

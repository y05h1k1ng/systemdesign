# systemdesign

## 概要
災害収納boxを作ろうぜみたいなグループワークが発端

作ったもの
- ラズパイ周りの制御（音声、LED、ボタン）
- 災害情報のなんちゃってapi
- 収納物管理webアプリ

## 構成
```
src
|-api
| |-main.py
| |-main.go
| |-api_test.py
|
|-rasp
| |-main.py
|
|-servise
  |-main.py
  |-templates
  | |-index.html
  |
  |-database
    |-datas.db
```

### api
#### main.py
- flask製
- 雨、津波、地震、火山の4つの警報情報
-- `/tunami`
-- `/rain`
-- `/earthquake`
-- `/volcano`

jsonで返す。
jsonの中身は警報の種類と強さ的な意味のlevel(ランダム)になってる。

#### main.go
もともとgoで書きたかったから書いたけど、ラズパイで実行させるのが面倒でpythonに乗り換えた名残

`go-json-rest`という謎パッケージを使ったが、今思うと`Echo`を使えばよかった

#### api_test.py
apiのテスト用スクリプト

### rasp
#### main.py
- ラズパイ周りの制御
- pygameで音声出力、GUI（と言っても画面出力でユーザの操作とかは一切ない）
- apiの情報を拾ってlevel(0~5)が3以上だったら、ライトが光って音声が流れる

### servise
- flask製
- 設計方針は画面の遷移がなくて、1ページで完結させたかった（が、編集をさせるのが辛いというかできていない。modalとか使えたらかっこいいなと思ったけど手が動かない）
- sqlite3で管理
- 追加、削除は実装
- 編集は未実装

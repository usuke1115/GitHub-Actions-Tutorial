# GitHub Actions YAMLファイルの書き方

まず, `.github/workflows`ディレクトリを<span style="color: red;">必ず</span>作る. そのディレクトリの配下に`yml`ファイルを作成する. ファイル名はなんでもよい.

`yml`ファイルにはあるトリガーに対し, 行うことを記述する. これを **ワークフロー** と呼ぶ. 

1つのファイル = 1ワークフローである.

```yml: Sample.yml
name: GitHub Actions Demo

on: [push]

jobs:
  echo_hello_world:
    runs-on: ubuntu-latest # ここは大体これで固定
    steps:
      - run: echo "hello world!!"
```

## トリガー設定

`on`の部分にはトリガーを記述する.
これはどのタイミングで実行するかを決定する.

例えば, 毎日15:00にスクレイピングする. 
```yml: crowl.yml
on:
  - cron: "* 15 * * *"
```
<br/>
 
`main`ブランチにプッシュされたときに, フォーマッターを実行する.

```
on:
  push:
    branches:
      - main
```
<br/>

複数のイベントを設定したいなら, 配列を使えばいい.
```yml: some_event.yml
on: [push, fork]
```


PRが来たときに...などがある.
```yml: pr.yml
on:
  pull_request: 
```

## ジョブ設定
各ジョブにはジョブIDというものが必要になる.
```yml: sample.yml
name: GitHub Actions Demo

on: [push]

jobs:
  echo_hello_world:
    runs-on: ubuntu-latest # ここは大体これで固定
    steps:
      - run: echo "hello world!!"
```
上の例だと`jobs:`の1つ下の行の`echo_hello_world`がジョブIDである.

`runs-on`フィールドは必須であり, 大抵はGitHubが提供するUbuntu Linuxの最新環境を指定することになる.

## 用参照

下の資料を読んだらやりたいことは大体できると思う.

[GitHub Actions Guide](https://zenn.dev/farstep/books/learn-github-actions)

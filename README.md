![uv](https://img.shields.io/badge/uv-0.8.13-blue)
![python](https://img.shields.io/badge/python-3.13.7-blue)
![quarto](https://img.shields.io/badge/quarto-1.7.32-blue)

## 開発環境セットアップ

このリポジトリでは **バッジの自動更新** を行うために以下が必要です:

- [jq](https://stedolan.github.io/jq/) : JSON の整形・更新に利用
- [pre-commit](https://pre-commit.com/) : Git コミット前にスクリプトを自動実行する仕組み

**&#9654;&nbsp; pre-commit初期設定**

リポジトリを clone したあと，以下を一度実行してください:

```bash
pre-commit install
```

## UV Dependency groups

| Group Name | Description |
|------------|-------------|
| `base`     | Base dependencies for all environments |
| `dev`      | Development dependencies |
| `book`     | Quarto Book dependencies |

それぞれのgroup別のinstall commandは以下の通りです

```bash
# base
uv add numpy

# dev
uv add --group dev pytest

# book
uv add --group book ipykernel nbformat plotly pandas matplotlib
```

## Lint check

**&#9654;&nbsp; uvx ruff**

- `uvx ruff`: プロジェクト内の Python コードに対して lint チェックを実行するコマンド

```bash
# check
uvx ruff check src/

# format
uvx ruff format src/
```

**&#9654;&nbsp; `ruff.toml`の設定**

- `ruff.toml`: ruff の設定ファイル
- `ruff`はrepositoty内に存在する`pyproject.toml`, `ruff.toml`, `.ruff.toml`のいずれかの設定をベースに運用される

## Localでquarto bookを立ち上げる方法

**&#9654;&nbsp; 依存関係の同期**

```bash
# pyproject.toml / uv.lock に基づいて依存パッケージを同期
uv sync
```

- `uv sync` は プロジェクトの依存関係を仮想環境に反映させるコマンド
- 依存パッケージを更新した場合，Quarto Book を正しく起動するために必要

**&#9654;&nbsp; 仮想環境内で Quarto を起動**

```bash
# 仮想環境内で Quarto プレビューを開始
uv run quarto preview
```

- `uv run` は 仮想環境内でコマンドを実行する uv の基本コマンド
- 上記を実行すると，Quarto Book がローカルサーバーで立ち上がる

## GitHub Repository Setup

現在のディレクトリの Git リポジトリ（`git init`済み）を GitHub Repositoryに作成し，first-commitをpushする手順は以下

**&#9654;&nbsp; GitHub Repository作成 Syntax**

```bash
gh repo create <repositoryname> --source=. --remote=<upstream-name> --public --push
```

**&#9654;&nbsp; 実行例**

```zsh
% gh repo create regression-monkey-nonparametric \
  --source=. \
  --remote=origin \
  --public \
  --push
✓ Created repository RyoNakagami/regression-monkey-nonparametric on github.com
  https://github.com/RyoNakagami/regression-monkey-nonparametric
✓ Added remote https://github.com/RyoNakagami/regression-monkey-nonparametric.git
Enumerating objects: 70, done.
Counting objects: 100% (70/70), done.
Delta compression using up to 32 threads
Compressing objects: 100% (61/61), done.
Writing objects: 100% (70/70), 166.02 KiB | 27.67 MiB/s, done.
Total 70 (delta 8), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (8/8), done.
To https://github.com/RyoNakagami/regression-monkey-nonparametric.git
 * [new branch]      HEAD -> main
branch 'main' set up to track 'origin/main'.
✓ Pushed commits to https://github.com/RyoNakagami/regression-monkey-nonparametric.git
```

remoteを確認すると

```zsh
% git remote -v
origin  https://github.com/RyoNakagami/regression-monkey-nonparametric.git (fetch)
origin  https://github.com/RyoNakagami/regression-monkey-nonparametric.git (push)
```

## Quarto Publish

運用としては `main` ブランチの内容をlocalでレンダリングし，それをGitHub Pagesにデプロイする流れを想定しています．
ただし，`gh-pages` ブランチは `.pre-commit-config.yaml` は存在しないため，pre-commitのhookが働かず，以下のようなエラーが発生します:

```bash
branch 'gh-pages' set up to track 'origin/gh-pages'.
HEAD is now at 4d5b51a Built site for gh-pages
No .pre-commit-config.yaml file was found
- To temporarily silence this, run `PRE_COMMIT_ALLOW_NO_CONFIG=1 git ...`
- To permanently silence this, install pre-commit with the --allow-missing-config option
- To uninstall pre-commit run `pre-commit uninstall`
fatal: '.quarto/quarto-publish-worktree-21440733a1c14bff' contains modified or untracked files, use --force to delete it
```

それに対処するため，以下のような実行を想定しています

```bash
PRE_COMMIT_ALLOW_NO_CONFIG=1 quarto publish gh-pages
```



## References

- [Quarto Publishing with GitHub Pages](https://quarto.org/docs/publishing/github-pages.html)

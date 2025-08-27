![UV](https://img.shields.io/endpoint?url=https://ryonakagami.github.io/regmonkey-datascience-blog/badges/posts.json)

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

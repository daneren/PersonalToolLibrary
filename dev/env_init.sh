
pip3 config set global.index-url https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
pip3 install uv

mkdir -vp ~/.config/uv && echo -e '[[index]]\nurl = "https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple"\ndefault = true' > ~/.config/uv/uv.toml

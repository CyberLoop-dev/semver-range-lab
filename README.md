<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=145&section=header&text=Semver%20Range%20Lab&fontColor=ffffff&fontSize=36" alt="Animated header"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=900&center=true&vCenter=true&width=620&lines=Semver%20Range%20Lab;Test%20version%20constraints" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/semver-range-lab?label=MIT)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/semver-range-lab)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/semver-range-lab?style=social)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/semver-range-lab)

<img src="./assets/mark.svg" width="145" alt="Custom SVG illustration"/>

**Explore whether stable MAJOR.MINOR.PATCH versions satisfy common semantic-version ranges.**

</div>

## ✨ Overview

A small local evaluator for the most common stable SemVer range forms. Rules are explicit and covered by tests.

## 🚀 Features

- 🔎 Supports exact, comparison, caret, tilde, wildcard, and OR ranges.
- 🧪 Evaluates many versions against one range.
- 📘 Documents zero-major caret behavior.
- 🚫 Rejects prerelease versions and unsupported syntax.

## 🧪 Demo

```text
$ python main.py '^1.2.0' 1.5.0 2.0.0
1.5.0: MATCH
2.0.0: NO MATCH
```

## ⚡ Quick Start

```bash
git clone https://github.com/CyberLoop-dev/semver-range-lab.git
cd semver-range-lab
python main.py '>=1.2.0 <2.0.0' 1.4.0 2.0.0
```

## 🧰 Tech Stack

Python 3.10+ · Standard library only.

## 🗂️ Folder Structure

```text
semver-range-lab/
├── main.py
├── tests/test_main.py
├── requirements.txt
├── .github/workflows/tests.yml
└── assets/mark.svg
```

## 🗺️ Roadmap

- [x] Comparator, caret, tilde, wildcard, and OR support
- [x] Unit tests and CI
- [ ] Prerelease and build metadata support
- [ ] Explain each range boundary

## 🤝 Contributing

Open an issue for a reproducible SemVer case. Add a test for each new range form.

## 📄 License

MIT — see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated footer"/></div>

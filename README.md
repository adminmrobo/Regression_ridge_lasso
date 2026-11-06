**[한국어](#ko) · [English](#en) · [中文](#zh) · [日本語](#ja) · [Oʻzbekcha](#uz) · [Русский](#ru) · [Tiếng Việt](#vi)**

<a id="ko"></a>

# 릿지와 라쏘 — 농어 무게로 배우는 과적합 막기

공개 주소: https://adminmrobo.github.io/Regression_ridge_lasso/ · 목차: [index.html](index.html) · 해설 바로 열기: [RG_ridge_lasso.html](RG_ridge_lasso.html)

![표지](og_rg.jpg)

농어 56마리의 길이·높이·폭으로 무게를 예측하며, 특성을 늘릴 때 생기는 과적합과 이를 막는 릿지·라쏘, 그리고 alpha를 고르는 교차 검증을 브라우저에서 직접 만져 보는 인터랙티브 교육 페이지다. 박사 · 하루(조수) · 초파리 연구원 · 주판봇이 말풍선으로 진행하고, 모든 핵심 숫자는 페이지 안 Colab 코드 2개를 실제로 실행한 결과다.

**바로 보기:** https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.html

**저자:** 글 · 안상선 ((주)M-Robo 대표)

## 언어

- **고르는 방법:** 최상단 메뉴의 🌐 언어 선택 상자, 또는 화면 오른쪽 아래 🌐 배너를 누른다. 고른 언어는 브라우저에 기억된다.
- **자동 전환:** 한국어 페이지로 들어오면, 기억된 언어가 있으면 그 언어로, 없으면 브라우저 언어가 지원 언어일 때 그 언어로 연다. 지원하지 않는 언어는 한국어 그대로다. 번역판 주소로 들어온 사람은 자동 전환하지 않는다.
- **주소로 고르기:** 주소 뒤에 `?lang=en`처럼 붙이면 그 언어로 열고 기억한다. `#섹션`은 그대로 유지된다.
- **언어 예외:** 없음. 이 페이지에는 한국어 입력이 있어야만 작동하는 실습이 없다.

| 언어 | 파일 이름 | 바로 보기 |
|---|---|---|
| 한국어 | RG_ridge_lasso.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.html |
| English | RG_ridge_lasso.en.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.en.html |
| 中文 | RG_ridge_lasso.zh.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.zh.html |
| 日本語 | RG_ridge_lasso.ja.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ja.html |
| Oʻzbekcha | RG_ridge_lasso.uz.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.uz.html |
| Русский | RG_ridge_lasso.ru.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ru.html |
| Tiếng Việt | RG_ridge_lasso.vi.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.vi.html |

## 구성

| 편 | 제목 | 다루는 내용 | 난이도 |
|---|---|---|---|
| RG | 릿지와 라쏘 — 농어 무게로 배우는 과적합 막기 | 기본 선형 회귀, 다항 특성과 과적합, 릿지(L2), 라쏘(L1), 교차 검증으로 alpha 고르기 | ★★★ |

## 농어 데이터가 걸어온 길

| 들어가는 것 | 나오는 것 | 다음 편으로 넘기는 질문 |
|---|---|---|
| 농어 56마리의 길이·높이·폭(cm)과 무게(g) | 특성 55개에서 계수를 묶은 릿지·라쏘 모델, 교차 검증으로 고른 alpha, 라쏘가 남긴 특성 8개 | 특성끼리의 관계를 사람이 만들어 주지 않아도 모델이 스스로 찾게 할 수 있을까? 릿지와 라쏘를 섞으면(엘라스틱넷) 닮은 특성 문제가 줄어들까? |

## 핵심 숫자

| 숫자 | 뜻 | 출처 |
|---|---|---|
| 훈련 0.9997 / 테스트 −4.3927 | 특성 55개 기본 회귀의 R². 훈련 데이터를 외운 과적합 | 코드 1 |
| 417,225 | 그 모델의 가장 큰 계수 크기 | 코드 1 |
| 0.9725 | 교차 검증이 고른 릿지 α=10의 테스트 R² | 코드 2 |
| 8 / 55 · 0.9802 | 라쏘 α=1이 남긴 특성 수와 테스트 R² | 코드 2 |

## 페이지에 들어 있는 것

| 순서 | 섹션 | 주요 실습 |
|---|---|---|
| 1 | 지령 | 연구실 식구 대화, 큰 그림 흐름도 |
| 2 | 기본 회귀 | 길이–무게 산점도와 예측선, 농어 저울(테스트 14마리) |
| 3 | 특성 늘리기 | degree 슬라이더 1~5, 훈련·테스트 R² 막대, 예측선이 출렁이는 모습 |
| 4 | 릿지 | alpha 슬라이더, 계수 55개 막대(로그 눈금), 규제 전 계수와 비교 |
| 5 | 라쏘 | alpha 슬라이더, 0이 되어 빠지는 계수, 남은 특성 수 |
| 6 | alpha 고르기 | 교차 검증 평균과 테스트 점수 비교, 5조각 돌려 채점하기 |
| — | 대결 | 특성 55개 그대로 vs 릿지, 봉인한 테스트로 판정 |
| 7 | 한계와 다음 미션 | 되는 것·안 되는 것, 실습별 요약표 |
| A~F | Colab 코드 · AI 응용 프롬프트 · 용어 정리 · 비유 모음 · 저자 소개와 레퍼런스 · 교육자를 위한 TIP | |
| — | 지식 색인 · 온톨로지·서지 꾸러미 | 개념 검색, 관계 그래프, JSON-LD·Turtle·CSV·BibTeX·RIS 꾸러미(ZIP) |

## Colab 코드

| 코드 1 | 코드 2 | 라이브러리 | 실행 시간 |
|---|---|---|---|
| 특성을 늘리면 테스트 점수가 무너진다 (섹션 2·3) | 계수를 묶고 alpha를 교차 검증으로 고르기 (섹션 4~6, 대결) | numpy, scikit-learn, matplotlib (Colab 기본 설치) | 각각 CPU 약 2~3초 |

각 코드 패널에서 복사 · .py 내려받기 · 노트북(.ipynb) 내려받기를 할 수 있다. 실행 확인: 2026-10-29, numpy 2.5 · scikit-learn 1.9 · matplotlib 3.11.

## 파일

```
RG_ridge_lasso.html                    한국어 원본
RG_ridge_lasso.en.html  .zh.html  .ja.html
RG_ridge_lasso.uz.html  .ru.html  .vi.html
README.md
index.html  index.en.html  index.zh.html  index.ja.html
index.uz.html  index.ru.html  index.vi.html
thumb_rg.webp  og_rg.jpg  hero_rg.webp  (cover_index.webp)
cover_manifest.json
code/rg_code1_overfitting.py  code/rg_code2_ridge_lasso.py
docs/COVER_00_index.md  docs/COVER_RG_ridge_lasso.md
docs/IMG_RG_ridge_lasso.md  docs/KG_00_registry_additions.json
```

| 파일 | 크기 |
|---|---|
| RG_ridge_lasso.html | 576 KB |
| RG_ridge_lasso.en.html | 576 KB |
| RG_ridge_lasso.zh.html | 569 KB |
| RG_ridge_lasso.ja.html | 583 KB |
| RG_ridge_lasso.uz.html | 585 KB |
| RG_ridge_lasso.ru.html | 623 KB |
| RG_ridge_lasso.vi.html | 590 KB |
| index.html | 15 KB |
| index.en.html | 15 KB |
| index.zh.html | 15 KB |
| index.ja.html | 16 KB |
| index.uz.html | 16 KB |
| index.ru.html | 17 KB |
| index.vi.html | 16 KB |

모든 HTML은 그림·데이터·스크립트를 한 파일에 담았다. 빌드 과정 없이 브라우저로 열기만 하면 된다. 외부에서 불러오는 것은 Google Fonts뿐이다.

## 먼저 읽으면 좋은 편

선형 회귀가 처음이라면 페이지의 2번 실습(기본 회귀)부터 읽으면 된다. 시리즈 번호가 정해지면 앞선 편을 연결한다.

## 데이터와 이미지

| 무엇 | 실제 계산인가, 설명용인가 |
|---|---|
| 점수·계수·예측 무게 | 실제 계산 (코드 1·2, scikit-learn 1.9.1) |
| 예측 곡선의 가로축 경로 | 설명용. 높이·폭을 길이로 어림한 가상 농어 |
| 5조각 돌리기 애니메이션 | 설명용 도식 |
| 여행 가방·저울·기출문제 비유 | 설명용 비유 (페이지 D 섹션에 틀리는 지점을 적음) |
| 캐릭터 그림 | adminmrobo/fruitfly-lab-expressions (ea5da3f) |

농어 데이터: 박해선, 『혼자 공부하는 머신러닝+딥러닝』 개정판(한빛미디어, 2025)의 실습 데이터, rickiepark/hg-mldl 저장소 perch_full.csv.

## 용어 표기

- 규제(regularization)는 "정규화"라고도 하지만, 표준화(standardization)와 헷갈리지 않도록 이 페이지는 "규제"로 통일했다.
- 릿지·라쏘의 규제를 처음부터 끝까지 **여행 가방** 비유로 쓴다. alpha가 클수록 가방이 작아진다.
- 계수가 큰 모델은 **지나치게 예민한 저울**, 과적합은 **기출문제만 외운 학생**으로 부른다.

## 라이선스

[크리에이티브 커먼즈 저작자표시-비영리 4.0 국제 라이선스(CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.ko)

출처 표기 예: 「릿지와 라쏘 — 농어 무게로 배우는 과적합 막기」, 글 · 안상선, CC BY-NC 4.0.

---

<a id="en"></a>

# Ridge and Lasso — Stopping Overfitting by Weighing Perch

Website: https://adminmrobo.github.io/Regression_ridge_lasso/ · Contents: [index.en.html](index.en.html) · Open the explainer: [RG_ridge_lasso.en.html](RG_ridge_lasso.en.html)

![Cover](og_rg.jpg)

An interactive educational page where you predict the weight of 56 perch from their length, height and width, and get hands-on in the browser with the overfitting that appears as you add features, the ridge and lasso that stop it, and the cross-validation that chooses alpha. The Doctor, Haru (the Assistant), the Fruit Fly Researcher and AbaBot guide you through speech bubbles, and every key number comes from actually running the 2 Colab code blocks on the page.

**View now:** https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.en.html

**Author:** Written by Ahn Sangsun (CEO, M-Robo Co., Ltd.)

## Languages

- **How to choose:** Use the 🌐 language selector in the top menu, or click the 🌐 banner at the bottom right of the screen. Your choice is remembered by the browser.
- **Automatic switching:** When you arrive at the Korean page, it opens in your remembered language if there is one; otherwise, it opens in your browser language if that language is supported. Unsupported languages stay in Korean. Visitors who arrive at a translated page's address are not switched automatically.
- **Choosing by address:** Add something like `?lang=en` to the address to open the page in that language and remember it. Any `#section` is kept as is.
- **Language exceptions:** None. This page has no exercise that only works with Korean input.

| Language | File name | View |
|---|---|---|
| 한국어 | RG_ridge_lasso.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.html |
| English | RG_ridge_lasso.en.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.en.html |
| 中文 | RG_ridge_lasso.zh.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.zh.html |
| 日本語 | RG_ridge_lasso.ja.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ja.html |
| Oʻzbekcha | RG_ridge_lasso.uz.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.uz.html |
| Русский | RG_ridge_lasso.ru.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ru.html |
| Tiếng Việt | RG_ridge_lasso.vi.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.vi.html |

## Contents

| Episode | Title | What it covers | Difficulty |
|---|---|---|---|
| RG | Ridge and Lasso — Stopping Overfitting by Weighing Perch | Basic linear regression, polynomial features and overfitting, ridge (L2), lasso (L1), choosing alpha with cross-validation | ★★★ |

## The journey of the perch data

| What goes in | What comes out | Question for the next episode |
|---|---|---|
| Length, height, width (cm) and weight (g) of 56 perch | Ridge and lasso models that hold down the coefficients of 55 features, alpha chosen by cross-validation, and the 8 features kept by lasso | Could the model find relationships between features by itself, without a person building them? If we mix ridge and lasso (elastic net), does the similar-features problem shrink? |

## Key numbers

| Number | Meaning | Source |
|---|---|---|
| Training 0.9997 / test −4.3927 | R² of basic regression with 55 features. Overfitting that memorized the training data | Code 1 |
| 417,225 | Size of that model's largest coefficient | Code 1 |
| 0.9725 | Test R² of ridge α=10, chosen by cross-validation | Code 2 |
| 8 / 55 · 0.9802 | Number of features kept by lasso α=1, and its test R² | Code 2 |

## What's on the page

| Order | Section | Main hands-on parts |
|---|---|---|
| 1 | Orders | Conversation among the lab crew, big-picture flow chart |
| 2 | Basic regression | Length–weight scatter plot with prediction line, the perch scale (14 test perch) |
| 3 | Adding features | Degree slider 1–5, training/test R² bars, the prediction line swinging wildly |
| 4 | Ridge | alpha slider, bars for the 55 coefficients (log scale), comparison with coefficients before regularization |
| 5 | Lasso | alpha slider, coefficients that drop out by going to 0, number of features left |
| 6 | Choosing alpha | Cross-validation average vs. test score, rotating 5 folds for grading |
| — | Duel | Keep all 55 features vs. ridge, judged on the sealed test set |
| 7 | Limits and the next mission | What it can and cannot do, summary table by exercise |
| A–F | Colab code · AI prompts for applying it · Glossary · Analogies · About the author and references · Tips for educators | |
| — | Knowledge index · Ontology & bibliography package | Concept search, relation graph, JSON-LD·Turtle·CSV·BibTeX·RIS package (ZIP) |

## Colab code

| Code 1 | Code 2 | Libraries | Run time |
|---|---|---|---|
| Adding features makes the test score collapse (sections 2·3) | Holding down the coefficients and choosing alpha by cross-validation (sections 4–6, duel) | numpy, scikit-learn, matplotlib (preinstalled on Colab) | About 2–3 s each on CPU |

Each code panel offers Copy · Download .py · Download notebook (.ipynb). Tested: 2026-10-29, numpy 2.5 · scikit-learn 1.9 · matplotlib 3.11.

## Files

```
RG_ridge_lasso.html                    Korean original
RG_ridge_lasso.en.html  .zh.html  .ja.html
RG_ridge_lasso.uz.html  .ru.html  .vi.html
README.md
index.html  index.en.html  index.zh.html  index.ja.html
index.uz.html  index.ru.html  index.vi.html
thumb_rg.webp  og_rg.jpg  hero_rg.webp  (cover_index.webp)
cover_manifest.json
code/rg_code1_overfitting.py  code/rg_code2_ridge_lasso.py
docs/COVER_00_index.md  docs/COVER_RG_ridge_lasso.md
docs/IMG_RG_ridge_lasso.md  docs/KG_00_registry_additions.json
```

| File | Size |
|---|---|
| RG_ridge_lasso.html | 576 KB |
| RG_ridge_lasso.en.html | 576 KB |
| RG_ridge_lasso.zh.html | 569 KB |
| RG_ridge_lasso.ja.html | 583 KB |
| RG_ridge_lasso.uz.html | 585 KB |
| RG_ridge_lasso.ru.html | 623 KB |
| RG_ridge_lasso.vi.html | 590 KB |
| index.html | 15 KB |
| index.en.html | 15 KB |
| index.zh.html | 15 KB |
| index.ja.html | 16 KB |
| index.uz.html | 16 KB |
| index.ru.html | 17 KB |
| index.vi.html | 16 KB |

Every HTML file contains its images, data and scripts in a single file. No build step is needed; just open it in a browser. The only external resource is Google Fonts.

## Good to read first

If linear regression is new to you, start with exercise 2 (basic regression) on the page. Earlier episodes will be linked once series numbers are set.

## Data and images

| What | Actual calculation or illustration? |
|---|---|
| Scores, coefficients, predicted weights | Actual calculation (Code 1·2, scikit-learn 1.9.1) |
| Horizontal path of the prediction curves | Illustration. Imaginary perch with height and width estimated from length |
| 5-fold rotation animation | Illustrative diagram |
| Suitcase, scale and past-exam analogies | Illustrative analogies (where each one breaks is noted in section D of the page) |
| Character art | adminmrobo/fruitfly-lab-expressions (ea5da3f) |

Perch data: practice data from Park Haesun, *Honja Gongbuhaneun Machine Learning+Deep Learning* [Machine Learning + Deep Learning for Self-Study], revised ed. (Hanbit Media, 2025); perch_full.csv in the rickiepark/hg-mldl repository.

## Terminology

- In Korean, regularization (규제) is sometimes also called "정규화," which is easily confused with standardization (표준화), so the Korean page uses "규제" throughout. The English page uses "regularization" throughout.
- Regularization in ridge and lasso is explained with the **suitcase** analogy from start to finish. The larger alpha is, the smaller the suitcase.
- A model with large coefficients is called **an over-sensitive scale**, and overfitting is **a student who memorized past exams**.

## License

[Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.en)

Example attribution: "Ridge and Lasso — Stopping Overfitting by Weighing Perch", Written by Ahn Sangsun, CC BY-NC 4.0.

---

<a id="zh"></a>

# 岭回归与 Lasso——用鲈鱼体重学习如何防止过拟合

网址：https://adminmrobo.github.io/Regression_ridge_lasso/ · 目录：[index.zh.html](index.zh.html) · 直接打开讲解：[RG_ridge_lasso.zh.html](RG_ridge_lasso.zh.html)

![封面](og_rg.jpg)

用 56 条鲈鱼的长度·高度·宽度预测体重，在浏览器中亲手操作增加特征时出现的过拟合、防止过拟合的岭回归·Lasso，以及用交叉验证选择 alpha。这是一个交互式教学页面。由博士 · Haru（助手）· 果蝇研究员 · 算盘宝 用对话气泡带领讲解，所有关键数字都是实际运行页面内 2 段 Colab 代码得到的结果。

**在线查看：** https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.zh.html

**作者：** 作者 · Ahn Sangsun（M-Robo 株式会社代表）

## 语言

- **选择方法：** 点击顶部菜单的 🌐 语言选择框，或屏幕右下角的 🌐 横幅。所选语言会保存在浏览器中。
- **自动切换：** 进入韩语页面时，若已保存语言，则用该语言打开；若没有保存，而浏览器语言是支持的语言，则用浏览器语言打开。不支持的语言保持韩语。从译本网址进入的访问者不会被自动切换。
- **用网址选择：** 在网址后加上 `?lang=en` 这样的参数，就会用该语言打开并保存。`#章节` 保持不变。
- **语言例外：** 无。本页没有必须输入韩语才能运行的实践。

| 语言 | 文件名 | 在线查看 |
|---|---|---|
| 한국어 | RG_ridge_lasso.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.html |
| English | RG_ridge_lasso.en.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.en.html |
| 中文 | RG_ridge_lasso.zh.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.zh.html |
| 日本語 | RG_ridge_lasso.ja.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ja.html |
| Oʻzbekcha | RG_ridge_lasso.uz.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.uz.html |
| Русский | RG_ridge_lasso.ru.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ru.html |
| Tiếng Việt | RG_ridge_lasso.vi.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.vi.html |

## 构成

| 篇 | 标题 | 内容 | 难度 |
|---|---|---|---|
| RG | 岭回归与 Lasso——用鲈鱼体重学习如何防止过拟合 | 基础线性回归，多项式特征与过拟合，岭回归（L2），Lasso（L1），用交叉验证选择 alpha | ★★★ |

## 鲈鱼数据走过的路

| 输入 | 输出 | 留给下一篇的问题 |
|---|---|---|
| 56 条鲈鱼的长度·高度·宽度(cm)与体重(g) | 在 55 个特征上约束系数的岭回归·Lasso 模型，交叉验证选出的 alpha，Lasso 保留的 8 个特征 | 特征之间的关系即使没有人来构造，能不能让模型自己找出来？把岭回归和 Lasso 混合起来（弹性网络），相似特征的问题会减轻吗？ |

## 关键数字

| 数字 | 含义 | 出处 |
|---|---|---|
| 训练 0.9997 / 测试 −4.3927 | 55 个特征的基础回归的 R²。背下训练数据的过拟合 | 代码 1 |
| 417,225 | 该模型的最大系数大小 | 代码 1 |
| 0.9725 | 交叉验证选出的岭回归 α=10 的测试 R² | 代码 2 |
| 8 / 55 · 0.9802 | Lasso α=1 保留的特征数与测试 R² | 代码 2 |

## 页面内容

| 顺序 | 章节 | 主要实践 |
|---|---|---|
| 1 | 指令 | 研究室成员对话，整体流程图 |
| 2 | 基础回归 | 长度–体重散点图与预测线，鲈鱼秤（测试 14 条） |
| 3 | 增加特征 | degree 滑块 1~5，训练·测试 R² 柱状图，预测线剧烈晃动的样子 |
| 4 | 岭回归 | alpha 滑块，55 个系数柱状图（对数刻度），与正则化前的系数比较 |
| 5 | Lasso | alpha 滑块，变为 0 而被去掉的系数，剩余特征数 |
| 6 | 选择 alpha | 交叉验证平均与测试分数的比较，5 份轮流评分 |
| — | 对决 | 55 个特征原样使用 vs 岭回归，用封存的测试集判定 |
| 7 | 局限与下一个任务 | 能做到的·做不到的，各实践汇总表 |
| A~F | Colab 代码 · AI 应用提示词 · 术语表 · 比喻汇总 · 作者简介与参考文献 · 教师指南 | |
| — | 知识索引 · 本体与书目资料包 | 概念搜索，关系图，JSON-LD·Turtle·CSV·BibTeX·RIS 资料包（ZIP） |

## Colab 代码

| 代码 1 | 代码 2 | 库 | 运行时间 |
|---|---|---|---|
| 增加特征后测试分数崩溃（第 2·3 节） | 约束系数，并用交叉验证选择 alpha（第 4~6 节，对决） | numpy, scikit-learn, matplotlib（Colab 默认已安装） | 各约 CPU 2~3 秒 |

每个代码面板都可以复制 · 下载 .py · 下载笔记本 (.ipynb)。运行确认：2026-10-29，numpy 2.5 · scikit-learn 1.9 · matplotlib 3.11。

## 文件

```
RG_ridge_lasso.html                    韩语原版
RG_ridge_lasso.en.html  .zh.html  .ja.html
RG_ridge_lasso.uz.html  .ru.html  .vi.html
README.md
index.html  index.en.html  index.zh.html  index.ja.html
index.uz.html  index.ru.html  index.vi.html
thumb_rg.webp  og_rg.jpg  hero_rg.webp  (cover_index.webp)
cover_manifest.json
code/rg_code1_overfitting.py  code/rg_code2_ridge_lasso.py
docs/COVER_00_index.md  docs/COVER_RG_ridge_lasso.md
docs/IMG_RG_ridge_lasso.md  docs/KG_00_registry_additions.json
```

| 文件 | 大小 |
|---|---|
| RG_ridge_lasso.html | 576 KB |
| RG_ridge_lasso.en.html | 576 KB |
| RG_ridge_lasso.zh.html | 569 KB |
| RG_ridge_lasso.ja.html | 583 KB |
| RG_ridge_lasso.uz.html | 585 KB |
| RG_ridge_lasso.ru.html | 623 KB |
| RG_ridge_lasso.vi.html | 590 KB |
| index.html | 15 KB |
| index.en.html | 15 KB |
| index.zh.html | 15 KB |
| index.ja.html | 16 KB |
| index.uz.html | 16 KB |
| index.ru.html | 17 KB |
| index.vi.html | 16 KB |

所有 HTML 都把图片·数据·脚本放在同一个文件里。无需构建，用浏览器直接打开即可。唯一从外部加载的是 Google Fonts。

## 建议先读的篇目

如果你第一次接触线性回归，从页面的第 2 个实践（基础回归）读起即可。系列编号确定后，会链接更早的篇目。

## 数据与图片

| 内容 | 实际计算还是仅供说明 |
|---|---|
| 分数·系数·预测体重 | 实际计算（代码 1·2，scikit-learn 1.9.1） |
| 预测曲线横轴上的路径 | 仅供说明。把高度·宽度按长度近似的虚拟鲈鱼 |
| 5 份轮换动画 | 仅供说明的示意图 |
| 旅行箱·秤·历年真题的比喻 | 仅供说明的比喻（失效之处写在页面 D 节） |
| 角色插图 | adminmrobo/fruitfly-lab-expressions (ea5da3f) |

鲈鱼数据：Park Haesun《Honja Gongbuhaneun Machine Learning+Deep Learning》[自学机器学习+深度学习] 修订版（Hanbit Media，2025）的实践数据，rickiepark/hg-mldl 仓库 perch_full.csv。

## 术语说明

- 正则化（regularization）也常被称为“规则化”，但为了不与标准化（standardization）混淆，本页统一使用“正则化”。
- 岭回归·Lasso 的正则化从头到尾都用**旅行箱**来比喻。alpha 越大，箱子越小。
- 系数大的模型称为**过于敏感的秤**，过拟合称为**只背历年真题的学生**。

## 许可协议

[知识共享 署名-非商业性使用 4.0 国际许可协议（CC BY-NC 4.0）](https://creativecommons.org/licenses/by-nc/4.0/deed.zh-hans)

署名示例：《岭回归与 Lasso——用鲈鱼体重学习如何防止过拟合》，作者 · Ahn Sangsun，CC BY-NC 4.0。

---

<a id="ja"></a>

# リッジとラッソ — スズキの重さで学ぶ過学習の防ぎ方

公開アドレス：https://adminmrobo.github.io/Regression_ridge_lasso/ · 目次：[index.ja.html](index.ja.html) · 解説を開く：[RG_ridge_lasso.ja.html](RG_ridge_lasso.ja.html)

![表紙](og_rg.jpg)

スズキ56匹の長さ・高さ・幅から重さを予測しながら、特徴を増やすと起こる過学習と、それを防ぐリッジ・ラッソ、そしてalphaを選ぶ交差検証をブラウザで実際に触って確かめる、インタラクティブな教育ページである。博士・ハル（助手）・ショウジョウバエ研究員・アバボットが吹き出しで進行し、主要な数字はすべてページ内のColabコード2本を実際に実行した結果である。

**すぐに見る:** https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ja.html

**著者:** 文・アン・サンソン（株式会社M-Robo代表）

## 言語

- **選び方:** 最上部メニューの🌐言語選択ボックス、または画面右下の🌐バナーを押す。選んだ言語はブラウザに記憶される。
- **自動切り替え:** 韓国語ページに入ると、記憶された言語があればその言語で、なければブラウザの言語が対応言語の場合にその言語で開く。対応していない言語では韓国語のままである。翻訳版のURLから入った人には自動切り替えを行わない。
- **URLで選ぶ:** URLの後ろに `?lang=en` のように付けると、その言語で開いて記憶する。`#セクション` はそのまま保たれる。
- **言語の例外:** なし。このページには、韓国語の入力がなければ動かない実習はない。

| 言語 | ファイル名 | すぐに見る |
|---|---|---|
| 한국어 | RG_ridge_lasso.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.html |
| English | RG_ridge_lasso.en.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.en.html |
| 中文 | RG_ridge_lasso.zh.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.zh.html |
| 日本語 | RG_ridge_lasso.ja.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ja.html |
| Oʻzbekcha | RG_ridge_lasso.uz.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.uz.html |
| Русский | RG_ridge_lasso.ru.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ru.html |
| Tiếng Việt | RG_ridge_lasso.vi.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.vi.html |

## 構成

| 回 | タイトル | 扱う内容 | 難易度 |
|---|---|---|---|
| RG | リッジとラッソ — スズキの重さで学ぶ過学習の防ぎ方 | 基本の線形回帰、多項式特徴と過学習、リッジ（L2）、ラッソ（L1）、交差検証によるalphaの選択 | ★★★ |

## スズキのデータがたどった道

| 入るもの | 出てくるもの | 次の回へ渡す問い |
|---|---|---|
| スズキ56匹の長さ・高さ・幅（cm）と重さ（g） | 特徴55個で係数を抑えたリッジ・ラッソのモデル、交差検証で選んだalpha、ラッソが残した特徴8個 | 特徴どうしの関係を人が作ってやらなくても、モデル自身に見つけさせることはできないだろうか？リッジとラッソを混ぜれば（エラスティックネット）、似た特徴の問題は減るだろうか？ |

## 主要な数字

| 数字 | 意味 | 出典 |
|---|---|---|
| 訓練 0.9997 / テスト −4.3927 | 特徴55個の基本回帰のR²。訓練データを丸暗記した過学習 | コード1 |
| 417,225 | そのモデルの最大の係数の大きさ | コード1 |
| 0.9725 | 交差検証が選んだリッジ α=10のテストR² | コード2 |
| 8 / 55 · 0.9802 | ラッソ α=1が残した特徴の数とテストR² | コード2 |

## ページに入っているもの

| 順番 | セクション | 主な実習 |
|---|---|---|
| 1 | 指令 | 研究室の仲間たちの会話、全体像の流れ図 |
| 2 | 基本の回帰 | 長さ–重さの散布図と予測線、スズキのはかり（テスト14匹） |
| 3 | 特徴を増やす | degreeスライダー1〜5、訓練・テストR²の棒グラフ、予測線が揺れる様子 |
| 4 | リッジ | alphaスライダー、係数55個の棒グラフ（対数目盛り）、正則化前の係数との比較 |
| 5 | ラッソ | alphaスライダー、0になって外れる係数、残った特徴の数 |
| 6 | alphaを選ぶ | 交差検証平均とテストスコアの比較、5つの束を順に回して採点 |
| — | 対決 | 特徴55個そのまま vs リッジ、封印したテストで判定 |
| 7 | 限界と次のミッション | できること・できないこと、実習ごとのまとめ表 |
| A〜F | Colabコード・AI応用プロンプト・用語集・たとえ集・著者紹介と参考文献・教育者向けTIP | |
| — | 知識索引・オントロジー・書誌パッケージ | 概念検索、関係グラフ、JSON-LD・Turtle・CSV・BibTeX・RISパッケージ（ZIP） |

## Colabコード

| コード1 | コード2 | ライブラリ | 実行時間 |
|---|---|---|---|
| 特徴を増やすとテストスコアが崩れる（セクション2・3） | 係数を抑え、alphaを交差検証で選ぶ（セクション4〜6、対決） | numpy, scikit-learn, matplotlib（Colabに標準でインストール済み） | それぞれCPUで約2〜3秒 |

各コードパネルから、コピー・.pyをダウンロード・ノートブック(.ipynb)をダウンロードができる。動作確認：2026-10-29、numpy 2.5・scikit-learn 1.9・matplotlib 3.11。

## ファイル

```
RG_ridge_lasso.html                    韓国語の原本
RG_ridge_lasso.en.html  .zh.html  .ja.html
RG_ridge_lasso.uz.html  .ru.html  .vi.html
README.md
index.html  index.en.html  index.zh.html  index.ja.html
index.uz.html  index.ru.html  index.vi.html
thumb_rg.webp  og_rg.jpg  hero_rg.webp  (cover_index.webp)
cover_manifest.json
code/rg_code1_overfitting.py  code/rg_code2_ridge_lasso.py
docs/COVER_00_index.md  docs/COVER_RG_ridge_lasso.md
docs/IMG_RG_ridge_lasso.md  docs/KG_00_registry_additions.json
```

| ファイル | サイズ |
|---|---|
| RG_ridge_lasso.html | 576 KB |
| RG_ridge_lasso.en.html | 576 KB |
| RG_ridge_lasso.zh.html | 569 KB |
| RG_ridge_lasso.ja.html | 583 KB |
| RG_ridge_lasso.uz.html | 585 KB |
| RG_ridge_lasso.ru.html | 623 KB |
| RG_ridge_lasso.vi.html | 590 KB |
| index.html | 15 KB |
| index.en.html | 15 KB |
| index.zh.html | 15 KB |
| index.ja.html | 16 KB |
| index.uz.html | 16 KB |
| index.ru.html | 17 KB |
| index.vi.html | 16 KB |

すべてのHTMLは、画像・データ・スクリプトを1つのファイルに収めている。ビルドの手順は不要で、ブラウザで開くだけでよい。外部から読み込むのはGoogle Fontsだけである。

## 先に読んでおくとよい回

線形回帰が初めてなら、ページの2番目の実習（基本の回帰）から読めばよい。シリーズ番号が決まったら、前の回へリンクする。

## データと画像

| 何か | 実際の計算か、説明用か |
|---|---|
| スコア・係数・予測の重さ | 実際の計算（コード1・2、scikit-learn 1.9.1） |
| 予測曲線の横軸の経路 | 説明用。高さ・幅を長さから見積もった仮想のスズキ |
| 5つの束を回すアニメーション | 説明用の図式 |
| スーツケース・はかり・過去問のたとえ | 説明用のたとえ（ページのDセクションに外れるところを記載） |
| キャラクターの絵 | adminmrobo/fruitfly-lab-expressions (ea5da3f) |

スズキのデータ：Park Haesun『Honja Gongbuhaneun Machine Learning+Deep Learning』[独学で学ぶ機械学習＋ディープラーニング] 改訂版（Hanbit Media, 2025）の実習データ、rickiepark/hg-mldl リポジトリの perch_full.csv。

## 用語の表記

- 正則化（regularization）は「正規化」とも呼ばれるが、標準化（standardization）と混同しないよう、このページでは「正則化」に統一した。
- リッジ・ラッソの正則化は、最初から最後まで**スーツケース**のたとえで説明する。alphaが大きいほどスーツケースは小さくなる。
- 係数が大きいモデルは**敏感すぎるはかり**、過学習は**過去問だけを丸暗記した学生**と呼ぶ。

## ライセンス

[クリエイティブ・コモンズ 表示-非営利 4.0 国際ライセンス（CC BY-NC 4.0）](https://creativecommons.org/licenses/by-nc/4.0/deed.ja)

クレジット表記の例：「リッジとラッソ — スズキの重さで学ぶ過学習の防ぎ方」、文・アン・サンソン、CC BY-NC 4.0。

---

<a id="uz"></a>

# Ridge va lasso — olabugʻa vazni misolida ortiqcha moslashishni toʻxtatish

Sayt manzili: https://adminmrobo.github.io/Regression_ridge_lasso/ · Mundarija: [index.uz.html](index.uz.html) · Izohni ochish: [RG_ridge_lasso.uz.html](RG_ridge_lasso.uz.html)

![Muqova](og_rg.jpg)

Bu interaktiv oʻquv sahifasida 56 ta olabugʻaning uzunligi, balandligi va eni boʻyicha vaznini bashorat qilasiz. Belgilar koʻpayganda yuzaga keladigan ortiqcha moslashishni, uni toʻxtatadigan ridge va lassoni hamda alpha ni tanlaydigan kross-validatsiyani brauzerda oʻz qoʻlingiz bilan sinab koʻrasiz. Sahifani Doktor · Haru (Yordamchi) · Drozofila tadqiqotchisi · AbaBot soʻz pufakchalari orqali olib boradi. Barcha asosiy raqamlar sahifadagi 2 ta Colab kodini haqiqatan ishga tushirib olingan natijalardir.

**Darhol koʻrish:** https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.uz.html

**Muallif:** Ahn Sangsun (M-Robo kompaniyasi rahbari)

## Til

- **Qanday tanlanadi:** eng yuqoridagi menyudagi 🌐 til tanlash qutisini yoki ekranning oʻng pastki burchagidagi 🌐 bannerni bosing. Tanlangan til brauzerda eslab qolinadi.
- **Avtomatik almashtirish:** koreyscha sahifaga kirganingizda, eslab qolingan til boʻlsa, sahifa oʻsha tilda ochiladi. Boʻlmasa, brauzer tili qoʻllab-quvvatlanadigan tillardan biri boʻlsa, oʻsha tilda ochiladi. Qoʻllab-quvvatlanmaydigan tillarda sahifa koreyscha qoladi. Tarjima sahifasi manzili orqali kirganlar uchun avtomatik almashtirish ishlamaydi.
- **Manzil orqali tanlash:** manzil oxiriga `?lang=en` kabi qoʻshsangiz, sahifa oʻsha tilda ochiladi va til eslab qolinadi. `#boʻlim` qismi saqlanib qoladi.
- **Til boʻyicha istisnolar:** yoʻq. Bu sahifada faqat koreyscha kiritish bilan ishlaydigan amaliyot yoʻq.

| Til | Fayl nomi | Darhol koʻrish |
|---|---|---|
| 한국어 | RG_ridge_lasso.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.html |
| English | RG_ridge_lasso.en.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.en.html |
| 中文 | RG_ridge_lasso.zh.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.zh.html |
| 日本語 | RG_ridge_lasso.ja.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ja.html |
| Oʻzbekcha | RG_ridge_lasso.uz.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.uz.html |
| Русский | RG_ridge_lasso.ru.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ru.html |
| Tiếng Việt | RG_ridge_lasso.vi.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.vi.html |

## Tuzilishi

| Qism | Sarlavha | Mazmuni | Qiyinligi |
|---|---|---|---|
| RG | Ridge va lasso — olabugʻa vazni misolida ortiqcha moslashishni toʻxtatish | Oddiy chiziqli regressiya, polinomial belgilar va ortiqcha moslashish, ridge (L2), lasso (L1), kross-validatsiya bilan alpha tanlash | ★★★ |

## Olabugʻa ma’lumotlari bosib oʻtgan yoʻl

| Kirish | Chiqish | Keyingi qismga oʻtadigan savol |
|---|---|---|
| 56 ta olabugʻaning uzunligi, balandligi, eni (cm) va vazni (g) | 55 ta belgida koeffitsiyentlarni cheklagan ridge va lasso modellari, kross-validatsiya bilan tanlangan alpha, lasso qoldirgan 8 ta belgi | Belgilar orasidagi bogʻliqlikni inson yaratib bermasa ham, model ularni oʻzi topa oladimi? Ridge va lassoni aralashtirsak (elastic net), oʻxshash belgilar muammosi kamayadimi? |

## Asosiy raqamlar

| Raqam | Ma’nosi | Manba |
|---|---|---|
| Oʻqitish 0.9997 / test −4.3927 | 55 ta belgili oddiy regressiyaning R². Oʻqitish ma’lumotlarini yodlab olgan ortiqcha moslashish | 1-kod |
| 417,225 | Shu modelning eng katta koeffitsiyent kattaligi | 1-kod |
| 0.9725 | Kross-validatsiya tanlagan ridge α=10 ning test R² natijasi | 2-kod |
| 8 / 55 · 0.9802 | Lasso α=1 qoldirgan belgilar soni va test R² | 2-kod |

## Sahifada nimalar bor

| Tartib | Boʻlim | Asosiy amaliyot |
|---|---|---|
| 1 | Topshiriq | Laboratoriya jamoasining suhbati, umumiy oqim sxemasi |
| 2 | Oddiy regressiya | Uzunlik va vazn sochilish diagrammasi, bashorat chizigʻi, olabugʻa tarozisi (14 ta test olabugʻasi) |
| 3 | Belgilarni koʻpaytirish | degree slayderi 1–5, oʻqitish va test R² ustunlari, bashorat chizigʻining tebranishi |
| 4 | Ridge | alpha slayderi, 55 ta koeffitsiyent ustunlari (logarifmik shkala), regulyarizatsiyadan oldingi koeffitsiyentlar bilan solishtirish |
| 5 | Lasso | alpha slayderi, 0 ga aylanib chiqib ketadigan koeffitsiyentlar, qolgan belgilar soni |
| 6 | alpha tanlash | Kross-validatsiya oʻrtachasi va test natijasini solishtirish, 5 qismni almashtirib baholash |
| — | Bellashuv | 55 ta belgi oʻzgarishsiz vs ridge, muhrlangan test bilan hukm |
| 7 | Cheklovlar va keyingi missiya | Nima mumkin va nima mumkin emas, amaliyotlar boʻyicha xulosa jadvali |
| A–F | Colab kodi · AI uchun amaliy promptlar · Atamalar lugʻati · Oʻxshatishlar toʻplami · Muallif haqida va manbalar · Oʻqituvchilar uchun maslahatlar | |
| — | Bilimlar indeksi · Ontologiya va bibliografiya paketi | Tushunchalarni qidirish, aloqalar grafigi, JSON-LD · Turtle · CSV · BibTeX · RIS paketi (ZIP) |

## Colab kodi

| 1-kod | 2-kod | Kutubxonalar | Bajarilish vaqti |
|---|---|---|---|
| Belgilar koʻpaysa, test natijasi qulaydi (2- va 3-boʻlimlar) | Koeffitsiyentlarni cheklash va alpha ni kross-validatsiya bilan tanlash (4–6-boʻlimlar, bellashuv) | numpy, scikit-learn, matplotlib (Colab da oldindan oʻrnatilgan) | Har biri CPU da taxminan 2–3 soniya |

Har bir kod panelida nusxalash · .py yuklab olish · Notebook (.ipynb) yuklab olish mumkin. Tekshirilgan: 2026-10-29, numpy 2.5 · scikit-learn 1.9 · matplotlib 3.11.

## Fayllar

```
RG_ridge_lasso.html                    koreyscha asl nusxa
RG_ridge_lasso.en.html  .zh.html  .ja.html
RG_ridge_lasso.uz.html  .ru.html  .vi.html
README.md
index.html  index.en.html  index.zh.html  index.ja.html
index.uz.html  index.ru.html  index.vi.html
thumb_rg.webp  og_rg.jpg  hero_rg.webp  (cover_index.webp)
cover_manifest.json
code/rg_code1_overfitting.py  code/rg_code2_ridge_lasso.py
docs/COVER_00_index.md  docs/COVER_RG_ridge_lasso.md
docs/IMG_RG_ridge_lasso.md  docs/KG_00_registry_additions.json
```

| Fayl | Hajmi |
|---|---|
| RG_ridge_lasso.html | 576 KB |
| RG_ridge_lasso.en.html | 576 KB |
| RG_ridge_lasso.zh.html | 569 KB |
| RG_ridge_lasso.ja.html | 583 KB |
| RG_ridge_lasso.uz.html | 585 KB |
| RG_ridge_lasso.ru.html | 623 KB |
| RG_ridge_lasso.vi.html | 590 KB |
| index.html | 15 KB |
| index.en.html | 15 KB |
| index.zh.html | 15 KB |
| index.ja.html | 16 KB |
| index.uz.html | 16 KB |
| index.ru.html | 17 KB |
| index.vi.html | 16 KB |

Har bir HTML fayl rasmlar, ma’lumotlar va skriptlarni oʻz ichiga oladi. Hech qanday yigʻish (build) jarayoni kerak emas — faylni brauzerda ochish kifoya. Tashqaridan faqat Google Fonts yuklanadi.

## Avval oʻqish foydali boʻlgan qismlar

Chiziqli regressiya siz uchun yangi boʻlsa, sahifaning 2-amaliyotidan (oddiy regressiya) boshlang. Turkum raqami belgilangach, oldingi qismlar bogʻlanadi.

## Ma’lumotlar va rasmlar

| Nima | Haqiqiy hisob-kitobmi yoki tushuntirish uchunmi |
|---|---|
| Natijalar · koeffitsiyentlar · bashorat qilingan vaznlar | Haqiqiy hisob-kitob (1- va 2-kod, scikit-learn 1.9.1) |
| Bashorat egri chizigʻining gorizontal oʻqi boʻyicha yoʻl | Tushuntirish uchun. Balandligi va eni uzunlikdan taxmin qilingan xayoliy olabugʻa |
| 5 qismni almashtirish animatsiyasi | Tushuntirish uchun sxema |
| Chamadon · tarozi · oʻtgan yillar savollari oʻxshatishlari | Tushuntirish uchun oʻxshatishlar (notoʻgʻri boʻladigan joylari sahifaning D boʻlimida yozilgan) |
| Qahramonlar rasmlari | adminmrobo/fruitfly-lab-expressions (ea5da3f) |

Olabugʻa ma’lumotlari: Park Haesun, Honja Gongbuhaneun Machine Learning+Deep Learning [Mustaqil oʻrganish uchun Machine Learning + Deep Learning], qayta ishlangan nashr (Hanbit Media, 2025) kitobidagi amaliy ma’lumotlar, rickiepark/hg-mldl repozitoriysidagi perch_full.csv.

## Atamalar haqida

- Regulyarizatsiya (regularization) ba’zan “normallashtirish” deb ham ataladi. Biroq standartlashtirish (standardization) bilan adashtirmaslik uchun bu sahifada doim “regulyarizatsiya” atamasi ishlatiladi.
- Ridge va lassodagi regulyarizatsiya boshidan oxirigacha **chamadon** oʻxshatishi bilan tushuntiriladi: alpha qancha katta boʻlsa, chamadon shuncha kichik.
- Koeffitsiyentlari katta model **haddan tashqari sezgir tarozi**, ortiqcha moslashish esa **faqat oʻtgan yillar savollarini yodlab olgan talaba** deb ataladi.

## Litsenziya

[Creative Commons Attribution-NonCommercial 4.0 International litsenziyasi (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.en)

Manbani koʻrsatish namunasi: «Ridge va lasso — olabugʻa vazni misolida ortiqcha moslashishni toʻxtatish», Muallif · Ahn Sangsun, CC BY-NC 4.0.

---

<a id="ru"></a>

# Ридж и лассо: как удержать модель от переобучения на примере веса окуня

Адрес сайта: https://adminmrobo.github.io/Regression_ridge_lasso/ · Содержание: [index.ru.html](index.ru.html) · Открыть разбор: [RG_ridge_lasso.ru.html](RG_ridge_lasso.ru.html)

![Обложка](og_rg.jpg)

Интерактивная учебная страница: вы предсказываете вес 56 окуней по их длине, высоте и ширине и прямо в браузере пробуете, как с ростом числа признаков возникает переобучение, как его сдерживают ридж и лассо и как кросс-валидацией выбирают alpha. Ведут страницу в репликах Доктор, Хару (Ассистент), Исследователь-дрозофила и АбаБот, а все ключевые числа получены реальным запуском двух фрагментов кода для Colab, встроенных в страницу.

**Открыть:** https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ru.html

**Автор:** Автор · Ан Сансон (генеральный директор M-Robo Co., Ltd.)

## Языки

- **Как выбрать:** нажмите на поле выбора языка 🌐 в верхнем меню или на баннер 🌐 в правом нижнем углу экрана. Выбранный язык запоминается в браузере.
- **Автоматическое переключение:** если вы открыли корейскую страницу, она откроется на запомненном языке; если такого нет — на языке браузера, когда он входит в число поддерживаемых. Для неподдерживаемых языков страница остаётся на корейском. Если вы пришли по адресу переведённой версии, автоматического переключения не происходит.
- **Выбор через адрес:** добавьте к адресу, например, `?lang=en` — страница откроется на этом языке и запомнит его. Якорь `#раздел` при этом сохраняется.
- **Языковые исключения:** нет. На этой странице нет практикумов, которые работают только с вводом на корейском.

| Язык | Имя файла | Открыть |
|---|---|---|
| 한국어 | RG_ridge_lasso.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.html |
| English | RG_ridge_lasso.en.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.en.html |
| 中文 | RG_ridge_lasso.zh.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.zh.html |
| 日本語 | RG_ridge_lasso.ja.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ja.html |
| Oʻzbekcha | RG_ridge_lasso.uz.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.uz.html |
| Русский | RG_ridge_lasso.ru.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ru.html |
| Tiếng Việt | RG_ridge_lasso.vi.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.vi.html |

## Состав

| Выпуск | Название | Содержание | Сложность |
|---|---|---|---|
| RG | Ридж и лассо: как удержать модель от переобучения на примере веса окуня | Базовая линейная регрессия, полиномиальные признаки и переобучение, ридж (L2), лассо (L1), выбор alpha кросс-валидацией | ★★★ |

## Путь данных об окунях

| Что на входе | Что на выходе | Вопрос к следующему выпуску |
|---|---|---|
| Длина, высота, ширина (cm) и вес (g) 56 окуней | Модели ридж и лассо со сдержанными коэффициентами на 55 признаках, alpha, выбранный кросс-валидацией, 8 признаков, оставленных лассо | Можно ли сделать так, чтобы модель сама находила связи между признаками, без того чтобы человек их создавал? Если смешать ридж и лассо (эластичная сеть), уменьшится ли проблема похожих признаков? |

## Ключевые числа

| Число | Смысл | Источник |
|---|---|---|
| обучение 0.9997 / тест −4.3927 | R² базовой регрессии на 55 признаках: переобучение, модель зазубрила обучающие данные | Код 1 |
| 417,225 | Наибольший коэффициент этой модели по модулю | Код 1 |
| 0.9725 | Тестовый R² риджа с α=10, выбранным кросс-валидацией | Код 2 |
| 8 / 55 · 0.9802 | Число признаков, оставленных лассо при α=1, и его тестовый R² | Код 2 |

## Что есть на странице

| № | Раздел | Основные практикумы |
|---|---|---|
| 1 | Задание | Диалог команды лаборатории, общая схема |
| 2 | Базовая регрессия | Диаграмма рассеяния «длина — вес» с линией предсказания, весы для окуней (14 тестовых рыб) |
| 3 | Больше признаков | Ползунок degree 1~5, столбцы обучающего и тестового R², скачущая линия предсказания |
| 4 | Ридж | Ползунок alpha, столбцы 55 коэффициентов (логарифмическая шкала), сравнение с коэффициентами до регуляризации |
| 5 | Лассо | Ползунок alpha, коэффициенты, которые обнуляются и исключаются, число оставшихся признаков |
| 6 | Выбор alpha | Сравнение среднего кросс-валидации и тестовой оценки, оценка по 5 частям по кругу |
| — | Поединок | Все 55 признаков как есть vs ридж, вердикт по запечатанному тесту |
| 7 | Ограничения и следующая миссия | Что можно и чего нельзя, сводная таблица по практикумам |
| A~F | Код для Colab · Промпты для применения с ИИ · Глоссарий · Собрание аналогий · Об авторе и источники · Советы преподавателям | |
| — | Индекс знаний · Пакет онтологии и библиографии | Поиск понятий, граф связей, пакет JSON-LD·Turtle·CSV·BibTeX·RIS (ZIP) |

## Код для Colab

| Код 1 | Код 2 | Библиотеки | Время выполнения |
|---|---|---|---|
| Больше признаков — и тестовая оценка рушится (разделы 2·3) | Сдержать коэффициенты и выбрать alpha кросс-валидацией (разделы 4~6, поединок) | numpy, scikit-learn, matplotlib (в Colab установлены по умолчанию) | CPU около 2~3 с каждый |

В панели каждого фрагмента кода доступны кнопки: Копировать · Скачать .py · Скачать ноутбук (.ipynb). Проверено: 2026-10-29, numpy 2.5 · scikit-learn 1.9 · matplotlib 3.11.

## Файлы

```
RG_ridge_lasso.html                    корейский оригинал
RG_ridge_lasso.en.html  .zh.html  .ja.html
RG_ridge_lasso.uz.html  .ru.html  .vi.html
README.md
index.html  index.en.html  index.zh.html  index.ja.html
index.uz.html  index.ru.html  index.vi.html
thumb_rg.webp  og_rg.jpg  hero_rg.webp  (cover_index.webp)
cover_manifest.json
code/rg_code1_overfitting.py  code/rg_code2_ridge_lasso.py
docs/COVER_00_index.md  docs/COVER_RG_ridge_lasso.md
docs/IMG_RG_ridge_lasso.md  docs/KG_00_registry_additions.json
```

| Файл | Размер |
|---|---|
| RG_ridge_lasso.html | 576 KB |
| RG_ridge_lasso.en.html | 576 KB |
| RG_ridge_lasso.zh.html | 569 KB |
| RG_ridge_lasso.ja.html | 583 KB |
| RG_ridge_lasso.uz.html | 585 KB |
| RG_ridge_lasso.ru.html | 623 KB |
| RG_ridge_lasso.vi.html | 590 KB |
| index.html | 15 KB |
| index.en.html | 15 KB |
| index.zh.html | 15 KB |
| index.ja.html | 16 KB |
| index.uz.html | 16 KB |
| index.ru.html | 17 KB |
| index.vi.html | 16 KB |

Каждый HTML-файл содержит рисунки, данные и скрипты внутри себя. Сборка не нужна — достаточно открыть файл в браузере. Извне загружаются только Google Fonts.

## Что полезно прочитать сначала

Если линейная регрессия вам в новинку, начните с практикума 2 на странице (базовая регрессия). Ссылки на предыдущие выпуски появятся, когда будут определены номера в серии.

## Данные и изображения

| Что | Реальный расчёт или иллюстрация |
|---|---|
| Оценки, коэффициенты, предсказанные веса | Реальный расчёт (коды 1·2, scikit-learn 1.9.1) |
| Путь по горизонтальной оси кривых предсказания | Иллюстрация: условные окуни, у которых высота и ширина оценены по длине |
| Анимация с 5 частями по кругу | Иллюстративная схема |
| Аналогии с чемоданом, весами и прошлогодними билетами | Аналогии для объяснения (где они не работают, указано в разделе D страницы) |
| Рисунки персонажей | adminmrobo/fruitfly-lab-expressions (ea5da3f) |

Данные об окунях: учебные данные из книги Park Haesun, *Honja Gongbuhaneun Machine Learning+Deep Learning* [Машинное обучение + глубокое обучение для самостоятельного изучения], исправленное издание (Hanbit Media, 2025); файл perch_full.csv из репозитория rickiepark/hg-mldl.

## О терминах

- Регуляризацию (regularization) иногда называют «нормализацией», но чтобы не путать её со стандартизацией (standardization), на этой странице везде используется термин «регуляризация».
- Регуляризация в ридже и лассо от начала до конца объясняется через аналогию с **чемоданом**: чем больше alpha, тем меньше чемодан.
- Модель с большими коэффициентами называется **слишком чувствительными весами**, а переобучение — **студентом, который вызубрил только прошлогодние билеты**.

## Лицензия

[Лицензия Creative Commons «Атрибуция — Некоммерческое использование» 4.0 Международная (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.ru)

Пример указания источника: «Ридж и лассо: как удержать модель от переобучения на примере веса окуня», Автор · Ан Сансон, CC BY-NC 4.0.

---

<a id="vi"></a>

# Ridge và Lasso — học cách chống quá khớp qua cân nặng cá vược

Địa chỉ trang: https://adminmrobo.github.io/Regression_ridge_lasso/ · Mục lục: [index.vi.html](index.vi.html) · Mở bài giải thích: [RG_ridge_lasso.vi.html](RG_ridge_lasso.vi.html)

![Ảnh bìa](og_rg.jpg)

Đây là trang học tương tác: bạn dự đoán cân nặng từ chiều dài, chiều cao, bề rộng của 56 con cá vược, rồi tự tay thử ngay trên trình duyệt hiện tượng quá khớp khi tăng số đặc trưng, cách Ridge và Lasso ngăn nó, và cách chọn alpha bằng kiểm định chéo. Tiến sĩ · Haru (Trợ lý) · Nhà nghiên cứu Ruồi giấm · AbaBot dẫn dắt bằng các bong bóng thoại, và mọi con số chính đều là kết quả chạy thật 2 đoạn mã Colab có trong trang.

**Xem ngay:** https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.vi.html

**Tác giả:** Ahn Sangsun (Giám đốc điều hành, M-Robo Co., Ltd.)

## Ngôn ngữ

- **Cách chọn:** bấm hộp chọn ngôn ngữ 🌐 ở thanh menu trên cùng, hoặc biểu ngữ 🌐 ở góc dưới bên phải màn hình. Ngôn ngữ đã chọn được trình duyệt ghi nhớ.
- **Tự chuyển:** khi vào trang tiếng Hàn, nếu đã có ngôn ngữ được ghi nhớ thì trang mở bằng ngôn ngữ đó; nếu chưa có mà ngôn ngữ của trình duyệt được hỗ trợ thì mở bằng ngôn ngữ đó. Ngôn ngữ không được hỗ trợ thì giữ nguyên tiếng Hàn. Người vào thẳng địa chỉ của bản dịch sẽ không bị tự chuyển.
- **Chọn qua địa chỉ:** thêm `?lang=en` vào sau địa chỉ thì trang mở bằng ngôn ngữ đó và ghi nhớ lại. `#mục` vẫn được giữ nguyên.
- **Ngoại lệ ngôn ngữ:** không có. Trang này không có bài thực hành nào chỉ chạy được với đầu vào tiếng Hàn.

| Ngôn ngữ | Tên tệp | Xem ngay |
|---|---|---|
| 한국어 | RG_ridge_lasso.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.html |
| English | RG_ridge_lasso.en.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.en.html |
| 中文 | RG_ridge_lasso.zh.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.zh.html |
| 日本語 | RG_ridge_lasso.ja.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ja.html |
| Oʻzbekcha | RG_ridge_lasso.uz.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.uz.html |
| Русский | RG_ridge_lasso.ru.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.ru.html |
| Tiếng Việt | RG_ridge_lasso.vi.html | https://adminmrobo.github.io/Regression_ridge_lasso/RG_ridge_lasso.vi.html |

## Cấu trúc

| Bài | Tiêu đề | Nội dung | Độ khó |
|---|---|---|---|
| RG | Ridge và Lasso — học cách chống quá khớp qua cân nặng cá vược | Hồi quy tuyến tính cơ bản, đặc trưng đa thức và quá khớp, Ridge (L2), Lasso (L1), chọn alpha bằng kiểm định chéo | ★★★ |

## Hành trình của dữ liệu cá vược

| Đầu vào | Đầu ra | Câu hỏi chuyển sang bài tiếp theo |
|---|---|---|
| Chiều dài·chiều cao·bề rộng (cm) và cân nặng (g) của 56 con cá vược | Mô hình Ridge·Lasso kìm giữ hệ số trên 55 đặc trưng, alpha chọn bằng kiểm định chéo, 8 đặc trưng Lasso giữ lại | Liệu có thể để mô hình tự tìm ra quan hệ giữa các đặc trưng mà con người không cần tạo giúp? Nếu trộn Ridge và Lasso (Elastic Net), vấn đề đặc trưng giống nhau có giảm đi không? |

## Các con số chính

| Con số | Ý nghĩa | Nguồn |
|---|---|---|
| Huấn luyện 0.9997 / Kiểm tra −4.3927 | R² của hồi quy cơ bản với 55 đặc trưng. Quá khớp do học thuộc dữ liệu huấn luyện | Mã 1 |
| 417,225 | Độ lớn hệ số lớn nhất của mô hình đó | Mã 1 |
| 0.9725 | R² kiểm tra của Ridge α=10 do kiểm định chéo chọn | Mã 2 |
| 8 / 55 · 0.9802 | Số đặc trưng Lasso α=1 giữ lại và R² kiểm tra | Mã 2 |

## Trang có gì

| Thứ tự | Mục | Thực hành chính |
|---|---|---|
| 1 | Chỉ thị | Hội thoại của các thành viên phòng thí nghiệm, sơ đồ luồng tổng quan |
| 2 | Hồi quy cơ bản | Biểu đồ phân tán dài–nặng và đường dự đoán, cân cá vược (14 con kiểm tra) |
| 3 | Thêm đặc trưng | Thanh trượt degree 1~5, cột R² huấn luyện·kiểm tra, đường dự đoán dao động |
| 4 | Ridge | Thanh trượt alpha, cột 55 hệ số (thang log), so sánh với hệ số trước điều chuẩn |
| 5 | Lasso | Thanh trượt alpha, các hệ số về 0 và bị loại, số đặc trưng còn lại |
| 6 | Chọn alpha | So sánh trung bình kiểm định chéo với điểm kiểm tra, xoay vòng 5 phần để chấm điểm |
| — | Đối đầu | Giữ nguyên 55 đặc trưng vs Ridge, phán quyết bằng tập kiểm tra đã niêm phong |
| 7 | Giới hạn và nhiệm vụ tiếp theo | Làm được·chưa làm được, bảng tóm tắt theo từng bài thực hành |
| A~F | Mã Colab · Prompt ứng dụng AI · Bảng thuật ngữ · Tổng hợp các phép so sánh · Giới thiệu tác giả và tài liệu tham khảo · Mẹo cho người dạy | |
| — | Chỉ mục tri thức · Gói ontology & thư mục tài liệu | Tìm khái niệm, đồ thị quan hệ, gói JSON-LD·Turtle·CSV·BibTeX·RIS (ZIP) |

## Mã Colab

| Mã 1 | Mã 2 | Thư viện | Thời gian chạy |
|---|---|---|---|
| Thêm đặc trưng thì điểm kiểm tra sụp đổ (mục 2·3) | Kìm giữ hệ số và chọn alpha bằng kiểm định chéo (mục 4~6, đối đầu) | numpy, scikit-learn, matplotlib (cài sẵn trên Colab) | Mỗi mã khoảng 2~3 giây trên CPU |

Ở mỗi khung mã, bạn có thể Sao chép · Tải .py · Tải notebook (.ipynb). Đã chạy thử: 2026-10-29, numpy 2.5 · scikit-learn 1.9 · matplotlib 3.11.

## Tệp

```
RG_ridge_lasso.html                    bản gốc tiếng Hàn
RG_ridge_lasso.en.html  .zh.html  .ja.html
RG_ridge_lasso.uz.html  .ru.html  .vi.html
README.md
index.html  index.en.html  index.zh.html  index.ja.html
index.uz.html  index.ru.html  index.vi.html
thumb_rg.webp  og_rg.jpg  hero_rg.webp  (cover_index.webp)
cover_manifest.json
code/rg_code1_overfitting.py  code/rg_code2_ridge_lasso.py
docs/COVER_00_index.md  docs/COVER_RG_ridge_lasso.md
docs/IMG_RG_ridge_lasso.md  docs/KG_00_registry_additions.json
```

| Tệp | Kích thước |
|---|---|
| RG_ridge_lasso.html | 576 KB |
| RG_ridge_lasso.en.html | 576 KB |
| RG_ridge_lasso.zh.html | 569 KB |
| RG_ridge_lasso.ja.html | 583 KB |
| RG_ridge_lasso.uz.html | 585 KB |
| RG_ridge_lasso.ru.html | 623 KB |
| RG_ridge_lasso.vi.html | 590 KB |
| index.html | 15 KB |
| index.en.html | 15 KB |
| index.zh.html | 15 KB |
| index.ja.html | 16 KB |
| index.uz.html | 16 KB |
| index.ru.html | 17 KB |
| index.vi.html | 16 KB |

Mỗi tệp HTML chứa trọn hình ảnh, dữ liệu và mã script trong một tệp. Không cần bước build, chỉ cần mở bằng trình duyệt. Thứ duy nhất tải từ bên ngoài là Google Fonts.

## Bài nên đọc trước

Nếu bạn mới làm quen với hồi quy tuyến tính, hãy bắt đầu từ bài thực hành số 2 (Hồi quy cơ bản) của trang. Khi có số thứ tự trong loạt bài, các bài trước sẽ được liên kết.

## Dữ liệu và hình ảnh

| Nội dung | Tính toán thật hay minh họa? |
|---|---|
| Điểm số·hệ số·cân nặng dự đoán | Tính toán thật (Mã 1·2, scikit-learn 1.9.1) |
| Đường đi trên trục ngang của đường dự đoán | Minh họa. Cá vược giả định với chiều cao·bề rộng ước lượng theo chiều dài |
| Hoạt ảnh xoay vòng 5 phần | Sơ đồ minh họa |
| Phép so sánh vali·cái cân·đề thi cũ | Phép so sánh để giải thích (chỗ không đúng được ghi ở mục D của trang) |
| Hình nhân vật | adminmrobo/fruitfly-lab-expressions (ea5da3f) |

Dữ liệu cá vược: dữ liệu thực hành của Park Haesun, Honja Gongbuhaneun Machine Learning+Deep Learning [Tự học Học máy + Học sâu], bản sửa đổi (Hanbit Media, 2025), tệp perch_full.csv trong kho mã rickiepark/hg-mldl.

## Cách dùng thuật ngữ

- Điều chuẩn (regularization) còn được gọi là "chính quy hóa", nhưng để không nhầm với chuẩn hóa (standardization), trang này thống nhất dùng "điều chuẩn".
- Điều chuẩn của Ridge·Lasso được giải thích từ đầu đến cuối bằng phép so sánh **chiếc vali**. alpha càng lớn thì vali càng nhỏ.
- Mô hình có hệ số lớn được gọi là **cái cân quá nhạy**, còn quá khớp được gọi là **học sinh chỉ học thuộc đề thi cũ**.

## Giấy phép

[Giấy phép Creative Commons Ghi công – Phi thương mại 4.0 Quốc tế (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/deed.vi)

Ví dụ ghi nguồn: "Ridge và Lasso — học cách chống quá khớp qua cân nặng cá vược", Tác giả · Ahn Sangsun, CC BY-NC 4.0.

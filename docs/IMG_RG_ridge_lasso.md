# RG번 「농어 무게로 배우는 릿지와 라쏘」 이미지 제작 명세서

| 항목 | 내용 |
|---|---|
| 페이지 | RG_ridge_lasso.html (시리즈 번호가 정해지면 파일 이름과 키의 `rg`를 번호로 바꿀 것) |
| 모드 / 주 앵커 | 교과서 / D 생활·현장: 연구실 안 계량대 (저울 위 농어 + 여행 가방) |
| 시즌 | 기본 |
| 대결 | 특성 55개 그대로(기본 회귀) vs 릿지 α=10 → 결과 F, 차이 5.365 (테스트 R² 0.9725 vs −4.3927) |
| 새로 그릴 그림 | P1 2장 · P2 2장 · P3 1장 |
| 제작 경로 | 직접 3장 (sc_rg_outro 합성본·thumb_rg·og_rg, 넣음/파일 전달) · 외부 의뢰 2장 필수 + 1장 선택 |
| 의뢰 도구 | Genspark (기본) |
| 진행 | 받음 0 / 의뢰 2 · 마지막 반영 아직 |
| 캐릭터 팩 표정 | 25장 (96px) + 대결 머리 10장 (192px), 팩 커밋 ea5da3f · 로봇은 ahnboat_lab_explainer 그림 팩 1.2의 주판봇 벡터 그림 v1 |
| 재사용 | 0장 (기존 장면 목록을 받지 않음) |
| 그림이 없을 때 | 페이지는 캐릭터 팩 표정, CSS 벌집 배경, 픽셀 캔버스(저울·농어·가방)로 이미 완성 상태 |

## 1. 그림체와 고정 외형
- 스타일: SKILL 18-3 (16비트 SNES 시대 픽셀 아트, 굵은 외곽선, 디더링 음영)
- 캐릭터 고정 외형: SKILL 18-4 표 그대로 (공식 저장소 `CHARACTER_CORE_EN`)
- 이 페이지 장소: 밤의 연구실 한쪽 계량대. 큰 바늘 저울 위에 농어 한 마리, 옆에 반쯤 열린 여행 가방(짐이 눌려 담긴 쪽과 꺼내 둔 짐 몇 개), 뒤쪽 칠판은 빈칸. 보라 조명이 왼쪽에서 들어옴.
- 장소 영어 묘사: *a weighing corner inside the same night lab world, a large dial scale with a single green-striped perch fish lying on its tray, a half-open travel suitcase beside it with some items packed tightly and a few items set aside on the floor, a blank chalkboard in the back, purple lab light spilling in from the left*

## 2. 필요한 그림 전체

| # | 키 | 판 | 크기 | 상태 | 제작 | 우선 | 들어가는 곳 | 대신 쓰는 그림 |
|---|---|---|---|---|---|---|---|---|
| 1 | bg_rg | F | 1920×720 | 의뢰 | 외부 | P1 | 히어로 배경 `.hero-bg` | CSS 그라데이션 + 벌집 무늬 |
| 2 | sc_rg_hero | E | 1200×800 | 의뢰 | 외부 | P1 | 히어로 무대 `.stage` | 팩 캐릭터 4명 + 픽셀 캔버스(저울·농어·가방) 합성 |
| 3 | doc_think → doc_e09 | A | 팩 96 | 팩 | — | — | 히어로 대화창·무대 | — |
| 4 | asst_smile → asst_e13 | B | 팩 96 | 팩 | — | — | 히어로, 등장인물 | — |
| 5 | fly_point → fly_e08 | C | 팩 96·192 | 팩 | — | — | 히어로, 대결 전 | — |
| 6 | robo_coin → robo_e16 | D | 팩 96·192 | 팩 | — | — | 히어로, 대결 전 | — |
| 7 | fly_arms → fly_e16 | C | 팩 192·96 | 팩 | — | — | 대결 후 (F), 아웃트로 | — |
| 8 | robo_sigh → robo_e20 | D | 팩 192 | 팩 | — | — | 대결 후 (F) | — |
| 9 | asst_spark → asst_e01 | B | 팩 96 | 팩 | — | — | 대결 결과 발표 | — |
| 10 | doc_judge → doc_e10 | A | 팩 96 | 팩 | — | — | 판정 | — |
| 11 | fly_cry → fly_e21 · fly_coffee → fly_e13 | C | 팩 192 | 팩 | — | — | 대결 후 (R·D 결과용, 이번 결과에선 안 보임) | — |
| 12 | robo_happy → robo_e12 · robo_meh → robo_e18 · robo_blush → robo_e14 | D | 팩 192 | 팩 | — | — | 대결 후 (R·D·X 결과용), robo_e14는 아웃트로에도 | — |
| 13 | asst_e24 · doc_e13 | A·B | 팩 96 | 팩 | — | — | 대결 후 (X·D 결과용) | — |
| 14 | doc_e08 · fly_e10 · robo_e13 | A·C·D | 팩 96 | 팩 | — | — | 등장인물 카드 | — |
| 15 | fly_e07 · doc_e07 · asst_e10 · robo_e07 · doc_e08 · fly_e10 · asst_e07 · doc_e16 | A~D | 팩 96 | 팩 | — | — | 본문 말풍선 (섹션당 1개) | — |
| 16 | asst_e12 · doc_e07 · robo_e14 | A·B·D | 팩 96 | 팩 | — | — | 대결 전 발표 자리, 아웃트로 | — |
| 17 | sc_rg_outro | E | 1200×800 | 넣음 (합성본) | 직접 → 외부 선택 | P2 | 아웃트로 `.outro-stage` | 팩 캐릭터 CSS 무대 합성 |
| 18 | thumb_rg | I | 600×400 | 넣음 (파일) | 직접 (히어로 무대 합성본 3:2 자르기) | P2 | 목차 카드 (이 HTML 밖) | 색 카드 |
| 19 | og_rg | K | 1200×630 | 넣음 (파일) | 직접 (히어로 화면 캡처 합성) | P3 | 공유 미리보기 (이 HTML 밖) | 없음 |
| — | 행동으로 보기 (농어 저울, 5조각 카드), 히어로 픽셀 소품 | — | — | 코드 | 직접 | — | Canvas 2D | — |

컷(G판)은 넣지 않음: 사다리 다섯 칸이 모두 인터랙티브 도식으로 개념을 보여 주고 있어, 장면 컷이 더할 정보가 적다고 판단함(R5는 "보여 줄 때만").

## 3. 새로 그릴 그림 상세

### 3-1. `bg_rg` — 밤의 연구실 계량대
| 항목 | 내용 |
|---|---|
| 판 · 크기 | F · 1920×720 (8:3, 정수배 가능) |
| 제작 경로 | 외부: Genspark |
| 배경 | 그림 전체 |
| 구도 | 왼쪽 45%는 어둡고 단순(제목 글자 자리). 오른쪽에 저울과 가방, 빛은 저울 위 농어에 모임 |
| 표정·몸짓 | 인물 없음 |
| 소품 | 바늘 저울, 농어, 여행 가방, 꺼내 둔 짐 2~3개, 빈 칠판, 시험관 선반 (글자 없음) |
| 빛·분위기 | 남보라 어둠, 왼쪽 보라 조명, 모니터의 청록 빛, 시험관의 분홍·초록 형광 점 |
| 피할 것 | 글자·숫자 눈금, 실존 브랜드 가방, 생물 해부·현미경 소품 (생물 앵커 아님) |
| 대체 글 (alt) | 밤의 연구실 계량대, 저울 위 농어와 여행 가방이 놓여 있음 |
| 대신 쓰는 그림 | CSS 그라데이션 + 벌집 무늬 |

**프롬프트 (복사해서 사용)**
```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, wide 8:3 background, left side simple and calm for title text, details on the right, a weighing corner inside the same night lab world, a large dial scale with a single green-striped perch fish lying on its tray, a half-open travel suitcase beside it with some items packed tightly and a few items set aside on the floor, a blank chalkboard in the back, a test tube rack with tiny magenta and green glowing vials, purple lab light spilling in from the left, warm light focused on the fish on the scale, no characters, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-2. `sc_rg_hero` — 네 캐릭터가 저울 위 농어를 바라봄
| 항목 | 내용 |
|---|---|
| 판 · 크기 | E · 1200×800 (3:2) |
| 제작 경로 | 외부: Genspark |
| 배경 | 그림 전체 |
| 구도 | 가운데 뒤 저울과 농어. 왼쪽 초파리 연구원이 오른쪽을 보며 가리킴, 오른쪽 주판봇이 왼쪽을 보며 주판알을 반짝임, 박사는 가운데 뒤에서 턱에 손, 하루는 옆에서 빈 줄무늬 장부를 듦. 중요한 것은 위쪽 62% 안 |
| 표정·몸짓 | doc_think, fly_point, robo_coin, asst_smile (18-5 사전) |
| 소품 | 저울, 농어, 여행 가방, 빈 장부 (글자 없음) |
| 빛·분위기 | 밤의 연구실, 저울 위 농어에 빛이 모임 |
| 피할 것 | 승패 암시 표정(결과 전 장면), 글자, 회사 캐릭터 Money-Robo의 특징(흰 둥근 머리·노란 눈·부유·금화) |
| 대체 글 (alt) | 밤의 연구실에서 네 캐릭터가 저울 위 농어와 여행 가방을 바라보는 장면 |
| 대신 쓰는 그림 | 팩 캐릭터 + 픽셀 캔버스 합성 무대 |

**프롬프트 (복사해서 사용)**
```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, a weighing corner inside the same night lab world with a large dial scale holding a single green-striped perch fish and a half-open travel suitcase beside it; the Professor, a chibi male scientist with a big head, dark charcoal spiky hair with a white streak at the front, a small low ponytail at the back, very thick bold black eyebrows, teal-framed rectangular glasses, light peach skin, white lab coat over a black vest, black tie and black slacks, standing at the back center with a hand on his chin and a small question mark; the Fruit Fly, a tiny expressive cartoon fruit fly researcher with a dark charcoal-black segmented insect body, large glossy red compound eyes, a retro dark blue helmet with a yellow-white center stripe and small round side bolts, colorful dangling cables in magenta, purple and blue curving from the back of the helmet, a tiny white lab coat over a black vest, translucent veined wings, six thin black legs with the front pair used like hands, on the left looking right and pointing at the fish with a suspicious look; JUPANBOT (AbaBot), a boxy beige retro CRT-monitor robot with a dark green screen face showing mint pixel eyes and mouth, a short antenna topped with a red-brown abacus bead, gray segmented arms and two small tank treads, on the right looking left with a sly grin, holding up a shiny abacus bead beside a small wooden abacus; Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat, at the side holding a blank striped ledger with a calm small smile, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-3. `sc_rg_outro` — 대결 뒤 (선택)
| 항목 | 내용 |
|---|---|
| 판 · 크기 | E · 1200×800 |
| 제작 경로 | 직접 합성본이 페이지에 있음. 외부 의뢰는 선택 |
| 구도 | 초파리 연구원이 앞·크게 팔짱, 주판봇은 옆에서 머쓱하게 화면에 분홍 빗금(인정하는 몸짓)(인정하는 몸짓), 박사는 검지를 세워 설명, 하루는 주먹 쥐고 응원. 저울 바늘이 안정된 모습 |
| 피할 것 | 조롱하는 몸짓, 글자, 금화·흰 둥근 머리(회사 캐릭터 Money-Robo의 특징) |
| 대체 글 (alt) | 대결을 마친 연구실, 초파리 연구원이 앞에서 팔짱을 끼고 주판봇이 머쓱하게 웃는 장면 |
| 대신 쓰는 그림 | 팩 캐릭터 CSS 무대 합성 |

**프롬프트 (복사해서 사용)**
```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, consistent with the reference images, cozy night laboratory mood, purple light, soft magenta and green fluorescent accents, 3:2 landscape scene, medium brightness, the same weighing corner with the dial scale needle resting steadily and the travel suitcase neatly closed; the Fruit Fly researcher (same design as reference: red compound eyes, dark blue striped helmet with magenta purple blue cables, tiny white lab coat over black vest) in front and larger, arms crossed with a proud sparkle; JUPANBOT (same design as reference: boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes, abacus-bead antenna, gray segmented arms, two tank treads) beside him with drooping pixel eyes and pink blush marks on its screen, a sheepish accepting pose; the Professor (teal rectangular glasses, charcoal spiky hair with white streak, thick black eyebrows, white lab coat, black vest and tie) explaining with one index finger raised; Haru (long pink hair with navy streaks, two hair buns, lavender hoodie under open white lab coat) cheering with a raised fist, no text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands
```

### 3-4. `thumb_rg`, `og_rg` — 직접 (완료)
히어로 화면을 1200×630으로 캡처한 `og_rg.png`, 히어로 무대 합성본을 3:2로 자른 `thumb_rg.png`(600×400)를 함께 전달함. `bg_rg`·`sc_rg_hero`를 받으면 그 그림으로 다시 만들 것.

## 4. 일관성 지침
- 참고 이미지: 공식 저장소 `refs/original/keyart_rivals.png`(넷이 함께) + `images/doctor/E09_*.png`, `images/fruitfly/E08_guiding.png`, `images/jupanbot/E16_proud.png`, `images/haru/E13_*.png`
- 같은 캐릭터는 같은 세션에서, 시드 고정 가능하면 고정: 박사 1101, 조수 1102, 초파리 1103, 로봇 1104
- 표정만 바꿀 때 추가 문장: *same character, same size and position, only change the facial expression and pose to ...*
- 투명 배경이 안 되면: *solid flat #00ff00 background*

## 5. 넘겨받은 뒤 처리
SKILL 18-15 절차 그대로 (키 맞추기 → 눈으로 검수 → `--ingest` → 페이지에 넣기 → 상태 갱신 → 점검 → 전달).
```bash
python3 build_character_pack.py --ingest 받은폴더/ --plates bg_rg=F,sc_rg_hero=E,sc_rg_outro=E --out received_rg
```

## 6. 체크리스트
- [x] HTML의 `data-img` 키가 모두 이 명세서에 있음 (thumb_rg·og_rg는 HTML 밖 산출물)
- [x] 대결 결과 후 표정이 5-8 표와 일치 (F: fly_arms, robo_sigh)
- [x] 결과 전 그림에 승패 암시 없음 (fly_point, robo_coin)
- [x] 모든 프롬프트에 고정 외형과 금지 구절
- [x] 팩에 있는 표정을 새로 그림에 넣지 않음
- [x] 장소가 주 앵커(D)와 일치, 초파리 해부·현미경 소품 없음
- [x] P1 2장 (6장 이하)
- [x] 페이지 그림 합계: 팩 표정 약 287 KB (base64, 400 KB 이하 → 530 KB 기준 안)

## 8. 외부 의뢰 묶음 (Genspark에 그대로 붙여 넣기)

같은 세션에서 이 순서대로: 배경 → 히어로 장면 → (선택) 아웃트로 장면.

### 의뢰 1/3 · `bg_rg`
- **올릴 참고 이미지:** 없음 (배경만)
- **크기·비율:** 1920×720 (8:3) 이상
- **배경:** 그림 전체
- **받을 파일 이름:** `bg_rg.png`
- **프롬프트:** 3-1의 완성 프롬프트 그대로
- **네거티브:** `blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, text, letters, watermark`
- **확인할 것:** 저울 눈금에 숫자가 그려지면 다시

### 의뢰 2/3 · `sc_rg_hero`
- **올릴 참고 이미지:** `refs/original/keyart_rivals.png`, `images/fruitfly/E08_guiding.png`, `images/jupanbot/E16_proud.png`
- **크기·비율:** 1200×800 (3:2) 이상
- **배경:** 그림 전체
- **받을 파일 이름:** `sc_rg_hero.png`
- **프롬프트:** 3-2의 완성 프롬프트 그대로
- **네거티브:** `blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark`
- **확인할 것:** 박사 안경이 둥글게 나오면 다시, 하루 앞머리 가운데 남색 줄이 없으면 다시

### 의뢰 3/3 · `sc_rg_outro` (선택)
- **올릴 참고 이미지:** `refs/original/keyart_rivals.png`, `images/fruitfly/E16_proud.png`, `images/jupanbot/E14_*.png`
- **크기·비율:** 1200×800 (3:2) 이상
- **받을 파일 이름:** `sc_rg_outro.png`
- **프롬프트:** 3-3의 완성 프롬프트 그대로
- **확인할 것:** 주판봇이 조롱당하는 구도면 다시 (인정하는 몸짓이어야 함)

## 7. 매니페스트
```json
{
  "page": "RG_ridge_lasso",
  "anchor": "D:weighing-corner",
  "season": "default",
  "duel": {"result": "F", "gap": 5.3652},
  "images": [
    {"key":"bg_rg","plate":"F","size":[1920,720],"maker":"external","tool":"genspark","status":"requested","priority":"P1","slot":"hero-bg","fallback":"css","alt":"밤의 연구실 계량대, 저울 위 농어와 여행 가방이 놓여 있음"},
    {"key":"sc_rg_hero","plate":"E","size":[1200,800],"maker":"external","tool":"genspark","status":"requested","priority":"P1","slot":"hero-stage","fallback":"composite","alt":"밤의 연구실에서 네 캐릭터가 저울 위 농어와 여행 가방을 바라보는 장면"},
    {"key":"sc_rg_outro","plate":"E","size":[1200,800],"maker":"claude","status":"placed","priority":"P2","slot":"outro","fallback":"composite","external_optional":true,"alt":"대결을 마친 연구실, 초파리 연구원이 앞에서 팔짱을 끼고 주판봇이 머쓱하게 웃는 장면"},
    {"key":"thumb_rg","plate":"I","size":[600,400],"maker":"claude","status":"placed","priority":"P2","slot":"index-card","alt":"농어 무게로 배우는 릿지와 라쏘 목차 카드"},
    {"key":"og_rg","plate":"K","size":[1200,630],"maker":"claude","status":"placed","priority":"P3","slot":"og","alt":"농어 무게로 배우는 릿지와 라쏘 페이지 미리보기"},
    {"key":"doc_think","pack":"doc_e09","plate":"A","size":96,"status":"pack","slot":"hero-dialog","alt":""},
    {"key":"fly_point","pack":"fly_e08","plate":"C","size":192,"status":"pack","slot":"duel-before","alt":""},
    {"key":"robo_coin","pack":"robo_e16","plate":"D","size":192,"status":"pack","slot":"duel-before","alt":""},
    {"key":"fly_arms","pack":"fly_e16","plate":"C","size":192,"status":"pack","slot":"duel-after","alt":""},
    {"key":"robo_sigh","pack":"robo_e20","plate":"D","size":192,"status":"pack","slot":"duel-after","alt":""},
    {"key":"asst_spark","pack":"asst_e01","plate":"B","size":96,"status":"pack","slot":"duel-result","alt":""},
    {"key":"doc_judge","pack":"doc_e10","plate":"A","size":96,"status":"pack","slot":"duel-verdict","alt":""}
  ],
  "character_pack": {"repo":"adminmrobo/fruitfly-lab-expressions","commit":"ea5da3f"},
  "status_values": "pack | placed(직접, 넣음) | requested(의뢰) | received(받음) | applied(반영) | rejected(다시 의뢰)"
}
```

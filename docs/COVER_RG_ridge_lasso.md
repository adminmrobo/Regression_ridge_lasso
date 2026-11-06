# 표지 지시문 — RG 릿지와 라쏘 (해설 페이지)

| 항목 | 내용 |
|---|---|
| 키 · 판 | `cover_rg` · L (16:9, 가로 1920 이상) |
| 페이지 | `RG_ridge_lasso.html` 외 6개 언어판 |
| 받은 뒤 파일 이름 | `cover_rg.webp` (1600×900, 220 KB 이하). 지금 페이지에는 표지 자리가 없다. 넣으려면 "표지를 넣어 줘"라고 요청한다 → 상단 내비 아래에 `<!-- lab-cover -->` 블록으로 더한다(본문은 그대로). 목차 카드 썸네일 `thumb_rg.webp`, 공유 미리보기 `og_rg.jpg`도 이 그림으로 다시 자른다 |
| 장소 (앵커 D) | 밤의 연구실 한쪽 계량대를 가까이 본 장면 |
| 주제 은유 | **여행 가방 두 개**: 계량대 위 큰 바늘 저울에 농어 한 마리. 저울 왼쪽 가방은 짐을 모두 눌러 압축해 담은 꽉 찬 가방(릿지), 오른쪽 가방은 꼭 필요한 짐 몇 개만 담고 나머지 짐을 바닥에 꺼내 둔 가방(라쏘). 저울 바늘은 아직 흔들리는 중 |
| 네 캐릭터 포즈 | 박사: 가운데 뒤에서 두 가방을 번갈아 가리키며 설명 / 조수(하루): 한쪽 옆에서 빈 줄무늬 장부와 펜을 들고 바늘을 지켜봄 / 초파리 연구원: 왼쪽에서 오른쪽을 보며, 꺼내 둔 짐 하나를 들어 올려 살펴봄 / 주판봇: 오른쪽에서 왼쪽을 보며, 짐을 더 넣으려는 듯 큰 상자를 안고 자신만만하게 웃음 |
| 대체 글 (alt) | 밤의 연구실 계량대에서 저울 위 농어를 두고, 짐을 눌러 담은 가방과 짐을 덜어 낸 가방을 박사가 가리키고 조수(하루)·초파리 연구원·주판봇이 지켜보는 표지 |
| 결과 암시 | 없음. 대결 전 장면이다 (주판봇은 자신만만, 초파리는 의심, 승패 표정 없음) |
| 목차 표지와 다른 점 | 목차(`COVER_00_index.md`): 연구실 전경, 벽의 두 곡선. 페이지: 계량대를 가까이 본 장면, 두 가방. 그래프 판은 넣지 않는다 |
| 피할 것 | 그림 안 글자·숫자·로고, 저울 눈금 숫자, 금화·지폐, 회사 로고의 하얀 로봇(옛 Money-Robo), 현미경·초파리 해부 소품 |

**참고 이미지 (함께 올리기):** 네 캐릭터 기본 그림 4장 (`adminmrobo/fruitfly-lab-expressions`의 `images/doctor/E13_neutral.png` · `images/haru/E13_neutral.png` · `images/fruitfly/E13_neutral.png` · `images/jupanbot/E13_neutral.png`). 목차 표지를 먼저 받았다면 그것도 그림체 참고로 함께 올린다.

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상 (처음부터 1920 이상으로 생성)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 그림체·같은 외형으로, 넷 모두 등장
- 키 순서는 박사 ≥ 조수 > 주판봇 > 초파리 (초파리는 박사 키의 약 0.4)
- 그림 안에 글자·숫자·로고를 넣지 말 것 (저울 눈금에도 숫자 없이)
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 어둡고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Match the art style, proportions and colors of the attached reference images exactly
(if there are no reference images: 16-bit RPG style pixel art, bold dark outline, 2–3 tone shading, small highlights).
Cozy night laboratory mood, purple light, soft magenta and green fluorescent accents.
Scene: a close view of a weighing corner inside the night lab; a large dial scale on a sturdy bench with one green-striped perch fish lying on its tray, the needle still swinging (the dial has no numbers).
Two travel suitcases stand on either side of the scale: the left one is packed full with every item squeezed and compressed to fit; the right one holds only a few essential items, and the other items are taken out and set neatly on the floor beside it.
All four characters together:
chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, standing at the back center pointing from one suitcase to the other as he explains;
girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side holding a blank striped ledger and a pen, watching the needle;
anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right, lifting one of the set-aside items to inspect it;
boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and a confident grin, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left, hugging a big box as if to pack even more.
Height order: scientist tallest, then the girl researcher, then the robot, the fruit fly is about 0.4 of the scientist's height.
Visual metaphor: squeeze everything in versus keep only what matters.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom); keep the bottom-left corner dark and simple; the light falls on the perch on the scale between the two suitcases.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no coins, no banknotes, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same art style and composition. Change only: {고칠 점}. Still no text.`

자주 쓸 고칠 점:
- 두 가방이 비슷해 보이면: `make the left suitcase bulging and overstuffed, and the right suitcase clearly half empty with items set aside on the floor`
- 저울에 숫자가 생기면: `remove every number from the scale dial`
- 주판봇이 하얀 로봇으로 나오면: `the robot must be a beige boxy CRT monitor with a dark green screen face and tank treads, exactly like the reference`

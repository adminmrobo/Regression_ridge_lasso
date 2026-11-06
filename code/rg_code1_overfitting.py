# ===============================================================
# 릿지와 라쏘 · 코드 1: 특성을 늘리면 훈련 점수는 오르고 테스트 점수는 무너진다
#  - 라이브러리: numpy, matplotlib, scikit-learn (Colab 기본 설치)
#  - 실행 확인: 2026-10-29, numpy 2.5 · scikit-learn 1.9 · matplotlib 3.11 (CPU 약 2초)
#  - 하는 일: ① 농어 56마리를 훈련 42 · 테스트 14로 나눈다
#            ② degree 1~5로 특성을 늘려 기본 회귀를 학습하고 R²를 잰다
#            ③ 길이 0.5cm 차이에 예측이 얼마나 출렁이는지 본다
#  - 웹페이지 섹션 1·2의 숫자와 같다. 시드를 고정해 언제 실행해도 같다.
# ===============================================================

# ---------- 1. 농어 데이터 ----------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge

# 길이(cm), 높이(cm), 폭(cm)
perch_full = np.array([
    [8.4, 2.11, 1.41], [13.7, 3.53, 2.0], [15.0, 3.82, 2.43], [16.2, 4.59, 2.63], [17.4, 4.59, 2.94],
    [18.0, 5.22, 3.32], [18.7, 5.2, 3.12], [19.0, 5.64, 3.05], [19.6, 5.14, 3.04], [20.0, 5.08, 2.77],
    [21.0, 5.69, 3.56], [21.0, 5.92, 3.31], [21.0, 5.69, 3.67], [21.3, 6.38, 3.53], [22.0, 6.11, 3.41],
    [22.0, 5.64, 3.52], [22.0, 6.11, 3.52], [22.0, 5.88, 3.52], [22.0, 5.52, 4.0], [22.5, 5.86, 3.62],
    [22.5, 6.79, 3.62], [22.7, 5.95, 3.63], [23.0, 5.22, 3.63], [23.5, 6.28, 3.72], [24.0, 7.29, 3.72],
    [24.0, 6.38, 3.82], [24.6, 6.73, 4.17], [25.0, 6.44, 3.68], [25.6, 6.56, 4.24], [26.5, 7.17, 4.14],
    [27.3, 8.32, 5.14], [27.5, 7.17, 4.34], [27.5, 7.05, 4.34], [27.5, 7.28, 4.57], [28.0, 7.82, 4.2],
    [28.7, 7.59, 4.64], [30.0, 7.62, 4.77], [32.8, 10.03, 6.02], [34.5, 10.26, 6.39], [35.0, 11.49, 7.8],
    [36.5, 10.88, 6.86], [36.0, 10.61, 6.74], [37.0, 10.84, 6.26], [37.0, 10.57, 6.37], [39.0, 11.14, 7.49],
    [39.0, 11.14, 6.0], [39.0, 12.43, 7.35], [40.0, 11.93, 7.11], [40.0, 11.73, 7.22], [40.0, 12.38, 7.46],
    [40.0, 11.14, 6.63], [42.0, 12.8, 6.87], [43.0, 11.93, 7.28], [43.0, 12.51, 7.42], [43.5, 12.6, 8.14],
    [44.0, 12.49, 7.6]])
# 무게(g)
perch_weight = np.array([
    5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0, 115.0, 125.0, 130.0, 120.0,
    120.0, 130.0, 135.0, 110.0, 130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
    218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0, 556.0, 840.0, 685.0, 700.0, 700.0,
    690.0, 900.0, 650.0, 820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0, 1000.0])

train_input, test_input, train_target, test_target = train_test_split(
    perch_full, perch_weight, random_state=42)
print('훈련', len(train_input), '마리 / 테스트', len(test_input), '마리')

# ---------- 2. degree 1~5로 특성 늘리기 ----------
rows = []
for degree in range(1, 6):
    poly = PolynomialFeatures(degree=degree, include_bias=False).fit(train_input)
    ss = StandardScaler().fit(poly.transform(train_input))        # 훈련 데이터로만 맞춘다
    tr = ss.transform(poly.transform(train_input))
    te = ss.transform(poly.transform(test_input))
    lr = LinearRegression().fit(tr, train_target)
    rows.append((degree, tr.shape[1], lr.score(tr, train_target), lr.score(te, test_target),
                 np.abs(lr.coef_).max()))
    print(f'degree {degree}: 특성 {tr.shape[1]:2d}개  훈련 R² {rows[-1][2]:.4f}  '
          f'테스트 R² {rows[-1][3]:8.4f}  가장 큰 계수 {rows[-1][4]:12,.1f}')

# ---------- 3. 길이 0.5cm 차이에 예측이 얼마나 출렁이나 ----------
fish = np.array([[18.0, 5.22, 3.32]])      # 테스트 농어 (실제 100g)
fish2 = fish + [[0.5, 0, 0]]               # 길이만 0.5cm 늘림
poly5 = PolynomialFeatures(degree=5, include_bias=False).fit(train_input)
ss5 = StandardScaler().fit(poly5.transform(train_input))
f5 = lambda a: ss5.transform(poly5.transform(a))
lr5 = LinearRegression().fit(f5(train_input), train_target)
rd5 = Ridge(alpha=0.1).fit(f5(train_input), train_target)
for name, m in [('기본 회귀', lr5), ('릿지 α=0.1', rd5)]:
    a, b = m.predict(f5(fish))[0], m.predict(f5(fish2))[0]
    print(f'{name}: 18.0cm → {a:.0f}g, 18.5cm → {b:.0f}g (차이 {b - a:.0f}g)')

# ---------- 4. 그래프 ----------
d = [r[0] for r in rows]
plt.plot(d, [r[2] for r in rows], 'o-', label='train R2')
plt.plot(d, [r[3] for r in rows], 's--', label='test R2')
plt.axhline(0, color='gray', lw=0.8)
plt.xlabel('degree'); plt.ylabel('R2'); plt.legend(); plt.show()

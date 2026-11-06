# ===============================================================
# 릿지와 라쏘 · 코드 2: 계수를 묶어 과적합 막기와 alpha 고르기
#  - 라이브러리: numpy, matplotlib, scikit-learn (Colab 기본 설치)
#  - 실행 확인: 2026-10-29, numpy 2.5 · scikit-learn 1.9 · matplotlib 3.11 (CPU 약 5초)
#  - 하는 일: ① 특성 55개(degree 5)를 표준화한다
#            ② alpha 후보 6개마다 릿지·라쏘의 훈련·테스트 R²와 남은 계수를 잰다
#            ③ 5겹 교차 검증으로 alpha를 고르고, 봉인한 테스트로 한 번만 채점한다
#  - 웹페이지 섹션 3~5와 대결의 숫자와 같다. 시드를 고정해 언제 실행해도 같다.
# ===============================================================

# ---------- 1. 농어 데이터와 특성 55개 ----------
import warnings
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
warnings.filterwarnings('ignore')   # 라쏘의 '덜 수렴' 경고를 숨긴다

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
poly = PolynomialFeatures(degree=5, include_bias=False).fit(train_input)
ss = StandardScaler().fit(poly.transform(train_input))      # 규제 전에 꼭 표준화
train_scaled = ss.transform(poly.transform(train_input))
test_scaled = ss.transform(poly.transform(test_input))
names = poly.get_feature_names_out(['L', 'H', 'W'])          # 길이·높이·폭
print('특성 수:', train_scaled.shape[1])

# ---------- 2. alpha마다 릿지와 라쏘 ----------
alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
scores = {'ridge': ([], []), 'lasso': ([], [])}
for alpha in alpha_list:
    ridge = Ridge(alpha=alpha).fit(train_scaled, train_target)
    lasso = Lasso(alpha=alpha, max_iter=10000).fit(train_scaled, train_target)
    for key, m in [('ridge', ridge), ('lasso', lasso)]:
        scores[key][0].append(m.score(train_scaled, train_target))
        scores[key][1].append(m.score(test_scaled, test_target))
    print(f'alpha {alpha:>7}: 릿지 훈련 {scores["ridge"][0][-1]:.4f} 테스트 {scores["ridge"][1][-1]:.4f} | '
          f'라쏘 훈련 {scores["lasso"][0][-1]:.4f} 테스트 {scores["lasso"][1][-1]:.4f} '
          f'남은 계수 {np.sum(lasso.coef_ != 0)}개')

# ---------- 3. 교차 검증으로 alpha 고르기 ----------
params = {'alpha': alpha_list}
ridge_cv = GridSearchCV(Ridge(), params, cv=5).fit(train_scaled, train_target)
lasso_cv = GridSearchCV(Lasso(max_iter=10000), params, cv=5).fit(train_scaled, train_target)
for name, g in [('릿지', ridge_cv), ('라쏘', lasso_cv)]:
    best = g.best_estimator_
    print(f'{name}: 고른 alpha {g.best_params_["alpha"]}, 교차 검증 평균 {g.best_score_:.4f}, '
          f'테스트 R² {best.score(test_scaled, test_target):.4f}, 0이 아닌 계수 {np.sum(best.coef_ != 0)}개')
print('라쏘가 남긴 특성:', list(names[lasso_cv.best_estimator_.coef_ != 0]))

# ---------- 4. 대결: 규제 없음 vs 릿지 ----------
lr = LinearRegression().fit(train_scaled, train_target)
print(f'대결 테스트 R² — 규제 없음 {lr.score(test_scaled, test_target):.4f}, '
      f'릿지 α={ridge_cv.best_params_["alpha"]} {ridge_cv.best_estimator_.score(test_scaled, test_target):.4f}')

# ---------- 5. 그래프 ----------
x = np.log10(alpha_list)
for key, mark in [('ridge', 'o'), ('lasso', 's')]:
    plt.plot(x, scores[key][0], mark + '-', label=key + ' train')
    plt.plot(x, scores[key][1], mark + '--', label=key + ' test')
plt.xlabel('log10(alpha)'); plt.ylabel('R2'); plt.ylim(0.85, 1.0); plt.legend(); plt.show()
